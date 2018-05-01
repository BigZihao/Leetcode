Search

DFS for graph need to use visited:

course schedule, evaluate division, word search, friend circle, number of island

边界处理在 DFS 一开始做，免得后面的多向 DFS 里再重写
如果要 backtrack，就先把自己格子设成其他字符再 DFS，免得死循环