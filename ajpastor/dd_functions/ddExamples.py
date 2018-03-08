
# This file was *autogenerated* from the file ./ddExamples.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_6 = Integer(6)
from ajpastor.dd_functions.ddFunction import *;

from ajpastor.misc.dinamic_string import *;
#from ajpastor.dd_functions.ddParametrizedFunction import *;

## Global variables (PUBLIC)
DFinite_examples = {};
DDFinite_examples = {};

## Global variables (PRIVATE)
__example_names = {};

##################################################################################
##################################################################################
###
### Predefined examples
###
##################################################################################
##################################################################################
def DD_EXAMPLES_LOAD():
    global DFinite_examples; global DDFinite_examples;
    global __example_names;

    s = DFinite.element([_sage_const_1 ,_sage_const_0 ,_sage_const_1 ],[_sage_const_0 ,_sage_const_1 ], name=DinamicString("sin(_1)", "x"));
    c = DFinite.element([_sage_const_1 ,_sage_const_0 ,_sage_const_1 ],[_sage_const_1 ,_sage_const_0 ], name=DinamicString("cos(_1)", "x"));
    sh = DFinite.element([-_sage_const_1 ,_sage_const_0 ,_sage_const_1 ],[_sage_const_0 ,_sage_const_1 ], name=DinamicString("sinh(_1)", "x"));
    ch = DFinite.element([-_sage_const_1 ,_sage_const_0 ,_sage_const_1 ],[_sage_const_1 ,_sage_const_0 ], name=DinamicString("cosh(_1)", "x"));
    ln = DFinite.element([_sage_const_1 ,_sage_const_0 ,(x+_sage_const_1 )],[_sage_const_0 ,_sage_const_1 ], name=DinamicString("log(_1-1)", "x"));
    e = DFinite.element([-_sage_const_1 ,_sage_const_1 ],[_sage_const_1 ], name=DinamicString("exp(_1)", "x"));
    tan = DDFinite.element([-_sage_const_2 ,_sage_const_0 ,c**_sage_const_2 ],[_sage_const_0 ,_sage_const_1 ], name=DinamicString("tan(_1)", "x"));
    
    ## Defining D-Finite Examples
    DFinite_examples['e'] = e;
    DFinite_examples['ln'] = ln;
    DFinite_examples['sin'] = s;
    DFinite_examples['cos'] = c;
    DFinite_examples['sinh'] = sh;
    DFinite_examples['cosh'] = ch;
    P = DFiniteP.parameters()[_sage_const_0 ];
    DFinite_examples['bessel'] = DFiniteP.element([x**_sage_const_2 -P**_sage_const_2 ,x,x**_sage_const_2 ], name=DinamicString("bessel_J(_1,_2)", ["P","x"]));
    DFinite_examples['legendre'] = DFiniteP.element([P*(P+_sage_const_1 ), -_sage_const_2 *x,_sage_const_1 -x**_sage_const_2 ], name=DinamicString("legendre_P(_1,_2)", ["P","x"]));
    DFinite_examples['chebyshev1'] = DFiniteP.element([P**_sage_const_2 ,-x,(_sage_const_1 -x**_sage_const_2 )], name=DinamicString("chebyshev_T(_1,_2)", ["P","x"]));
    DFinite_examples['chebyshev2'] = DFiniteP.element([P*(P+_sage_const_2 ),-_sage_const_3 *x,_sage_const_1 -x**_sage_const_2 ], name=DinamicString("chebyshev_U(_1,_2)", ["P","x"]));
    
    ## Defining DD-Finite Examples
    DDFinite_examples['esin'] = DDFinite.element([_sage_const_1 ,-c], [_sage_const_1 ], name=DinamicString("exp(sin(_1))", "x"));
    DDFinite_examples['sine'] = DDFinite.element([e**_sage_const_2 ,-_sage_const_1 ,_sage_const_1 ],[_sage_const_0 ,_sage_const_1 ], name=DinamicString("sin(exp(_1))", "x"));
    DDFinite_examples['tan'] = [tan, DDFinite.element([_sage_const_0 ,-_sage_const_2 *s*c,c**_sage_const_2 ], [_sage_const_0 ,_sage_const_1 ], name=DinamicString("tan(_1)", "x"))];
    DDFinite_examples['bernoulli'] = DDFinite.element([x*e-e+_sage_const_1 ,x*(e-_sage_const_1 )],[_sage_const_1 ,-_sage_const_1 /_sage_const_2 ,_sage_const_1 /_sage_const_6 ,_sage_const_0 ]);
    
    ## Defining some names
    __example_names['exp'] = 'e';
    __example_names['log'] = 'ln';
    __example_names['sen'] = 'sin';
    __example_names['tg'] = 'tan';

def DFinite_example(input, n=_sage_const_0 ):
    if(DFinite_examples.has_key(input)):
        res = DFinite_examples[input];
    elif (__example_names.has_key(input) and DFinite_examples.has_key(__example_names[input])):
        res = DFinite_examples[__example_names[input]];
    else:
        raise ValueError('The DD-Function by name %s does not exist' %(input));
        
    if(type(res)==list):
        return res[n];
    else:
        return res;
    

def DDFinite_example(input, n = _sage_const_0 ):
    if(DDFinite_examples.has_key(input)):
        res = DDFinite_examples[input];
    elif (__example_names.has_key(input) and DDFinite_examples.has_key(__example_names[input])):
        res = DDFinite_examples[__example_names[input]];
    else:
        raise ValueError('The DD-Function by name %s does not exist' %(input));
        
    if(type(res)==list):
        return res[n];
    else:
        return res;
    
def DDFunction_example(input, n=_sage_const_0 ):
    try:
        return DFinite_example(input, n);
    except Exception:
        pass;
    try:
        return DDFinite_example(input, n);
    except Exception:
        pass;
        
    raise ValueError('No DD-Function by name %s exist' %(input));

##################################################################################
##################################################################################
###
### Trigonometric and Hyperbolic trigonometric Functions
###
##################################################################################
##################################################################################
@cached_function
def Sin(input, ddR = None):
    from ajpastor.dd_functions.ddFunction import DDFunction;
    if(isinstance(input, DDFunction)):
        return Sin(x)(input);
    f,dR = __decide_parent(input, ddR);
    
    evaluate = lambda p : dR.getSequenceElement(p,_sage_const_0 );
    if(evaluate(f) != _sage_const_0 ):
        raise ValueError("Impossible to compute sin(f) with f(0) != 0");
    
    df = dR.base_derivation(f);
    df2 = dR.base_derivation(df);
    
    newName = repr(f);
    if(hasattr(f, "_DDFunction__name") and (not(f._DDFunction__name is None))):
        newName = f._DDFunction__name;
    
    return dR.element([df**_sage_const_3 ,-df2,df],[_sage_const_0 ,evaluate(df),evaluate(df2)], name=DinamicString("sin(_1)", newName)); 

@cached_function    
def Cos(input, ddR = None):
    from ajpastor.dd_functions.ddFunction import DDFunction;
    if(isinstance(input, DDFunction)):
        return Cos(x)(input);
    f,dR = __decide_parent(input, ddR);
    
    evaluate = lambda p : dR.getSequenceElement(p,_sage_const_0 );
    if(evaluate(f) != _sage_const_0 ):
        raise ValueError("Impossible to compute cos(f) with f(0) != 0");
    
    df = dR.base_derivation(f);
    df2 = dR.base_derivation(df);
    
    newName = repr(f);
    if(hasattr(f, "_DDFunction__name") and (not(f._DDFunction__name is None))):
        newName = f._DDFunction__name;
    
    return dR.element([df**_sage_const_3 ,-df2,df],[_sage_const_1 ,_sage_const_0 ,-evaluate(df)**_sage_const_2 ], name=DinamicString("cos(_1)",newName)); 

@cached_function
def Tan(input, ddR = None):
    from ajpastor.dd_functions.ddFunction import DDFunction;
    if(isinstance(input, DDFunction)):
        return Tan(x)(input);
    if(input == x):
        return DDFinite_example('tan');
    g, dR = __decide_parent(input, ddR,_sage_const_2 );
    
    
    evaluate = lambda p : dR.getSequenceElement(p,_sage_const_0 );
    if(evaluate(g) != _sage_const_0 ):
        raise ValueError("Impossible to compute tan(f) with f(0) != 0");
    
    dg = dR.base_derivation(g); ddg = dR.base_derivation(dg);
    a = Cos(input)**_sage_const_2 ; b = dR.base().zero(); c = dR.base()(-_sage_const_2 );
    
    ### First we compute the new linear differential operator
    newOperator = dR.element([dg**_sage_const_3 *c,dg**_sage_const_2 *b-ddg*a,dg*a]).equation;
        
    ### Now, we compute the initial values required
    required = newOperator.get_jp_fo()+_sage_const_1 ;
        
    init_tan = Tan(x).getInitialValueList(required);
    init_input = [factorial(i)*dR.base().getSequenceElement(g,i) for i in range(required)];
        
    newInit = [init_tan[_sage_const_0 ]]+[sum([init_tan[j]*bell_polynomial(i,j)(*init_input[_sage_const_1 :i-j+_sage_const_2 ]) for j in range(_sage_const_1 ,i+_sage_const_1 )]) for i in range(_sage_const_1 ,required)]; ## See Faa di Bruno's formula
    
    result = dR.element(newOperator,newInit);
    
    newName = repr(input);
    if(hasattr(input, "_DDFunction__name") and (not(input._DDFunction__name is None))):
        newName = input._DDFunction__name;
    
    result._DDFunction__name = DinamicString("tan(_1)",newName);
    return result;

@cached_function    
def Sinh(input, ddR = None):
    from ajpastor.dd_functions.ddFunction import DDFunction;
    if(isinstance(input, DDFunction)):
        return Sinh(x)(input);
    f,dR = __decide_parent(input, ddR);
    
    evaluate = lambda p : dR.getSequenceElement(p,_sage_const_0 );
    if(evaluate(f) != _sage_const_0 ):
        raise ValueError("Impossible to compute sin(f) with f(0) != 0");
    
    df = dR.base_derivation(f);
    df2 = dR.base_derivation(df);
    
    newName = repr(f);
    if(hasattr(f, "_DDFunction__name") and (not(f._DDFunction__name is None))):
        newName = f._DDFunction__name;
    
    return dR.element([-df**_sage_const_3 ,-df2,df],[_sage_const_0 ,evaluate(df),evaluate(df2)], name=DinamicString("sinh(_1)",newName)); 

@cached_function    
def Cosh(input, ddR = None):
    from ajpastor.dd_functions.ddFunction import DDFunction;
    if(isinstance(input, DDFunction)):
        return Cosh(x)(input);
    f,dR = __decide_parent(input, ddR);
    
    evaluate = lambda p : dR.getSequenceElement(p,_sage_const_0 );
    if(evaluate(f) != _sage_const_0 ):
        raise ValueError("Impossible to compute cos(f) with f(0) != 0");
    
    df = dR.base_derivation(f);
    df2 = dR.base_derivation(df);
    
    newName = repr(f);
    if(hasattr(f, "_DDFunction__name") and (not(f._DDFunction__name is None))):
        newName = f._DDFunction__name;
    
    return dR.element([-df**_sage_const_3 ,-df2,df],[_sage_const_1 ,_sage_const_0 ,evaluate(df)**_sage_const_2 ], name=DinamicString("cosh(_1)", newName)); 

##################################################################################
##################################################################################
###
### Exponential and Logarithm Functions
###
##################################################################################
##################################################################################   
@cached_function  
def Log(input, ddR = None):
    from ajpastor.dd_functions.ddFunction import DDFunction;
    if(isinstance(input, DDFunction)):
        return Log(x+_sage_const_1 )(input);
    f,dR = __decide_parent(input, ddR);
    
    evaluate = lambda p : dR.getSequenceElement(p,_sage_const_0 );
    if(evaluate(f) != _sage_const_1 ):
        raise ValueError("Impossible to compute ln(f) with f(0) != 1");
    
    df = dR.base_derivation(f);
    df2 = dR.base_derivation(df);
    
    newName = repr(f);
    if(hasattr(f, "_DDFunction__name") and (not(f._DDFunction__name is None))):
        newName = f._DDFunction__name;
    
    return dR.element([_sage_const_0 ,df**_sage_const_2 -df2*f,df*f],[_sage_const_0 ,evaluate(df), evaluate(df2)-evaluate(df)**_sage_const_2 ], name=DinamicString("log(_1)",newName));
    
@cached_function 
def Log1(input, ddR = None):
    from ajpastor.dd_functions.ddFunction import DDFunction;
    if(isinstance(input, DDFunction)):
        return Log1(x)(input);
    f,dR = __decide_parent(input, ddR);
    
    evaluate = lambda p : dR.getSequenceElement(p,_sage_const_0 );
    if(evaluate(f) != _sage_const_0 ):
        raise ValueError("Impossible to compute cos(f) with f(0) != 0");
    
    df = dR.base_derivation(f);
    df2 = dR.base_derivation(df);
    
    f1 = f+_sage_const_1 ;
    
    newName = repr(f);
    if(hasattr(f, "_DDFunction__name") and (not(f._DDFunction__name is None))):
        newName = f._DDFunction__name;
    
    return dR.element([_sage_const_0 ,df**_sage_const_2 -df2*f1,df*f1],[_sage_const_0 ,evaluate(df), evaluate(df2)-evaluate(df)**_sage_const_2 ], name=DinamicString("log(_1+1)", newName)); 
    
@cached_function 
def Exp(input, ddR = None):
    from ajpastor.dd_functions.ddFunction import DDFunction;
    if(isinstance(input, DDFunction)):
        return Exp(x)(input);
    f,dR = __decide_parent(input, ddR);
    
    evaluate = lambda p : dR.getSequenceElement(p,_sage_const_0 );
    if(evaluate(f) != _sage_const_0 ):
        raise ValueError("Impossible to compute exp(f) with f(0) != 0");
    
    newName = repr(f);
    if(hasattr(f, "_DDFunction__name") and (not(f._DDFunction__name is None))):
        newName = f._DDFunction__name;
        
    return dR.element([-dR.base_derivation(f),_sage_const_1 ],[_sage_const_1 ], name=DinamicString("exp(_1)", newName));

##################################################################################
##################################################################################
###
### Special Functions
###
##################################################################################
##################################################################################    
### Bessel Functions
@cached_function 
def BesselD(input, kind = _sage_const_1 ):
    if(input is None):
        return DDFunction_example('bessel');
    elif(kind == _sage_const_1 ):
        try:
            alpha = QQ(input);
            if(alpha < _sage_const_0 ):
                raise ValueError("Impossible to manage Bessel functions of first kind with negative order");
                
            P = DFiniteP.parameters()[_sage_const_0 ];
            
            func = DDFunction_example('bessel')(**{str(P):alpha});
            if(alpha in ZZ):
                return func.change_init_values([_sage_const_0  for i in range(alpha)] + [_sage_const_1 /_sage_const_2 **alpha, _sage_const_0 , -((alpha+_sage_const_2 )/(_sage_const_2 **(alpha+_sage_const_2 )))], name = "bessel_J(%d,x)" %input);
            else:
                return func.change_init_values([_sage_const_0 ], name = DinamicString("bessel_J(_1,_2)", [str(input), "x"]));
        except TypeError:
            raise TypeError("Impossible to manage Bessel functions of first kind with irrational order");
    else:
        raise ValueError("Impossible to manage Bessel functions of %dth kind" %(kind));

### Legendre Polynomials     
__legendre_initials = [[_sage_const_1 ,_sage_const_0 ],[_sage_const_0 ,_sage_const_1 ]];   
@cached_function 
def LegendreD(input):
    global __legendre_initials;
    if(input is None):
        return DDFunction_example('legendre');

    try:
        n = ZZ(input);
        if(n < _sage_const_0 ):
            raise ValueError("Impossible to create a Legendre polynomial of negative index");
            
        P = DFiniteP.parameters()[_sage_const_0 ];  
        func = DDFunction_example('legendre')(**{str(P):n});
        for i in range(len(__legendre_initials), n+_sage_const_1 ):
            prev = __legendre_initials[-_sage_const_1 ];
            prev2 = __legendre_initials[-_sage_const_2 ];
            __legendre_initials += [[-(i-_sage_const_1 )*prev2[_sage_const_0 ]/i,((_sage_const_2 *i-_sage_const_1 )*prev[_sage_const_0 ] - (i-_sage_const_1 )*prev2[_sage_const_1 ])/i]];
        return func.change_init_values(__legendre_initials[n], name=DinamicString("legendre_P(_1,_2)", [str(input), "x"]));
    except TypeError as e:
        #raise TypeError("Impossible to create a Legendre polynomial of rational index");
        raise e;

### Chebyshev Polynomials        
__chebyshev_initials = [[],[[_sage_const_1 ,_sage_const_0 ],[_sage_const_0 ,_sage_const_1 ]],[[_sage_const_1 ,_sage_const_0 ],[_sage_const_0 ,_sage_const_2 ]]];
@cached_function    
def ChebyshevD(input, kind = _sage_const_1 ):
    global __chebyshev_initials;
    if(input is None):
        return DDFunction_example('chebyshev%d' %kind);

    try:
        n = ZZ(input);
        if(n < _sage_const_0 ):
            raise ValueError("Impossible to create a Legendre polynomial of negative index");
            
        P = DFiniteP.parameters()[_sage_const_0 ];
        ## Building the differential equation
        name = None;
        if(kind == _sage_const_1 ):
            func = DDFunction_example('chebyshev1')(**{str(P):n});
            name = DinamicString("chebyshev_T(_1,_2)", [str(input), "x"]);
        elif(kind == _sage_const_2 ):
            func = DDFunction_example('chebyshev2')(**{str(P):n});
            name = DinamicString("chebyshev_U(_1,_2)", [str(input), "x"]);
        else:
            raise ValueError("Impossible to manage Chebyshev polynomial of %d-th kind" %(kind));
            
        ## Computing initial values
        for i in range(len(__chebyshev_initials[kind]), n+_sage_const_1 ):
            prev = __chebyshev_initials[kind][-_sage_const_1 ];
            prev2 = __chebyshev_initials[kind][-_sage_const_2 ];
            __chebyshev_initials[kind] += [[-prev2[_sage_const_0 ], _sage_const_2 *prev[_sage_const_0 ]-prev2[_sage_const_1 ]]];
        return func.change_init_values(__chebyshev_initials[kind][n],name);
    except TypeError as e:
        raise e;    

### Hypergeometric Functions
__CACHED_HYPERGEOMETRIC = {};

def HypergeometricFunction(a,b,c, init = _sage_const_1 ):
    return GenericHypergeometricFunction([a,b],[c],init);

def GenericHypergeometricFunction(num=[],den=[],init=_sage_const_1 ):
    if (not (isinstance(num,list) or isinstance(num,set) or isinstance(num,tuple))):
        num = [num];
    else:
        num = list(num);
    if (not (isinstance(den,list) or isinstance(den,set) or isinstance(den,tuple))):
        den = [den];
    else:
        den = list(den);
        
    ## Cleaning repeated values 
    i = _sage_const_0 ;
    while(i < len(num) and len(den) > _sage_const_0 ):
        if(num[i] in den):
            den.remove(num[i]);
            num.remove(num[i]);
        else:
            i += _sage_const_1 ;
    
    ## Sort list for cannonical input
    num.sort(); den.sort();
    
    ## Casting to tuples to have hash  
    num = tuple(num); den = tuple(den);
    
    ## Checking the function is cached
    global __CACHED_HYPERGEOMETRIC;
    if(not((num,den,init) in __CACHED_HYPERGEOMETRIC)):
        ## Building differential operator
        get_op = lambda p : DFinite.element(p).equation;
        op_num = x*prod(get_op([el,x]) for el in num);
        op_den = x*get_op([_sage_const_0 ,_sage_const_1 ])*prod(get_op([el-_sage_const_1 ,x]) for el in den);
        op = op_num - op_den;
        
        f = DFinite.element(op);
        
        initVals = [init];
        
        if(init == _sage_const_1 ):
            __CACHED_HYPERGEOMETRIC[(num,den,init)] = f.change_init_values([_sage_const_1 ],name=DinamicString("hypergeometric(_1,_2,_3)", [str(num),str(den),"x"]));
        else:
            __CACHED_HYPERGEOMETRIC[(num,den,init)] = f.change_init_values([init],name=DinamicString("%d*(hypergeometric(_1,_2,_3))", [str(num),str(den),"x"]));
        
    ## Return the cached element
    return __CACHED_HYPERGEOMETRIC[(num,den,init)];
    
### Mathieu's Functions
@cached_function
def MathieuD(a=None,q=None,init=()):
    params =[];
    if(a is None):
        params += ['a'];
    if(q is None):
        params += ['q'];
    
    destiny_ring = DDFinite; ra = a; rq = q;
    if(len(params) > _sage_const_0 ):
        destiny_ring = ParametrizedDDRing(DDFinite, params);
        if(len(params) == _sage_const_2 ):
            ra,rq = destiny_ring.parameters();
        elif('a' in params):
            ra = destiny_ring.parameters()[_sage_const_0 ]; rq = q;
        else:
            rq = destiny_ring.parameters()[_sage_const_0 ]; ra = a;
        
    return destiny_ring.element([ra-_sage_const_2 *rq*Cos(_sage_const_2 *x), _sage_const_0 , _sage_const_1 ], init, name=DinamicString("Mathieu(_1,_2;_3)(_4)", [repr(ra),repr(rq),str(list(init[:_sage_const_2 ])),"x"]));

@cached_function
def MathieuSin(a=None,q=None):
    return MathieuD(a,q,(_sage_const_0 ,_sage_const_1 ));
    
@cached_function
def MathieuCos(a=None,q=None):
    return MathieuD(a,q,(_sage_const_1 ,_sage_const_0 ));
    
##################################################################################
##################################################################################
###
### Particular differential Equations
###
##################################################################################
##################################################################################  
### Federschwinger // Swing with mass
## f'' + 2a f' + b^2f = ksin(cx)
@cached_function
def Federschwinger(a,b,c,k,init=(_sage_const_0 ,_sage_const_0 )):
    return DDFinite.element([b**_sage_const_2 ,_sage_const_2 *a,_sage_const_1 ], init, k*Sin(c*x));
    
##################################################################################
##################################################################################
###
### Private methods
###
##################################################################################
##################################################################################    
def __decide_parent(input, parent = None, depth = _sage_const_1 ):
    if(parent is None):
        R = input.parent();
        if(isinstance(R, sage.symbolic.ring.SymbolicRing)):
            parameters = set([str(el) for el in input.variables()])-set(['x']);
            if(len(parameters) > _sage_const_0 ):
                parent = ParametrizedDDRing(DDRing(DFinite, depth=depth), parameters);
            else:
                parent = DDRing(PolynomialRing(QQ,x), depth=depth);
        else:
            try:
                parent = DDRing(R, depth = depth);
            except Exception:
                raise TypeError("The object provided is not in a valid Parent");
    
    return parent.base()(input), parent;
    
#### Usual running after defining everything
DD_EXAMPLES_LOAD();

