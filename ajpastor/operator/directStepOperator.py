
# This file was *autogenerated* from the file ./directStepOperator.sage
from sage.all_cmdline import *   # import sage library

_sage_const_1 = Integer(1); _sage_const_0 = Integer(0)

####################################################################################################
####################################################################################################
###
### DirectStepOperator module
###
### ------------------------------------------------------------------------------------------------
###
### This file contains an extension of a TwoStepsOperator that computes the kernell of the appropiate matrix using standard SAGE algorithms.
### ------------------------------------------------------------------------------------------------
###
### Version: 0.0
### Date of begining: 05-05-2017
###
### Updated (21-08-2017)
###     - Changed name parent to base
###
###
### ------------------------------------------------------------------------------------------------
### Dependencies:
###     - TwoStepsOperator class
####################################################################################################
####################################################################################################

# Local imports
from .twoStepsOperator import TwoStepsOperator;
from .operator import foo_derivative;

class DirectStepOperator(TwoStepsOperator):

    #######################################################
    ### INIT METHOD AND GETTERS
    #######################################################
    def __init__(self, base, input, derivate = foo_derivative):
        super(DirectStepOperator, self).__init__(base, input, derivate);
            
    ####################################################### 
        
    ####################################################### 
    ### SOLVING MATRICES METHOD
    ####################################################### 
    def _get_element_nullspace(self, M):
        from ajpastor.misc.bareiss import BareissAlgorithm;
        ## We take the domain where our elements will lie
        parent = M.parent().base().base();
        
        ## Computing the kernell of the matrix
        try:
            lcms = [lcm([el.denominator() for el in row]) for row in M];
            N = Matrix(parent, [[el*lcms[i] for el in M[i]] for i in range(M.nrows())]);
            ba = BareissAlgorithm(parent, N, lambda p : False);
            
            ker = ba.right_kernel_matrix();
        except Exception as e:
            print e
            ker = M.right_kernel_matrix();
        #ker = M.right_kernel_matrix();
        ## If the nullspace has hight dimension, we try to reduce the final vector computing zeros at the end
        aux = [row for row in ker];
        i = _sage_const_1 ;
        
        while(len(aux) > _sage_const_1 ):
            new = [];
            current = None;
            for j in range(len(aux)):
                if(aux[j][-(i)] == _sage_const_0 ):
                    new += [aux[j]];
                elif(current is None):
                    current = j;
                else:
                    new += [aux[current]*aux[j][-(i)] - aux[j]*aux[current][-(i)]];
                    current = j;
            aux = [el/gcd(el) for el in new];
            i = i+_sage_const_1 ;

            
        ## When exiting the loop, aux has just one vector
        sol = aux[_sage_const_0 ];
        
        ## Our solution has denominators. We clean them all
        p = prod([el.denominator() for el in sol]);
        return vector(parent, [el*p for el in sol]);
    ####################################################### 
    

