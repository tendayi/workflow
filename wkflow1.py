import workflow

def Workflow1(object):
    def __init__(self):
        self.state = {}

    def execute(self):
        def step1(data): pass
        def step2(data): pass
        def step3(data): pass
        def step4(data): pass
        def step5(data): pass
        
        # need this as a workflow can end in a number of ways
        def end(): raise StopIteration()

        self.steps = {1: step1, 2: step2, 3: step3, 4: step4, 5: step5, -1: end}

        workflow.start(self)

        return self.state(RESULT)
