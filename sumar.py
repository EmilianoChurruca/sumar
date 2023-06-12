from sys import stdin, argv
from automata.tm.dtm import DTM
from automata.base.exceptions import AutomatonException

"""
L = { a^n b^m c^(n+m) / w pertenece Sigma* con Sigma = { a, b, c }
"""
las_transiciones={
    'q0': {
        'a': ('q1', 'x', 'R'),  
        'b': ('q2', 'y', 'R'),  
    },
    'q1': {
        'a': ('q1', 'a', 'R'),  
        'b': ('q2', 'b', 'R'),  
    },
    'q2': {
        'b': ('q2', 'b', 'R'), 
        'z': ('q2', 'z', 'R'),
        'c': ('q3', 'z', 'R')   
    },
    'q3': {
        'c': ('q4', 'c', 'L'),  
        '~': ('q5', '~', 'L') 
    },
    'q4': {
        'a': ('q4', 'a', 'L'),
        'b': ('q4', 'b', 'L'),
        'c': ('q4', 'c', 'L'),
        'z': ('q4', 'z', 'L'),
        'x': ('q0', 'x', 'R'), 
        'y': ('q0', 'y', 'R')   
    },
    'q5': {
        'z': ('q5', 'z', 'L'),  
        'y': ('q6', 'y', 'L')  
    },
    'q6': {
        'y': ('q6', 'y', 'L'),
        'x': ('q7', 'x', 'L'),  
    },
    'q7': {
        'x': ('q7', 'x', 'L'),
        '~': ('qacc', '~', 'R')
    }
}

maquina = DTM(
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6','q7', 'qacc'},
    input_symbols={'a','b','c'},
    tape_symbols={'a','b','c', 'x', 'y','z', '~'},
    transitions=las_transiciones,
    initial_state='q0',
    final_states={'qacc'},
    blank_symbol='~'
)

def evaluar(w, debug=False):
    if debug:
        for c in maquina.read_input_stepwise(w):
            c.print()
        return True
    return maquina.accepts_input(w)


if __name__ == '__main__':
    for w in stdin:
        res = False
        try:
            res = evaluar(w.strip(), '--debug' in argv) # strip saca el enter del final
        except AutomatonException as ex:
            print(ex.args)
        if (res):
            print('ACEPTA')
        else:
            print('RECHAZA')