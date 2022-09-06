#есть ли петли? petlyy(n,ms)
#может ли данная матрица быть матрицей смежности простого неориентированного графа. orientir(n,ms)
#перевод матрицы смещности в список ребер неориентированного графа ms_to_sr(n,ms)
#кол-во ребер в графе count_edges_neorintir(n,ms ) (считает с петлями)
#перевод матрицы смежности ориентированного графа в список ребер ms_to_sr_orientir(n,ms)
#кол-во ребер в ориентировванном графе count_edges_orientir(n,ms):
#оптимизированный перевод матрицы смежности в список ребер ориентированного графа ms_to_sr_orientir_2_0(n,ms):
#перевод списка ребер обычного в матрицу смежности sr_to_ms(n,m,sr):
#перевод списка ребер ориентированного графа в матрицу смежности sr_to_ms_orientir(n,m,sr):
#вывод матрицы в виде таблицы vyyyvod_matric(ms)
#Простой неориентированный граф задан матрицей смежности, выведите его пред- ставление в виде списка смежности. ms_to_ssm_neorientir(n,ms)
#Простой неориентированный граф задан списком ребер, выведите его представле- ние в виде списка смежности. def sr_to_smm_neorientir(n,m,sr):
#Простой ориентированный граф задан списком ребер, выведите его представление в виде списка смежности. sr_to_smm_orientir(n,m,sr):
#Простой неориентированный граф задан списком смежности, выведите его пред- ставление в виде матрицы смежности. smm_to_ms_neorientir(n,smm):
def count_edges_orientir(n,ms):
    c=0
    for i in range(n):
        for j in range(i,n):
            if ms[i][j]!=0:
                c+=1
            if ms[i][j]==0 and ms[j][i]!=0:
                c+=1
    return c

def ms_to_sr_orientir_2_0(n,ms):
    e=[]
    for i in range(n):
        for j in range(i,n):
            if ms[i][j]!=0:
                e.append([i,j])
            if ms[i][j]==0 and ms[j][i]!=0:
                e.append([j,i])
    return e

def count_edges_neorientir(n,ms):
    c=0
    for i in range(n):
        for j in range(i,n):
            if ms[i][j]==1:
                c+=1
    return c

def petlyy(n,ms):
    flag=False
    for i in range(n):
        for j in range(i,n):
            if ms[i][j]==ms[j][i] and i==j and ms[i][j]!=0 and (ms[j][i]!=0):
                flag=True
        if flag:
            return "Yes"
    return "NO"
    
def orientir(n,ms):
    flag=True
    for i in range(n):
        for j in range(n):
            if (ms[i][j]!=ms[j][i]) or ((i==j)  and (ms[i][j]==ms[j][i]) and (ms[i][j]!=0)and (ms[j][i]!=0)) :
                flag=False
                
        if not flag:
            return "No"
    return "Yes"      


def ms_to_sr(n,ms):
    e=[]
    for i in range(n):
        for j in range(i,n):
            if ms[i][j]==1:
                e.append([i,j])
    return e


def ms_to_sr_orientir(n,ms):
    e=[]
    for i in range(n):
        for j in range(n):
            if ms[i][j]==1:
                e.append([i,j])
    l=len(e)
    i=0
    while i<l:
        a,b=e[i]
        j=i+1
        while j<l:
            if (e[j]==[b,a]):
                del e[j]
                l=len(e)
                break
            
            j+=1
        i+=1
    return e

def sr_to_ms(n,m,sr):
    ms=[]
    for i in range(n):
        ms.append([0]*n)
    for i in range(m):
        fist=sr[i][0]
        two=sr[i][1]
        ms[fist][two]=1
        ms[two][fist]=1
    return ms

def vyyyvod_matric(ms):
    for i in range(len(ms)):
        print(ms[i],sep='\n')
    return ""

def sr_to_ms_orientir(n,m,sr):
    ms=[]
    for i in range(n):
        ms.append([0]*n)
    for i in range(m):
        first=sr[i][0]
        two=sr[i][1]
        ms[first][two]=1
    return ms

def ms_to_ssm(n,ms):
    ssm=[]
    for i in range(n):
        ssm.append([])
    for i in range(n):
        for j in range(n):
            if ms[i][j]!=0:
                ssm[i].append(j+1)
    return  ssm

def read_matrica(n):
    ms=[]
    for i in range(n):
        ms.append([int(j) for j in input().split()])
    return ms

def read_sp_reber(m):
    e=[]
    for i in range (m):
        a,b=map(int,input().split())
        e.append([a-1,b-1])
    return e

def sr_to_smm_neorientir(n,m,sr):
    smm=[]
    for  i in range(n):
        smm.append([])
    for i in range(m):
        for j in range(2):
            smm[sr[i][j]].append((sr[i][j-1])+1)
            
    for i in range(n):
        (smm[i]).sort()
    return smm

def sr_to_smm_orientir(n,m,sr):
    smm=[]
    for  i in range(n):
        smm.append([])
    for i in range(m):
        smm[sr[i][0]].append((sr[i][1])+1)
        
    for i in range(n):
        (smm[i]).sort()
    return smm

def read_smm(n):
    smm=[]
    for i in range(n):
        smm.append([int(j) for j in input().split()])
    return smm

def smm_to_ms_neorientir(n,smm):
    
    ms=[]
    for i in range(n):
        ms.append([])
    for i in range(n):
        for j in range(n):
            ms[i].append(0)

    for i  in range(n):
        for j in range(len(smm[i])):
            print(1)
            ms[i][(smm[i][j])-1]=1
            
    return(ms)

def preobroz_smm(n,smm):
    for i in range(n):
        for j in range(len(smm[i])):
            smm[i][j]-=1
    return smm

def dfs_mag(v,smm,vkonech):
    visited=[False]*len(smm)
    proverka=dfs(v-1,smm,visited)
    return proverka[vkonech-1]

def dfs(v,smm,visited):
    visited[v]=True
    for u in range(len(smm[v])):
        if not visited[smm[v][u]]:
            dfs(smm[v][u],smm,visited)
    return visited

def bfs(v,smm):
    visited=[False]*len(smm)
    visited[v]=True
    queue=[]
    queue.append(v)
    while (len(queue)>0):
        v=queue.pop(0)
        for u in range(len(smm[v])):
            if not visited[smm[v][u]]:
                visited[smm[v][u]]=True
                queue.append(smm[v][u])
    return visited

def dijk(v,ms,smm):
    visited=[False]*len(smm)
    d=[]
    for i in range(len(smm)):
        d.append(10000000000)
    d[v]=0

    for i in range(len(smm)):
        min_d=1000000
        min_v=-1
        for j in range(len(smm)):
            if (d[j]<min_d) and (not visited[j]):
                min_d=d[j]
                min_v=j
        if min_d==1000000:
            break

        for u in range(len(smm[min_v])):
            if not visited[smm[min_v][u]]:
                    
                d[smm[min_v][u]]=min(d[smm[min_v][u]],d[min_v]+ms[min_v][smm[min_v][u]])

        visited[min_v]=True
    return d

def bellman(v,ms,smm):
    n=len(smm)
    a=[]
    for i in range(n):
        a.append([])
    for i in range(n):
        for j in range(n):
            a[i].append(100000000)

    a[v][0]=0
    

    for j in range(1,n):
        for i in range(n):
            
            a[i][j]=a[i][j-1]

            for u in range(len(smm[i])):
                a[i][j]=min(a[i][j],a[smm[i][u]][j-1]+ms[smm[i][u]][i])

     
    return a   




n=int(input())

ms=read_matrica(n)
smm=ms_to_ssm(n,ms)

preobraz=preobroz_smm(n,smm)
dddjk=dijk(0,ms,preobraz)
bell= vyyyvod_matric( bellman(0,ms,preobraz))

print(bell)
















