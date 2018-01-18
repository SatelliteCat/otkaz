public void dfs (bool[,] a, List<bool> visited, int n, int v, int x, int cnt)
{
int i = 0;
if (v==x)
{
cnt++;
return;
}
visited[v] = true;
for (i=0;i<n;i++)
{
if (a[v,i] && !(visited[i]))
{
dfs(a, visited, n, i, x, cnt);
}
}
visited[v] = false;
}