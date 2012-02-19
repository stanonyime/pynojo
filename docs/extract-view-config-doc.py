# $File: extract-view-config-doc.py
# $Date: Fri Feb 17 16:44:08 2012 +0800
# $Author: jiakai <jia.kai66@gmail.com>


output_table = [('Name', 'Pattern', 'Renderer', 'Function')]

fout = None

def add_view_extract_doc(self, *args, **kargs):
    func = kargs.get('view')
    if func is None:
        return
    fname = func.__name__
    if fname[0] == '_':
        return

    if 'attr' in kargs:
        fref = ":meth:`{0}.{1}.{2}`" . format(func.__module__, fname,
                kargs['attr'])
    else:
        fref = ":func:`{0}.{1}`" . format(func.__module__, fname)

    route_name = kargs.get('route_name')
    if route_name is None:
        output_table.append(('N/A', 'N/A', 'N/A', fref))
    else:
        from pynojo.view import _route_list
        rarg = dict()
        for i in _route_list:
            if i['name'] == route_name:
                rarg = i
                break
        output_table.append((
            route_name,
            rarg.get('pattern', 'N/A'),
            kargs.get('renderer', 'N/A'),
            fref))

def mktable(table):
    maxwidth = list()
    for i in range(len(table[0])):
        maxwidth.append(max(len(j[i]) for j in table))

    def mkrow(val, sep = '|'):
        fout.write(''.join(('+', sep.join('{{0:<{0}}}'.format(maxwidth[i]).format(val[i]) \
                for i in range(len(maxwidth))), '+')))
        fout.write('\n')

    def mksep(sep = '-'):
        mkrow([sep * i for i in maxwidth], '+')


    mksep()
    mkrow(table[0])
    mksep('=')
    for i in range(1, len(table)):
        mkrow(table[i])
        mksep()

if __name__ == '__main__':
    import sys, os
    if len(sys.argv) != 2:
        sys.exit('usage: {0} <output file>'.format(sys.argv[0]))
    fout = open(sys.argv[1], 'w')

    sys.path.insert(0, os.path.abspath('..'))

    from pyramid.config import Configurator
    Configurator.add_view = add_view_extract_doc
    conf = Configurator()
    conf.scan("pynojo")

    output_table[1:] = sorted(output_table[1:], 
            cmp = lambda a, b: cmp(a[0], b[0]))
    mktable(output_table)

