#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def main():
    try:
        configuration = open('config.txt')
    except Exception:
        print("Couldn't find the config.txt file!")

if __name__ == '__main__':
    main()

