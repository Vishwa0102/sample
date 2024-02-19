

#RE TO NFA
rcount=1
symbols=['e','a','b']
re='(a|b)*'
states={}#key : r1,r2 ,value : states 0-r1,1-r1
rval={}#gives rval for the symbol or expression
expressions=[]
table_fin={}
tables={}
exit=False
while re!="":
  e=""
  currenti=0
  for i in range(re.index('(')+1,re.index(')')):
    currenti=i
    e+=re[i]
    if re[i] in symbols:
      if re[i] not in states:
        rvalue='r'+str(rcount)
        states[rvalue]=[]
        states[rvalue].append('0-r'+str(rcount))
        states[rvalue].append('1-r'+str(rcount))
        tables['r'+str(rcount)]={}
        rval[re[i]]='r'+str(rcount)
        for j,s in enumerate(states[rvalue]):
          tables['r'+str(rcount)][s]=['-']*len(symbols)
          if j==0:
            tables['r'+str(rcount)][s][symbols.index(re[i])]=states[rvalue][1]
          table_fin['r'+str(rcount)]=tables['r'+str(rcount)]
        rcount+=1
      if len(e)>=2:
        rval[e]='r'+str(rcount)
        rvalue=rval[e]
        sepIndex=''
        for index in range(len(e)-1,-1,-1):
          if e[index] not in symbols:
            sepIndex=index
            break
        #print('e = ',e)
        #print('rvalue',rvalue)
        if e[sepIndex]=='|':
          #print("JIi")
          tables[rvalue]={}
          currtable=tables[rvalue]
          #A=e[:e.index('|')]
          #B=e[e.index('|')+1:]
          A=e[:sepIndex]
          B=e[sepIndex+1:]
          r1=rval[A]
          r2=rval[B]
          currtable['0-'+rvalue]=['-']*len(symbols)
          #print("rvall ",rvalue)
          currtable['0-'+rvalue][0]=[states[r1][0],states[r2][0]]
          currtable.update(tables[r1])
          currtable['1-'+r1][0]='1-'+rvalue
          currtable.update(tables[r2])
          currtable['1-'+r2][0]='1-'+rvalue
          currtable['1-'+rvalue]=['-']*len(symbols)
          states[rvalue]=list(tables[rvalue].keys())
          table_fin['r'+str(rcount)]=currtable

        currenti=i
        rcount+=1
    star=False
    if currenti+2<len(re):
      if re[currenti+2]=='*':
        star=True
        r3=rval[e]
        e='('+e+')'+'*'
        rval[e]='r'+str(rcount)
        rvalue=rval[e]
        tables[rvalue]={}
        currtable=tables[rvalue]
        currtable['0-'+rvalue]=['-']*len(symbols)
        currtable['0-'+rvalue][0]=[states[r3][0],'1-'+rvalue]
        currtable.update(tables[r3])
        currtable[states[r3][-1]][0]=[states[r3][0],'1-'+rvalue]
        currtable['1-'+rvalue]=['-']*len(symbols)
        states[rvalue]=list(tables[rvalue].keys())
        table_fin['r'+str(rcount)]=currtable
    else:
      print('hiiii')
      exit=True
      break

      currenti=i  #currtable['1-'+rvalue][0]=[states[r3][0],'1-'+rvalue]
  re=re[re.index(')')+1:]
  if '(' not in re:
    break
for key,val in tables.items():
  print(key)
  for k,v in val.items():
    print(k+" : ",end="")
    print(v)
  print('\n\n')


#generate

 symbols=['a','b']
 re='(a|b)*(ab)'
 re='(a|b)*(ba)'
 re='(a|b)(ba)'
 strings=[]
 while len(re)>1:
  l=[]
  s=""
  for j in range(re.index('(')+1,re.index(')')):
    if re[j] in symbols:
      s+=re[j]
    else:
      if re[j]=='|':
        l.append(s)
        s=""
  if s!="":
    l.append(s)
  nexti=re.index(')')+1
  if nexti==len(re):
    strings.append(l)
    break
  if re[nexti]=='*':
    if len(l)==1:
      for i in range(2,11):
        l.append(l[0]*i)
    else:
      temp=[]
      for ch in l:
        t=[]
        for i in range(1,4):
            t.append(ch*i)
        temp.append(t)
      for i in range(len(temp)-1):
        for j in range(3):
          for k in range(3):
            l.append(temp[i][j]+temp[i+1][k])
  strings.append(l)
  re=re[nexti:]
 final=[]
 for s in strings[0]:
  final.append(s)
 for j in range(1,len(strings)):
  temp=[]
  for k in range(len(strings[j])):
    for s in final:
      s+=strings[j][k]
      temp.append(s)
  final.clear()
  final =temp
 print('the strings are ',final)


 #check dfa accepts the strings

     Q = ['q0', 'q1', 'q2']
    input_symbols =['0', '1']
    q0 = ['q0']
    F = ['q2']
    transition_table=[['q0','q0','q1'],
                      ['q1','q2','q1'],
                      ['q2','q2','q2']]
    string='0110'
    curr_state='q0'
    print("Entet input states : ")
    Q=input().split()
    print("Entet input symbols : ")
    input_symbols=input().split()
    print("Entet initial state : ")
    q0=input().split()
    print("Entet final states : ")
    F=input().split()
    transition_table=[]
    for q in Q:
      print("Enter transitions for ",q)
      trans=input().split()
      trans.insert(0,q)
      transition_table.append(trans)
    print("Enter string : ")
    string=input()
    print("Transitions : ",end=" ")
    for inp in string:
      print(curr_state,end="->")
      row=Q.index(curr_state)
      i=input_symbols.index(inp)
      curr_state=transition_table[row][i+1]
    print()
    if curr_state in F:
      print("String is accepted")
    else:
      print("String not accepted")

#NFA to DFA

from collections import deque

class State:
    def __init__(self, label, nfa_states):
        self.label = label
        self.nfa_states = nfa_states
        self.transition = {} # Key: i/p symbol. Value: List of states that can be reached
        self.is_final = False

def findEpsClosure(state):
    resList = [state]
    for toState in nfa_table[state][0]:
        if toState == -1:
            break
        resList.extend(findEpsClosure(toState))
    return resList

no_of_states = int(input('Enter no. of states: '))
alphabets = list(input('Enter space-separated alphabets: ').split())
alphabets.insert(0, 'epsilon')

nfa_table = []
print('INPUT THE NFA TABLE:-')
print('Enter space-separated TO states for each i/p symbol')
print("Enter '-1' if none")

for i in range(no_of_states):
    row = []
    print('State ', i, ':-')
    for c in alphabets:
        row.append(list(map(int,input(f"\t{c}: ").split())))
    nfa_table.append(row)

no_final_states = int(input('Enter no. of final states: '))

if no_final_states:
    final_states = list(map(int, input('Enter space-separated final states: ').split()))
else:
    final_states = []
dfa_table = [] # List of dictionaries. Elements are different states. Keys are input symbol. Values are destination state on that input symbol from that state

new_state_queue = deque()

dfa_initial_state = State('A', findEpsClosure(0))
new_state_queue.append(dfa_initial_state)
dfa_table.append(dfa_initial_state)

while new_state_queue:
    curr_state = new_state_queue.popleft()

    # Setting FINAL STATE status
    for nfa_state in curr_state.nfa_states:
        if nfa_state in final_states:
            curr_state.is_final = True
            break
    
    for i in range(1,len(alphabets)):
        T = set()
        for state in curr_state.nfa_states:
            if nfa_table[state][i] != [-1]:
                T.update(nfa_table[state][i])

        if len(T)==0:
            trapStateAlreadyPresent = False
            for dfa_state in dfa_table:
                if T == dfa_state.nfa_states:
                    trapStateAlreadyPresent = True
                    break

            if not trapStateAlreadyPresent:
                dfa_table.append(State('TRAP', T))

            curr_state.transition[alphabets[i]] = 'TRAP'    
            continue

        epsilon_closure = set()
        for state in T:
            epsilon_closure.update(findEpsClosure(state))

        existingState = False

        for dfa_state in dfa_table:
            if dfa_state.nfa_states == epsilon_closure:
                curr_state.transition[alphabets[i]] = dfa_state.label
                existingState = True
                break

        if not existingState:
            if dfa_table[-1].label == 'TRAP':
                new_label = chr (ord(dfa_table[-2].label) + 1)
            else:
                new_label = chr( ord(dfa_table[-1].label) + 1)
            new_state = State(new_label, epsilon_closure)
            new_state_queue.append(new_state)
            dfa_table.append(new_state)
            curr_state.transition[alphabets[i]] = new_label

print('Final DFA table:-\n')

print('State \t ', end='')

for i in range(1, len(alphabets)):
    print(alphabets[i], end=' \t ')
print(' Final State')

for dfa_state in dfa_table:
    print(dfa_state.label, end=' \t ')
    if dfa_state.label == 'TRAP':
        print('- \t' * (len(alphabets)-1), end='')
        print(' NO')
        continue
    for i in range(1,len(alphabets)):
        print(dfa_state.transition[alphabets[i]], end=' \t ')
    if dfa_state.is_final:
        print(' YES')
    else:
        print(' NO')

#epsilon closure
ftable=tables[list(tables.keys())[-1]].copy()
closure={}
for state in ftable:
  close=[]
  q=[state]
  value=[]
  visited=[]
  while q:
    currstate=q.pop(0)
    visited.append(currstate)
    val=ftable[currstate][0]
    if isinstance(val,list):
      for st in val:
        value.append(st)
        if st not in currstate:
          q.append(st)
    else:
      if val!='-':
        value.append(val)
        if val not in visited:
          q.append(val)
    closure[state]=value

#re to nfa
rcount=1
symbols=['e','a','b']
re='(ab)*'
states={}#key : r1,r2 ,value : states 0-r1,1-r1
rval={}#gives rval for the symbol or expression
expressions=[]
tables={}
exit=False
prevcon=""
while re!="":
  e=""
  currenti=0
  for i in range(re.index('(')+1,re.index(')')):
    currenti=i
    e+=re[i]
    if re[i] in symbols:
      if i!=re.index('(')+1:
        expressions.append(e)
      if re[i] not in states:
        rvalue='r'+str(rcount)
        states[rvalue]=[]
        states[rvalue].append('0-r'+str(rcount))
        states[rvalue].append('1-r'+str(rcount))
        tables['r'+str(rcount)]={}
        rval[re[i]]='r'+str(rcount)
        for j,s in enumerate(states[rvalue]):
          tables['r'+str(rcount)][s]=['-']*len(symbols)
          if j==0:
            tables['r'+str(rcount)][s][symbols.index(re[i])]=states[rvalue][1]
        rcount+=1
      if len(e)>=2:
        if e[-2] in symbols:
          rval[e]='r'+str(rcount)
          rvalue=rval[e]
          r1=""
          if prevcon!="":
            r1=rval[prevcon]
          else:
            r1=rval[e[-2]]
          r2=rval[re[i]]
          #print('r1=',r1)
          #print('r2=',r2)
          tables[rvalue]={}
          currtable=tables[rvalue]
          currtable.update(tables[r1])
          last=list(tables[r1].keys())[-1]
          del currtable[last]
          first=list(tables[r2].keys())[0]
          currtable.update(tables[r2])
          for key,val in currtable.items():
            if isinstance(val,list):
              if last in val:
                for i in range(len(val)):
                  if val[i]==last:
                    val[i]=first
          states[rvalue]=list(tables[rvalue].keys())
          
          print('curr',currtable)
        if '|' in e:
          prevcon=""
          print('e=',e)
          rval[e]='r'+str(rcount)
          rvalue=rval[e]
          sepIndex=''
          for index in range(len(e)-1,-1,-1):
            if e[index] not in symbols:
              sepIndex=index
              break
          #print('e = ',e)
          #print('rvalue',rvalue)
          if e[sepIndex]=='|':
            #print("JIi")
            tables[rvalue]={}
            currtable=tables[rvalue]
            #A=e[:e.index('|')]
            #B=e[e.index('|')+1:]
            A=e[:sepIndex]
            B=e[sepIndex+1:]
            r1=rval[A]
            r2=rval[B]
            currtable['0-'+rvalue]=['-']*len(symbols)
            #print("rvall ",rvalue)
            currtable['0-'+rvalue][0]=[states[r1][0],states[r2][0]]
            currtable.update(tables[r1])
            currtable['1-'+r1][0]='1-'+rvalue
            currtable.update(tables[r2])
            currtable['1-'+r2][0]='1-'+rvalue
            currtable['1-'+rvalue]=['-']*len(symbols)
            states[rvalue]=list(tables[rvalue].keys())


        currenti=i
        rcount+=1
    else:
      prevcon=""
    star=False
    if currenti+2<len(re):
      if re[currenti+2]=='*':
        star=True
        r3=rval[e]
        e='('+e+')'+'*'
        rval[e]='r'+str(rcount)
        rvalue=rval[e]
        tables[rvalue]={}
        currtable=tables[rvalue]
        currtable['0-'+rvalue]=['-']*len(symbols)
        currtable['0-'+rvalue][0]=[states[r3][0],'1-'+rvalue]
        currtable.update(tables[r3])
        currtable[states[r3][-1]][0]=[states[r3][0],'1-'+rvalue]
        currtable['1-'+rvalue]=['-']*len(symbols)
        states[rvalue]=list(tables[rvalue].keys())
    else:
      print('hiiii')
      exit=True
      break

      currenti=i  #currtable['1-'+rvalue][0]=[states[r3][0],'1-'+rvalue]
  re=re[re.index(')')+1:]
  if '(' not in re:
    break
