from RefRed.calculations.run_sequence_breaker import RunSequenceBreaker

class UpdateReductionTable(object):
    
    def __init__(self, parent=None, runs=None, row=0, col=1, clear_cell=False):
        self.parent= parent
        self.row = row
        self.col = col
        
        if clear_cell:
            self.clear_cell()
            return
        
        self.raw_runs = str(runs)
        run_breaker = RunSequenceBreaker(run_sequence=self.raw_runs)
        list_run = run_breaker.final_list
    
    def clear_cell(self):
        print('in clear cell')
        
    