def OuterFun(args):
    print(f'Inside OuterFun({args})')
    def InnerFun(extraArgs):
        print(f'Inside InnerFun {extraArgs} : {args}')
   
    InnerFun((10, 20, args))

OuterFun(100)
