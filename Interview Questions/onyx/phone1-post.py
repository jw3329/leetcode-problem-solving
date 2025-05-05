from pydantic import BaseModel
from collections import defaultdict
from typing import List


SECTION_SEPARATOR_PAT = " ... "
DOCUMENT_SEPARATOR_PAT = "\n-----\n"


class Document(BaseModel):
    document_id: int


class Chunk(BaseModel):
    chunk_id: int
    content: str
    score: float
    source_document: Document


class Section(BaseModel):
    central_chunk: Chunk
    chunks: list[Chunk]
    combined_content: str


def merge_sections(sections: list[Section]) -> list[Section]:
    # Group sections by document_id
    doc_sections = defaultdict(list)
    for section in sections:
        doc_id = section.central_chunk.source_document.document_id
        doc_sections[doc_id].append(section)

    merged_sections = []

    for doc_id, sects in doc_sections.items():
        # Sort sections by starting chunk_id
        sects.sort(key=lambda s: s.chunks[0].chunk_id)
        merged = []

        for section in sects:
            if not merged:
                merged.append(section)
                continue

            last = merged[-1]
            # Check overlap between last and current
            last_ids = {chunk.chunk_id for chunk in last.chunks}
            curr_ids = {chunk.chunk_id for chunk in section.chunks}

            if last_ids & curr_ids:
                # Merge overlapping sections
                combined_chunks = {c.chunk_id: c for c in last.chunks + section.chunks}
                merged_chunks = sorted(
                    combined_chunks.values(), key=lambda c: c.chunk_id
                )
                central_chunk = max(merged_chunks, key=lambda c: c.score)
                combined_content = " ".join([c.content for c in merged_chunks])
                merged[-1] = Section(
                    central_chunk=central_chunk,
                    chunks=merged_chunks,
                    combined_content=combined_content,
                )
            else:
                merged.append(section)

        merged_sections.extend(merged)

    return merged_sections


def build_prompt(merged_sections: list[Section]) -> str:
    # Group sections by document
    doc_to_sections = defaultdict(list)
    for section in merged_sections:
        doc_id = section.central_chunk.source_document.document_id
        doc_to_sections[doc_id].append(section)

    # Get document scores = max section score per document
    doc_scores = {
        doc_id: max(s.central_chunk.score for s in sections)
        for doc_id, sections in doc_to_sections.items()
    }

    # Sort documents by score descending
    sorted_docs = sorted(doc_to_sections.items(), key=lambda x: -doc_scores[x[0]])

    final_output = []
    for doc_id, sections in sorted_docs:
        # Sort sections by chunk start
        sections.sort(key=lambda s: s.chunks[0].chunk_id)
        doc_text = SECTION_SEPARATOR_PAT.join(s.combined_content for s in sections)
        final_output.append(doc_text)

    return DOCUMENT_SEPARATOR_PAT.join(final_output)


# TESTING IT
combined = merge_sections([section_1, section_2, section_3, section_4])

prompt = build_prompt(combined)

print(prompt)
