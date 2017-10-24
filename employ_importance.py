class Solution(object):
	def getImportance(self, employees, id):
		emps = {employee.id: employee for employee in employees}
		def dfs(id):
			subordinates_importance = sum([dfs(sub_id) for sub_id in emps[id].subordinates])
			return subordinates_importance + emps[id].subordinates_importance
		return dfs(id)

	def getImportance(self, employees, id):
		d = {e.id: e for e in employees}
		ret = 0
		stk = [d[id]]
		while stk:
			top = stk.pop()
			ret+=top.importance
			for n in top.subordinates:
				stk.append(d[n])
		return ret
