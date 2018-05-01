string

给定一个长度为 n 的 String，切成若干个 pieces 总共有 $$2^{n-1}$$ 种切法，即对于所有 $$n-1$$ 个分界点上，选择“切/不切”.

此类问题最常用的优化，就是利用子串性质， abuse 子串的结构。
同时维护一个类似 sliding window and two pointer/ hashtable 的结构去向尾部移动，如果是 KMP pattern matching，不回滚的 window / pattern 就可以达到 linear time.

longest substring without repeating substring
hashtable + sliding window