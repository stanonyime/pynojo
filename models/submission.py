#!/usr/bin/env python


class Submission:
    def __init__(self, sid, uid, pid, score, status, detail, time, src, lang):
        self.sid = sid
        self.uid = uid
        self.pid = pid
        self.score = score
        self.status = status
        self.detail = detail
        self.time = time
        self.src = src
        self.lang = lang
    def save(self):
        if self.uid == None:
            try:
                uid = db.submissions.insert(
                        {
                            'uid' : self.uid,
                            'pid' : self.pid,
                            'score' : self.score,
                            'status' : self.status,
                            'detail' : self.detail,
                            'time' : self.time,
                            'src' : self.src,
                            'lang' : self.lang
                        }, safe = True)
            except pymongo.errors.DuplicateKeyError:
                return 1
            except Exception:
                return 2
            self.uid = uid
            return 0
        else:
            try:
                db.submissions.update({'_id' : self.sid},
                        {
                            'uid' : self.uid,
                            'pid' : self.pid,
                            'score' : self.score,
                            'status' : self.status,
                            'detail' : self.detail,
                            'time' : self.time,
                            'src' : self.src,
                            'lang' : self.lang
                        }, safe = True)
            except Exception:
                return 2
            return 0
    def update_info(self, **kwargs):
        for key in kwargs:
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
    def Submission_from_sid(db, sid):
        k = db.submissions.find_one({'_id' : sid})
        if k == None:
            return None
        else:
            return Submission(k['_id'], k['uid'], k['pid'], k['score'], k['status'], k['detail'], k['time'], k['src'], k['lang'])
    def List_of_submission_from_uid(db, uid):
        return db.submissions.find({'uid' : uid})
    def List_of_submission_from_pid(db, pid):
        return db.submissions.find({'pid' : pid})
