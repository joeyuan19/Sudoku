
public class ListNode {
	int[][] data;
	ListNode next;
	
	public ListNode(int[][] data, ListNode next) {
		this.data = data;
		this.next = next;
	}
	public int getSize() {
		return getSize(this);
	}
	private int getSize(ListNode n) {
		if (n.next == null) {
			return 1;
		}
		else {
			return 1 + getSize(n.next);
		}
	
	}
}
