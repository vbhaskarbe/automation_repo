Just as a side note i use inner functions like this.

def env():
    def add(key,val):
         setattr(env, key, val)
    env.add = add
now you can call env.add('this','that')
and reference it like env.this

i find this useful for tracking globals in a controled way


