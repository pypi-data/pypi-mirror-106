import typing as t

class CaseError(Exception):
	def __init__(self, *args: object) -> None:
		'''
			Exception class for errors in cases.
		'''
		super().__init__(*args)

class Switch:
	def __init__(self,cases: t.Dict[str,t.Callable] = None, runCaseFunction: bool = False) -> None:
		'''
			Python Switch class.

			:param cases: Dict of cases.
			:param runCaseFunction: Run the case function when the case is called.
			:type cases: dict
			:type runCaseFunction: bool

			:Example:
			>>> s = Switch({"d":lambda x:x})
		'''
		self.default = lambda:None
		if cases != None:
			for name, f in cases.items():
				if not isinstance(name,str):
					raise CaseError("The case name must be a str.")
				
				if not callable(f):
					raise CaseError("The case function must be a callable function.")

				self.__setattr__(name,f)
		
		self.runCaseFunction = runCaseFunction
	
	def case(self) -> t.Callable:
		'''
			Decorate a case.

			:Example:
			>>> s = Switch()
			>>> @s.case()
			>>> def d(x): return x
		'''
		def decorator(f: t.Callable) -> t.Callable:
			self.addCase(f.__name__,f)
			return f
			
		return decorator
	
	def addCase(self,name: str,f: t.Callable) -> None:
		'''
			Add a case.

			:param name: Case name.
			:param f: Case function.
			:type name: str
			:type f: Callable

			:Example:
			>>> s = Switch()
			>>> s.addCase("d",lambda x:x)
		'''
		if not isinstance(name,str):
			raise CaseError("The case name must be a str.")

		if not callable(f):
			raise CaseError("The case function must be a callable function.")

		self.__setattr__(name,f)
	
	def get(self,name: str) -> t.Callable:
		'''
			Get a case by name.

			:param name: Case name.
			:type name: str
			:returns: Case function.
			:rtype: Callable

			:Example:
			>>> s = Switch({"d":lambda x:x})
			>>> d = s.get("d")
		'''
		if not isinstance(name,str):
			raise CaseError("The case name must be a str.")
		
		if self.runCaseFunction:
			return self.__dict__.get(name,self.default)()

		return self.__dict__.get(name,self.default)