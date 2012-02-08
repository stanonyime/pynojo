#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import hashlib
import pymongo

class Problem:
    def __init__(self, uid, title, code, desc, input_format, output_format, sample_input, sample_output, sources):
        self.pid = pid
        self.title = title
        self.code = code
        self.desc = desc
        self.input_format = input_format
        self.output_format = output_format
        self.sample_input = sample_input
        self.sample_output = sample_output
        self.sources = sources
    def update_option(self, **kwargs):
        for key in kwargs:
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
    def save(self, db): # 2=duplicate key , 1= other error, 0=ok
        if self.pid == None:
            try:
                pid = db.problems.insert(
                        {
                            'title' : self.title,
                            'code' : self.code,
                            'desc' : self.desc,
                            'input_format' : self.input_format,
                            'output_format' : self.output_format,
                            'sample_input' : self.sample_input,
                            'sample_output' : self.sample_output,
                            'sources' : self.sources
                        }, safe = True)
            except pymongo.errors.DuplicateKeyError:
                return 2
            except Exception:
                return 1
            self.pid = pid
            return 0
        else:
            try:
                db.problems.update({'code' : self.code}, {
                            'title' : self.title,
                            'code' : self.code,
                            'desc' : self.desc,
                            'input_format' : self.input_format,
                            'output_format' : self.output_format,
                            'sample_input' : self.sample_input,
                            'sample_output' : self.sample_output,
                            'sources' : self.sources
                        }, safe = True)
            except Exception:
                return 1
            return 0
    def Problem_from_code(code, db):
        k = db.problems.find_one({'code' : code})
        if k == None:
            return None
        else:
            return Problem(
                    k['_id'], k['title'], k['code'], k['desc'],
                    k['input_format'], k['output_format'],
                    k['sample_input'], k['sample_output'], k['sources']
                    )
