class measurement:
    """
    Form a number with an uncertainty.

    Note: This class does not implement many features
    but rather is a test class for uncertainties
    
    nominal \u00B1 value 

    Keyword arguments:
    value -- the nominal component
    error -- the uncertainty component

    """

    def __init__(self,value,error):
        """Initialise the nominal value and the uncertainty 
        of the measurement  """
        self._value = value
        self._error = error

    @property
    def value(self):
        """ Return the nominal value of the measurement"""
        return self._value

    @value.setter
    def value(self,value):
        """ Set the nominal value of the measurement"""
        self._value = value

    @value.deleter
    def value(self):
        """ deleter """
        del self._value

    @property
    def error(self,error):
        """ Return the uncertainty of the measurement"""
        return self._error
    @error.setter
    def error(self,error):
        """Set the uncertainty of the measurement """
        self._error = error
    @error.deleter
    def error(self):
        del self._error


    def __add__(self,other):
        """
        Add two measurements together 

        Parameters:
        argument1 (measurement): nominal \u00B1 uncertainty
        argument2 (measurement): nominal \u00B1 uncertainty
        
        Returns:
        measurement: Return nominal1 + nominal2 in nominal 
                     Return uncertainty in quadrature.
        """
        import math
        total_value = self._value + other._value
        total_error = math.sqrt(self._error**2 + other._error**2)
        return measurement(total_value,total_error )

    def __sub__(self,other):
        """
        Subtract two measurements 

        Parameters:
        argument1 (measurement): nominal \u00B1 uncertainty
        argument2 (measurement): nominal \u00B1 uncertainty

        Returns:
        measurement: Return nominal1 - nominal2 in nominal
                     Return uncertainty in quadrature.
        """

        import math
        total_value = self._value - other._value
        total_error = math.sqrt(self._error**2 + other._error**2)

        return measurement(total_value,total_error)

    def __mul__(self,other):
        """
        Multiply two measurements together

        Parameters:
        argument1 (measurement): nominal \u00B1 uncertainty
        argument2 (measurement): nominal \u00B1 uncertainty

        Returns:
        measurement: Return nominal1 * nominal2 in nominal
                     Return sqrt( nom2**2*unc1**2 + nom1**2*unc2**2).
        """

        import math
        total_value = self._value*other._value
        total_error = math.sqrt((other._value**2)*(self._error**2) + (self._value**2)*(other._error**2))

        return measurement(total_value,total_error )

    def __truediv__(self,other):
        """
        Divide two measurements together

        Parameters:
        argument1 (measurement): nominal \u00B1 uncertainty
        argument2 (measurement): nominal \u00B1 uncertainty

        Returns:
        measurement: Return nominal1/nominal2 in nominal
                     Return uncertainty propogated for a/b.
        """
        import math
        total_value = self._value/other._value
        total_error = math.sqrt(( (1/other._value)**2)*(self._error**2) + (self._value/other._value/other._value)**2*(other._error**2))
        return measurement(total_value,total_error)

    def __repr__(self):
        """
        Return representation of measurement 
        Returns: value \u00B1 error
        """
        return str(self._value) +"\u00B1" + str(self._error) 

        
x = measurement(1,1)
y = measurement(2,2)
z = measurement(3,3)

print("===============================")
help(measurement)
print("===============================")
print("x")
print(x)
print("y")
print(y)
print("z")
print(z)
print("===============================")

print("addition")
print(x+y)
print("subtract")
print(x-y)
print("multiplication")
print(x*y)
print("division")
print(x/y)
print("===============================")

print("x/y*z")
print(x/y*z)
print("===============================")



