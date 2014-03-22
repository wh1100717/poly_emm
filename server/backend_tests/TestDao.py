#!/usr/bin/env python
# -*- coding: utf-8 -*-

#=======================
#### file: testAppDao.py ####
#=======================

import sys
import os
import nose
from nose import with_setup

c_path = os.getcwd()
base_path = c_path[:c_path.rfind("backend_tests")]
sys.path.append(base_path)

# from dao import AppDao

def setup_module(module):
	print "单元测试开始"

def teardown_module(module):
	print "单元测试结束"

def setup_func():
	print "set up test fixtures"

def teardown_func():
	print "tear down test fixtures"

def test_should_be_implemented():
	print "\n1. 	ShouldBeImpelemented测试开始"
	the_target_result = "Specific result should be outputed using below method"
	assert True

def test_demo():
	print "\n2. 	TestDemo测试开始"
	the_target_result = "hello world"


def test_divid_function():
	print "\n3. 	add()测试开始"
	assert divid(2, 1) == 2
	assert divid(4, 2) == 2
	assert divid(20, 10) == 2
	assert divid(20, 0) == 0



def divid(a,b):
	if b == 0:
		return 0
	else:
		return a/b


if __name__ == "__main__":
	test_get_app_count()