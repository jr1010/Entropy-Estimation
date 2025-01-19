import numpy as np


def compute_von_neuman_from_memory(bit_results, error_correction=False, error_rates=None):
    s = []
    k = 0
    counts = {'0'*(4-len(bin(i)[2:]))+bin(i)[2:]:0 for i in range(16)}
    
    for idx, bit in enumerate(bit_results):
        # if (idx+1)%10000 == 0:
        #     print(f'Shots : {idx+1}  ', end='\r')
        counts[bit.replace(" ", "")] += 1
        if error_correction:
            cnt_new = error_mitigation(counts, error_rates, shots=(idx+1))
            k = max(min(cnt_new['0011'] + cnt_new['1001'], 1), 0)
            s += [von_neumann_S_from_k(k)]
        else:
            if bit in ['0011', '1001', '1 0 0 1', '0 0 1 1']:
                k += 1       
            s += [(von_neumann_S_from_k(k/(idx+1)))]

    return s

                     
def entropy(p):
    if p==0 or p==1:
        return 0
    else:
        return -p*np.log2(p) -(1-p)*np.log2(1-p)


def von_neumann_S_from_k(k):
    if k>0.25:
        return 1
    if k<0:
        return 0
        
    t = np.sqrt(1-4*k)
    l1 = 0.5*(1+t)
    return entropy(l1)


def post_process_ibmq(pub_result):
    measurement = dict()
    memory_register = list()
    for key in pub_result.data.keys():
        memory_register += [pub_result.data[key].get_bitstrings()]

    memory_pr = list()
    for idx in range(len(memory_register[0])):
        string = ''
        for reg in memory_register[::-1]:
            string += reg[idx]
        memory_pr.append(string)    

    return memory_pr


def estimate_bounds_from_memory(memory, error_prob):
    probs = np.ones(len(memory))
    n = np.array(range(1, len(memory)+1))
    k = 0
    
    for idx, el in enumerate(memory):
        if el in ['1 0 0 1', '1001', '0011', '0 0 1 1']:
            k += 1
        probs[idx] = k/(idx+1)

    bound = np.sqrt(np.log(2/error_prob)/(2*n))
    ucb = probs + bound
    lcb = probs - bound

    return ucb, lcb


def generate_random_state(n):
    random_states = np.random.uniform(0, 1, size=(n, 6)) + 1j*np.random.uniform(0, 1, size=(n, 6))
    random_states = random_states/np.linalg.norm(random_states, axis=1).reshape(-1, 1)
    return random_states


def von_neumann_entropy(eigvals, dim=2):
    res = 0
    for eig in eigvals:
        if eig == 0:
            continue
        res += eig*np.log2(1/eig)

    return np.round(res, 3)


def partial_traces(state, dimA, dimB, density_matrix=False):
    if not density_matrix:
        st = state.reshape(-1, 1)
        density_m = st@np.conj(st.T)
    else:
        density_m = state.copy()
    
    density_A = np.zeros((dimA, dimA)).astype(np.complex128)
    density_B = np.zeros((dimB, dimB)).astype(np.complex128)

    for row in range(dimA):
        for col in range(dimA):
            density_A[row, col] = np.sum([density_m[dimB*row + i, dimB*col + i] for i in range(dimB)]) 

    for row in range(dimB):
        for col in range(dimB):
            density_B[row, col] = np.sum([density_m[row + i*dimB, col + i*dimB] for i in range(dimA)])

    return (density_A/np.linalg.trace(density_A), density_B/np.linalg.trace(density_B)) 

def tensor_prodcut(state):
    n = len(state)
    res = np.zeros(n*n).astype(np.complex128)

    for idx, el in enumerate(state):
        res[n*idx: n*(idx+1)] = el*state

    return res
    

def tensor(rhoA, rhoB):
    n = rhoA.shape[0]
    m = rhoB.shape[0]

    res = np.zeros((n*m, n*m)).astype(np.complex128)

    for i in range(n):
        for j in range(n):
            res[i*m:(i+1)*m, j*m:(j+1)*m] = rhoA[i, j]*rhoB

    return res


def von_neumann_entropy_from_state(state, dimA, dimB):
    pa, pb = partial_traces(state, dimA, dimB)
    eigs = np.linalg.eigvalsh(pa)
    return von_neumann_entropy(eigs, dim=2)
    