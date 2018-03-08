
# This file was *autogenerated* from the file ./conversion.sage
from sage.all_cmdline import *   # import sage library

_sage_const_1 = Integer(1); _sage_const_0 = Integer(0)
from sage.rings.polynomial.polynomial_ring import is_PolynomialRing as isUniPolynomial;
from sage.rings.polynomial.multi_polynomial_ring import is_MPolynomialRing as isMPolynomial;

class ConversionSystem(object):
    ## Main bulder
    def __init__(self, base):
        '''
            Builder for a Conversion system.
            
            Take the following input:
                - `base`: a ring (checked or raise a TypeError)
        '''
        
        ## Starting the method
        if(not base in IntegralDomains()):
            raise TypeError("Imposible to build a conversion systom from something that is not a Ring");
    
        ## Initializing variables
        self.__base = base;
        
        self.__relations = None;
        self.__rel_ideal = None;
            
    ## Public getters
    def base(self):
        return self.__base;
        
    def is_polynomial(self):
        '''
            Returns a Boolean value that show if there are variables in this conversion system.
        '''
        return (isUniPolynomial(self.poly_ring()) or isMPolynomial(self.poly_ring()));
        
    def poly_ring(self):
        '''
            Returns the polynomial ring where the conversion system works.
        '''
        raise NotImplementedError("Abstract method not implemented 'poly_ring()'");
        
    def poly_field(self):
        '''
            Returns the polynomial fraction field where the conversion system works.
        '''
        raise NotImplementedError("Abstract method not implemented 'poly_field()'");
                
    def map_of_vars(self):
        '''
            Returns a Python dictionary which maps the variables of `self.poly_ring()` to the real elements of `self.base()`
        '''
        raise NotImplementedError("Abstract method not implemented 'map_of_vars()'");
        
    ## Pulbic methods
    def add_relations(self, *relations):
        if(self.is_polynomial()):
            try:
                ## Adding the new relations
                self._relations(); # We make sure the relations are initialized
                    
                self.__add_relation(relations);
                    
                ## Changing the ideal and computing a groebner basis
                if(len(self.__relations) >= _sage_const_1 ):
                    self.__rel_ideal = ideal(self.poly_ring(), self.__relations);
                    self.__relations = self.__rel_ideal.groebner_basis();
            except TypeError as e:
                raise e;
    
    def clean_relations(self):
        self.__relations = [];
                
    def to_poly(self, element):
        '''
            This method cast an element in `self.base()` or `self.base().fraction_field()` to a polynomial in the conversion system. This method can receive different types on elments. 
            
            The types allowed for the argument poly are:
                - Elements in `self.base()`
                - Elements in `self.base().fraction_field()`
                - List, Sets or Tuples
                - Matrices with polynomials recognized
                - Vectors with polynomials recognized
                
            Returns an element in `self.poly_ring()` or `self.poly_field()`.
            
            If the type is not valid, a TypeError exception will be risen. 
            If it is not possible to cast the element, a ValueError exception will be risen.
        '''
        if(element in self.base()):
            return self._to_poly_element(element);
        elif(element in self.base().fraction_field()):
            n = self.to_poly(element.numerator());
            d = self.to_poly(element.denominator());
            return self.poly_field()(n/d);
        elif(isinstance(element, sage.matrix.matrix.Matrix)):
            R = self.poly_ring();
            if(element.parent().base().is_field()):
                R = self.poly_field();
            return Matrix(R, [self.to_poly(row) for row in element]);
        elif(isinstance(element, sage.modules.free_module_element.FreeModuleElement)):
            R = self.poly_ring();
            if(element.parent().base().is_field()):
                R = self.poly_field();
            return vector(R, [self.to_poly(el) for el in element]);
        elif(isinstance(element, list)):
            return [self.to_poly(el) for el in element];
        elif(isinstance(element, set)):
            return set([self.to_poly(el) for el in element]);
        elif(isinstance(relation, tuple)):
            return tuple([self.to_poly(el) for el in element]);
        else:
            raise TypeError("Wrong type: Impossible to get polynomial value of element (%s)" %(element));
        
    def to_real(self, poly):
        '''
            This method cast a polynomial recognized in the conversion system to a real element in `self.base()`. This method can receive different types on elments. 
            
            The types allowed for the argument poly are:
                - Elements in `self.poly_ring()`
                - Elements in `self.poly_field()`
                - List, Sets or Tuples
                - Matrices with polynomials recognized
                - Vectors with polynomials recognized
                
            Returns an element in `self.base()` or `self.base().fraction_field()`.
            
            If the type is not valid, a TypeError exception will be risen.
        '''
        if(poly in self.poly_ring()):
            if(not self.is_polynomial()):
                return self.base()(poly);
            return self._to_real_element(self.poly_ring()(poly));
        elif(poly in self.poly_field()):
            n = self.to_real(poly.numerator());
            d = self.to_real(poly.denominator());
            return n/d;
        elif(isinstance(poly, sage.matrix.matrix.Matrix)):
            R = self.base();
            if(poly.parent().base().is_field()):
                R = R.fraction_field();
            return Matrix(R, [self.to_real(row) for row in poly]);
        elif(isinstance(poly, sage.modules.free_module_element.FreeModuleElement)):
            R = self.base();
            if(poly.parent().base().is_field()):
                R = R.fraction_field();
            return vector(R, [self.to_real(el) for el in poly]);
        elif(isinstance(poly, list)):
            return [self.to_real(el) for el in poly];
        elif(isinstance(poly, set)):
            return set([self.to_real(el) for el in poly]);
        elif(isinstance(poly, tuple)):
            return tuple([self.to_real(el) for el in poly]);
        else:
            raise TypeError("Wrong type: Impossible to get real value of element (%s)" %(poly));
            
    def simplify(self, element):
        '''
            Simplify the element receive using the relations known for the Conversion System.
            
            Several types of input are allowed:
                - An element of `self.poly_ring()` or `self.poly_field()`.
                - A List, a Set or a Tuple
                - Matrices or vectors with polynomials rocignized by the Conversion system
                - Elements in `self.base()`
        '''
        if(element in self.poly_ring()):
            try:
                return self.poly_ring()(element).reduce(self._relations());
            except AttributeError:
                return self.poly_ring()(element);
        elif(element in self.poly_field()):
            element = self.poly_field()(element);
            n = self.simplify(element.numerator());
            d = self.simplify(element.denominator());
            return n/d;
        elif(isinstance(element, list)):
            return [self.simplify(el) for el in element];
        elif(isinstance(element, set)):
            return set([self.simplify(el) for el in element]);
        elif(isinstance(element, tuple)):
            return tuple([self.simplify(el) for el in element]);
        elif(isinstance(element, sage.matrix.matrix.Matrix)):
            R = self.poly_ring();
            if(element.parent().base().is_field()):
                R = self.poly_field();
            return Matrix(R, [[self.simplify(el) for el in row] for row in element]);
        elif(isinstance(element, sage.modules.free_module_element.FreeModuleElement)):
            R = self.poly_ring();
            if(element.parent().base().is_field()):
                R = self.poly_field();
            return vector(R, [self.simplify(el) for el in element]);
        elif(element in self.base()):
            return self.to_real(self.simplify(self.to_poly(element)));
        else:
            return element;
            
    def mix_conversion(self, conversion):
        '''
            Method that mixes two conversion system of the same class. It is also allowed to mix `self` with an element of `self.base().fraction_field()`
        '''
        if(isinstance(conversion, self.__class__) or (conversion in self.base().fraction_field())):
            return self._mix_conversion(conversion);
        elif(isinstance(conversion, ConversionSystem) and isinstance(self, conversion.__class__)):
            return conversion._mix_conversion(self);
                
    ## Protected methods
    def _change_poly_ring(self, new_ring):
        if(not (self.poly_ring() is new_ring)):
            if(not(self.__relations is None)):
                self.__relations = [new_ring(el) for el in self.__relations];
                self.__rel_ideal = ideal(self.poly_ring(), []);
                
    def _relations(self):
        '''
            Returns a Groebner Basis of the relations ideals known in this conversion system.
        '''
        if(self.__relations is None):
            self.__relations = [];
            self.__rel_ideal = ideal(self.poly_ring(), []);
            
        return self.__relations;
        
    def _rel_ideal(self):
        '''
            Returns the ideal object of relations known in this conversion system.
        '''
        return self.__rel_ideal;
        
    def _to_poly_element(self, element):
        '''
            Method that cast an element in `self.base()` to a polynomial in the conversion system.
            
            This method must be implemented in each specific type of conversion system.
            
            Raise a ValueError if the element can not be casted.
        '''
        raise NotImplementedError("Abstract method not implemented '_to_poly_element(element)'");
        
    def _to_real_element(self, polynomial):
        '''
            Method that receives a polynomial in the variables on the conversion system and plug in the real values of those variables.
            
            It returns an element in self.base().
            
            This method can be overwritten if needed.
        '''
        variables = polynomial.parent().gens();
        multi = (len(variables) > _sage_const_1 );
        res = self.base().zero();
        for (k,v) in polynomial.dict().items():
            term = self.base().one();
            ## We distinguish between several variables and just one
            ## because the return of poly.dict() is different
            if(multi):
                for i in range(len(variables)):
                    term *= (self.map_of_vars()[str(variables[i])]**k[i]);
            else:
                term *= self.map_of_vars()[str(variables[_sage_const_0 ])]**k;
                
            res += term*self.base()(v);
            
        return res;
        
    def _mix_conversion(self, conversion):
        '''
            Method that, assuming `conversion` is a compatible Conversion System, mix `self` with `conversion` to a new Conversion System of the same type of `self` that can represent objects in any conversion system.
            
            This method must be implemented in each particular class extending ConversionSystem.
        '''
        raise NotImplementedError("Abstract method not implemented '_mix_conversion(conversion)'");
                
    ## Private methods
    def __add_relation(self, relation):
        '''
        General method for adding relations that accepts any kind of argument posible.
        
        Allowed input types:
            - List, Set or Tuple
            - Polynomials.
            - Fractions of polynomials.
            - Any element that can be converted using `self`.
        '''
        if(isinstance(relation, list) or isinstance(relation, set) or isinstance(relation, tuple)):
            for el in relation:
                self.__add_relation(el);
        elif(relation in self.poly_ring()):
            reduced = self.simplify(relation);
            if(reduced != _sage_const_0 ):
                self.__relations += [reduced];
        elif(relation in self.poly_field()):
            reduced = self.simplify(relation.numerator());
            if(reduced != _sage_const_0 ):
                self.__relations += [reduced];
        else:
            try:
                self.__add_relation(self.to_poly(relation));
            except Exception:
                raise TypeError("Impossible to add a non-polynomical relation");
                
    ## Magic Python methods
    def __repr__(self):
        if(self.is_polynomial()):
            return "Conversion system with %d variables" %self.poly_ring().ngens();
        else:
            return "(Empty) Conversion system";
    
    def __str__(self):
        out = "";
        out += repr(self) + "\n";
        if(self.is_polynomial()):
            out += "\tFrom: %s\n" %self.base();
            out += "\tTo  : %s\n" %self.poly_ring();
            out += "Map of the variables:\n";
            for gen in self.poly_ring().gens():
                out += "%s\t->\t%s\n" %(gen, repr(self.map_of_vars()[str(gen)]));
        return out;
        

