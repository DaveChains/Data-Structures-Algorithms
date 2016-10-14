package com.datastructures;

/**
 * Created by dcadenas on 14-10-2016.
 */

import com.datastructures.listbased.LinkedListSimple;


import org.apache.log4j.Logger;
import org.junit.Before;
import org.junit.Test;

//import org.springframework.test.context.ContextConfiguration;
//import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
//import org.springframework.test.context.support.AnnotationConfigContextLoader;
//
//
//@RunWith(SpringJUnit4ClassRunner.class)
////@ContextConfiguration(classes = AppConfig.class, loader = AnnotationConfigContextLoader.class)
//@ContextConfiguration(classes = AnnotationConfigContextLoader.class)
public class LinkedListSimpleSimpleUTest {

    protected static LinkedListSimple simpleLinkedListSimple;
    final static Logger logger = Logger.getLogger(LinkedListSimpleSimpleUTest.class);

    @Before
    public void beforeTest() {
        // Default constructor - let's put "0" into head element.
        simpleLinkedListSimple = new LinkedListSimple();
        // add more elements to LinkedListSimple
        simpleLinkedListSimple.add("1");
        simpleLinkedListSimple.add("2");
        simpleLinkedListSimple.add("3");
        simpleLinkedListSimple.add("4");
        simpleLinkedListSimple.add("5");
        simpleLinkedListSimple.add("2", 2);
    }

    @Test
    public void testSampleServiceCreateNewOrder() {
        logger.debug("Print: simpleLinkedListSimple: \t\t" + simpleLinkedListSimple);

//        System.out.println(".size(): \t\t\t\t" + simpleLinkedListSimple.size());
//        System.out.println(".get(3): \t\t\t\t" + simpleLinkedListSimple.get(3) + " (get element at index:3 - list starts from 0)");
//        System.out.println(".remove(2): \t\t\t\t" + simpleLinkedListSimple.remove(2) + " (element removed)");
//        System.out.println(".get(3): \t\t\t\t" + simpleLinkedListSimple.get(3) + " (get element at index:3 - list starts from 0)");
//        System.out.println(".size(): \t\t\t\t" + simpleLinkedListSimple.size());
//        System.out.println(".add(): \t\t\t\t" + simpleLinkedListSimple.size());
//        System.out.println("Print again: simpleLinkedListSimple: \t" + simpleLinkedListSimple);
    }
}
