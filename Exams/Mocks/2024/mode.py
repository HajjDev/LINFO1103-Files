def find_mode(l):
    def rec(l, mode, mode_app, candidate, candidate_app):
        if l.is_empty(): return mode
        
        if l.head() == mode:
            mode_app += 1
        else:
            if candidate == l.head():
                candidate_app += 1
                if candidate_app > mode_app:
                    mode, mode_app = candidate, candidate_app
            else:
                candidate, candidate_app = l.head(), 1
        
        return rec(l.tail(), mode, mode_app, candidate, candidate_app)

    return None if l.is_empty() else rec(l, l.head(), 0, 0, 0)