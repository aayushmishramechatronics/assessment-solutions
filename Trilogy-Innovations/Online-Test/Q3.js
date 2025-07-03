/**
 * function ListNode(x) {
 * this.value = x;
 * this.next = null;
 * }
 */

function solution(a, b) {
    const arrA = [];
    let currentNodeA = a;
    while (currentNodeA) {
        arrA.push(currentNodeA.value);
        currentNodeA = currentNodeA.next;
    }

    const arrB = [];
    let currentNodeB = b;
    while (currentNodeB) {
        arrB.push(currentNodeB.value);
        currentNodeB = currentNodeB.next;
    }
    const resultAsArray = [];
    let carry = 0;
    
    while (arrA.length > 0 || arrB.length > 0 || carry > 0) {
        
        const num1 = arrA.pop() || 0;
        const num2 = arrB.pop() || 0;
        const currentSum = num1 + num2 + carry;
        const newNodeValue = currentSum % 10000;
        carry = Math.floor(currentSum / 10000);
        resultAsArray.unshift(newNodeValue);
    }
    if (resultAsArray.length === 0) {
        return new ListNode(0);
    }
    const resultHead = new ListNode(resultAsArray[0]);
    let currentNode = resultHead;
    
    for (let i = 1; i < resultAsArray.length; i++) {
        currentNode.next = new ListNode(resultAsArray[i]);
        currentNode = currentNode.next;
    }
    return resultHead;
}
