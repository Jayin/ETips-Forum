默认对DevelopmentConfig进行测试


Method	Checks that	New in
assertEqual(a, b)	a == b	 
assertNotEqual(a, b)	a != b	 
assertTrue(x)	bool(x) is True	 
assertFalse(x)	bool(x) is False	 
assertIs(a, b)	a is b	2.7
assertIsNot(a, b)	a is not b	2.7
assertIsNone(x)	x is None	2.7
assertIsNotNone(x)	x is not None	2.7
assertIn(a, b)	a in b	2.7
assertNotIn(a, b)	a not in b	2.7
assertIsInstance(a, b)	isinstance(a, b)	2.7
assertNotIsInstance(a, b)	not isinstance(a, b)	2.7