package com.datastructures;

import com.datastructures.ListBased.LinkedList;

/**
 * Created by davidchains on 10/13/16.
 */
public class App {

    public static LinkedList simpleLinkedList;

    public static void main(String[] args) throws Exception {
        // Default constructor - let's put "0" into head element.
        simpleLinkedList = new LinkedList();

        // add more elements to LinkedList
        simpleLinkedList.add("1");
        simpleLinkedList.add("2");
        simpleLinkedList.add("3");
        simpleLinkedList.add("4");
        simpleLinkedList.add("5");
        simpleLinkedList.add("2", 2);


		/*
		 * Please note that primitive values can not be added into LinkedList directly. They must be converted to their
		 * corresponding wrapper class.
		 */
        System.out.println("Print: simpleLinkedList: \t\t" + simpleLinkedList);
        System.out.println(".size(): \t\t\t\t" + simpleLinkedList.size());
        System.out.println(".get(3): \t\t\t\t" + simpleLinkedList.get(3) + " (get element at index:3 - list starts from 0)");
        System.out.println(".remove(2): \t\t\t\t" + simpleLinkedList.remove(2) + " (element removed)");
        System.out.println(".get(3): \t\t\t\t" + simpleLinkedList.get(3) + " (get element at index:3 - list starts from 0)");
        System.out.println(".size(): \t\t\t\t" + simpleLinkedList.size());
        System.out.println(".add(): \t\t\t\t" + simpleLinkedList.size());
        System.out.println("Print again: simpleLinkedList: \t" + simpleLinkedList);    }
}
