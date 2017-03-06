package com.yp.test;


import com.yp.test.entity.Cat;
import com.yp.test.comm.LogCommon2;
import org.apache.log4j.Logger;

public class HelloWorld {

    static Logger log = Logger.getLogger("no");

    public static void main(String[] args) {
        Cat c = new Cat("keyboard");
        LogCommon2.fillLogger("hello",log);
        log.info("这是log4j");
        System.out.println("hello," + c.getName());
    }

}
