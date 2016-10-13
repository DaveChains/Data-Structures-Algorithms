package com.datastructures.ListBased;

/**
 * Created by davidchains on 10/13/16.
 */
public class LinkedList {

    private static int counter;
    private Node head;

    public LinkedList() {}

    public void add(Object object){

    }

    private static int getCounter(){
        return counter;
    }

    private static void incrementCounter() {
        counter++;
    }

    private void decrementCounter() {
        counter--;
    }

    // inserts the specified element at the specified position in this list
    public void add(Object data, int index) {

    }

    // returns the element at the specified position in this list.

    public Object get(int index) {

    }

    // removes the element at the specified position in this list.
    public boolean remove(int index) {
    }

    // returns the number of elements in this list.
    public int size() {
        return getCounter();
    }



    private class Node {
        // reference to the next node in the chain, or null if there isn't one.
        Node next;

        // data carried by this node. could be of any type you need.
        Object data;

        // Node constructor
        public Node(Object dataValue) {
            next = null;
            data = dataValue;
        }

        // another Node constructor if we want to specify the node to point to.
        @SuppressWarnings("unused")
        public Node(Object dataValue, Node nextValue) {
            next = nextValue;
            data = dataValue;
        }

        // these methods should be self-explanatory
        public Object getData() {
            return data;
        }

        @SuppressWarnings("unused")
        public void setData(Object dataValue) {
            data = dataValue;
        }

        public Node getNext() {
            return next;
        }

        public void setNext(Node nextValue) {
            next = nextValue;
        }

    }
}
