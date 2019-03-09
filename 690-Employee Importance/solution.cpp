/*
// Employee info
class Employee {
public:
    // It's the unique ID of each node.
    // unique id of this employee
    int id;
    // the importance value of this employee
    int importance;
    // the id of direct subordinates
    vector<int> subordinates;
};
*/
class Solution {
public:
    int getImportance(vector<Employee*> employees, int id) {
        unordered_map<int,Employee*> employees_map;
        for(auto &employee : employees) {
            employees_map[employee->id] = employee;
        }
        return getImportanceHelper(employees_map,id);
    }
    
    int getImportanceHelper(unordered_map<int,Employee*> employees_map, int id) {
        if(employees_map[id]->subordinates.empty()) return employees_map[id]->importance;
        int res = employees_map[id]->importance;
        for(auto &subordinate : employees_map[id]->subordinates) {
            res += getImportanceHelper(employees_map,subordinate);
        }
        return res;
    }
};
