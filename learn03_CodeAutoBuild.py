# coding:utf8

import os
import re
import time

autCodeStr = """
package <packageName>;

public class <fileName> {

	/*
	 * 第一个java程序，将打印helloworld
	 */
	public static void main(String []args) {
		System.out.println("hello world");
	}
}
        """

class MakeModel:
    packageName = ''
    fileName = ''

    def __init__(self, packageName, fileName):
        self.packageName = packageName
        self.fileName = fileName
        print 'start'

    def createFile(self):
        f = open('test.java', 'w+')

        # str_a = autCodeStr.replace(self.packageName, '<packageName>')
        # str_b = str_a.replace(self.fileName, '<fileName>')

        table_a = ['<packageName>', '<fileName>']
        table_b = [self.packageName, self.fileName]
        replace_str = self.replace_var(table_a, table_b, autCodeStr)
        print replace_str

        f.write(replace_str)
        f.close()

    def replace_var(self, a, b, c):
        strinfo = re.compile(a[1])
        h = strinfo.sub(b[1], c)
        print '-------------------------'
        for x in range(len(a)):
            print 'a'+a[x]
            print 'b'+b[x]
            c = self.replace(a[x], b[x], c)
        print '========================'
        return c

    def replace(self,a,b,c):
        strinfo = re.compile(a)
        return strinfo.sub(b,c)


if __name__ == '__main__':
    javaModle = MakeModel('learnCodeAuto', 'test')
    javaModle.createFile()