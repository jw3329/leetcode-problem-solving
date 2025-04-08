from pydantic import BaseModel


# Additional Reqs:
# - The central_chunk of a Section is always the Chunk with the highest score.
# - Don't merge Sections from different documents.
# - Print out the full combined text of the documents in order of the highest scoring documents. The document score is also the score of the highest scoring section within it.

# Assumptions
# - The Sections can be passed into merge_sections in any order and it must work
# - The Chunks of a Section are consecutive and always from the same document


# Use the following when printing out the final string
SECTION_SEPARATOR_PAT = " ... "
DOCUMENT_SEPARATOR_PAT = "\n-----\n"


class Document(BaseModel):
  # The real documents have much more info but for this example
  # all that is needed is the ID
  document_id: int


class Chunk(BaseModel):
  # First Chunk of the doc will have ID 0, then 1, then 2, etc.
  chunk_id: int
  content: str
  score: float

  source_document: Document


class Section(BaseModel):
  # The Section will have the list of Chunks in sorted order
  central_chunk: Chunk
  # For simplicity, this also includes the Central Chunk
  # We can also assume it is sorted by chunk_id
  chunks: list[Chunk]
  combined_content: str


# Feel free to play or change any of this data
doc_0 = Document(document_id=0)
doc_1 = Document(document_id=1)

# Consecutive Chunks from the first document
d0_c2 = Chunk(
  chunk_id=2, content="Let's", score=0.6, source_document=doc_0,
)

d0_c3 = Chunk(
  chunk_id=3, content="crush", score=0.1, source_document=doc_0,
)

d0_c4 = Chunk(
  chunk_id=4, content="this", score=0.5, source_document=doc_0,
)

d0_c5 = Chunk(
  chunk_id=5, content="challenge", score=0.7, source_document=doc_0,
)

# Later Chunk from the first document
d0_c8 = Chunk(
  chunk_id=8, content="together", score=0.3, source_document=doc_0,
)

# Chunk from the second document
d1_c3 = Chunk(
  chunk_id=3, content="Good Luck!", score=0.9, source_document=doc_1,
)

# Sections 1 and 2 should be merged
section_1 = Section(
  central_chunk=d0_c2,
  chunks=[d0_c2, d0_c3, d0_c4],
  # Don't use a string overlap to calculate combined_content when merging 
  # Sections. Aggregate from the chunks to generate this for each Section
  combined_content="Let's crush this"
)

section_2 = Section(
  central_chunk=d0_c5,
  chunks=[d0_c3, d0_c4, d0_c5],
  combined_content="crush this challenge"
)

# Section 3 is from the same document and needs to be printed after the other two
# with a ... in between
section_3 = Section(
  central_chunk=d0_c8,
  chunks=[d0_c8],
  combined_content="together"
)

# Section 4 is from a different document
section_4 = Section(
  central_chunk=d1_c3,
  chunks=[d1_c3],
  combined_content="Good Luck!"
)


# Feel free to update the function definitions if you'd like
def merge_sections(sections: list[Section]) -> list[Section]:
  """Merge the Sections into larger Sections"""
  # iterate sections
  # for each section, find if there's any connected chunks
  # connect -> if there's anything that next to last chunk
  # if no connected, then append to result
  # if connected, merge chunks into first one
  # then we should mark merged document to skip next
  # try to refine each sections in result, chunks with central chunk and combined content

  def connected(section: Section):
    for i in range(len(sections)):
      if overlaps(section.chunks[-1], sections[i].chunks[0]):
        return True
    return False

  def overlaps(a: Chunk, b: Chunk):
    if a.source_document.document_id != b.source_document.document_id: return False
    return b.chunk_id <= a.chunk_id

  def is_connected(sec1: Section, sec2: Section):
    return overlaps(sec1.chunks[-1], sec2.chunks[0])

  def merge(sec1: Section, sec2: Section):
    # first merge chunks
    # iterate chunks, get central_chunk
    # combine content
    new_chunks = sec1.chunks
    for chunk in sec2.chunks:
      new_chunks_id = list(map(lambda x: x.chunk_id, new_chunks))
      if chunk.chunk_id not in new_chunks_id:
        new_chunks.append(chunk)
    # now chunks are there
    # iterate to grab central chunk and combine content
    new_content = new_chunks[0].content
    new_central_chunk = new_chunks[0]
    for i in range(1, len(new_chunks)):
      if new_central_chunk.score < new_chunks[i].score:
        new_central_chunk = new_chunks[i]
      new_content += new_chunks[i].content
    sec1.chunks = new_chunks
    sec1.combined_content = new_content
    sec1.central_chunk = new_central_chunk


  res = []
  sections.sort(key=lambda x: (x.chunks[0].source_document.document_id, x.chunks[0].chunk_id))
  for i, section in enumerate(sections):
    if not connected(section):
      res.append(section)
    else:
      if i+1 < len(sections) and is_connected(section, sections[i+1]):
        merge(section, sections[i+1])
      res.append(section)
  return res


def build_prompt(merged_sections: list[Section]) -> str:
  """This function should print the contents of the documents,
  it can just be one string per document"""
  # TODO please complete this function
  return ""


combined = merge_sections(
  # This needs to work even if the section order is random
  sections=[section_1, section_2, section_3, section_4]
)

for sect in combined:
  print(sect)
  print()
prompt = build_prompt(combined)

print(prompt)

# Should print out:
# Good Luck!
# -----
# Let's crush this challenge ... together

