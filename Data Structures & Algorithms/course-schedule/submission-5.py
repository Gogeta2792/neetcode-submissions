class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for course, prereq in prerequisites:
            adj[course].append(prereq)
        
        taken = set()

        def dfs(course):
            if adj[course] == []:
                return True

            if course in taken:
                return False
            
            taken.add(course)

            for prereq in adj[course]:
                if not dfs(prereq):
                    return False
            
            taken.remove(course)

            adj[course] = []

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True