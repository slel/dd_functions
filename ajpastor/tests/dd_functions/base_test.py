r"""
Python file for a basic test

This module is not inteded to be executed. This is a basic blueprint for further test files.

EXAMPLES::
    sage: from ajpastor.tests.dd_functions.base_test import *

TODO::
    * Complete the Examples section of this documentation
    * Document the package
    * Review the functionality of the package

AUTHORS:

    - Antonio Jimenez-Pastor (2016-10-01): initial version

"""

# ****************************************************************************
#  Copyright (C) 2019 Antonio Jimenez-Pastor <ajpastor@risc.uni-linz.ac.at>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#                  https://www.gnu.org/licenses/
# ****************************************************************************

# This file was *autogenerated* from the file ./dd_functions/identities.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_10 = Integer(10); _sage_const_0 = Integer(0)
import sys, traceback;
from timeit import default_timer as timer;

from ajpastor.misc.verbose import *;
from ajpastor.dd_functions import *;


def run():
    ## Loop variables
    __MIN_N = _sage_const_2 ;
    __MAX_N = _sage_const_10 ;
    __DIFF = __MAX_N - __MIN_N;

    ## Verbose control
    __LEVEL = -_sage_const_2 ; ## Verbose level (-2 print loops, -1 print test, 0 print global data, greater print nothing
    __PREV_LEVEL = sverbose.get_level();

    ## Extra private functions
    #def assert_initial(func, symbolic, size, name):
    #    for i in range(size):
    #        func_val = func.getInitialValue(i);
    #        real_val = symbolic.derivative(i)(x=_sage_const_0 );
    #        assert (func_val == real_val), "Error in the %d initial value of the function %s: expected %s but got %s"%(i,name,real_val,func_val);
            
    #def random_polynomial(min=-_sage_const_10 ,max=_sage_const_10 ,degree=_sage_const_3 ):
    #    R = PolynomialRing(QQ,x);
    #    p = R(_sage_const_1 );
    #    while(p.degree() == _sage_const_0 ):
    #        p = R([randint(min,max) for i in range(degree+_sage_const_1 )])
    #    
    #    return p;

    ####################################################################################
    ## Setting up the tests
    sverbose.set_level(__LEVEL);
    __deep_wrap = sverbose.get_deep_wrapper();
    sverbose.set_deep_wrapper(-__LEVEL);
    sverbose("Running tests over identities of DDFunctions"); ## HEAD LINE
    sverbose("");
    sverbose("Author: Antonio Jimenez-Pastor"); ## AUTHOR LINE
    sverbose("Date: 27-09-2018"); ## DATE LINE
    sverbose("");
    sverbose.increase_depth();
              

    ##Starting execution
    t = timer();
    #########################################
    ### TESTS FOR STRUCTURES DDRing and DDFunction
    #########################################
    try:
        ## How to Start a section
        #sverbose("Checking trigonometric equalities");
        #sverbose.increase_depth();
        # ...
        #sverbose.decrease_depth();
        
        ## How to test an identity
        #sverbose("sin^2(x)+cos^2(x) = 1");
        #assert Sin(x)**_sage_const_2 +Cos(x)**_sage_const_2  == _sage_const_1 , "Error with sin^2(x)+cos^2(x) = 1";
        
        ## How to test a loop
        #sverbose("Testing pushouts for parameters with D(QQ[x])");
        #sverbose.increase_depth();
        #sverbose.start_iteration(_sage_const_9 , True, True);
        # ... code with 'sverbose.next_iteration();'
        #sverbose.decrease_depth();
        #sverbose("Finished tests");
        
        
    except (Exception, KeyboardInterrupt) as e:
        sverbose.reset_depth();
        sverbose.set_level(__PREV_LEVEL);
        print("Error found during tests: %s" %(e));
        raise e;
        
    sverbose.decrease_depth();
    sverbose("Finished all the tests on the examples");
    t = timer() - t;
    sverbose("Example tests finished successfully --> %s" %(t));
    sverbose.set_deep_wrapper(__deep_wrap);
    sverbose.set_level(__PREV_LEVEL);


