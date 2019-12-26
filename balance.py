def is_balanced(s):
    map = {
        '(':')',
        '{':'}',
        '[':']'
    };
    stack = [];

    for b in s:
        if b == '{' or b == '[' or b == '(':
            stack.append(b)
        elif len(stack) == 0:
            return 'NO';
        else:
            last = stack.pop();
            if b != map[last]:
                return 'NO';
    if len(stack) != 0:
        return 'NO';
    return 'YES';


is_balanced('{}')
