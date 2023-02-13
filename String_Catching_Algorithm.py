#We use Rabin-Karp algorithm for acoomplishing our string matching algorithm.           
#The advantage of the Kmp algorithm is that it only requires O(m) and processing time, while the fastest finite state automaton also requires O(m * | Ʃ |)


#The meaning of the prefix function t[q] is the length of the largest prefix of the pattern P in the suffix string of the substring P[1..q] of the pattern P.
class KMP:
    def longest_prefix_suffix(P):
        if P[0] != ' ':
            P = ' ' + P
        m = len(P) - 1
        t = [0] * (m+1)
        k = 0
        match = 0
        for q in range(2, m+1):
            while k > 0 and P[k+1] != P[q]:
                k = t[k]
            if P[k+1] == P[q]:
                k += 1
            t[q] = k
            return t

    def kmp_matcher(T, P):
        T = ' ' + T
        P = ' ' + P
        n = len(T) - 1
        m = len(P) - 1
        t = KMP.longest_prefix_suffix(P)#Call the function longest_prefix_suffix to calculate the prefix function of mode P.
        q = 0
        for i in range(1, n+1):         #Start scanning of text T sequentially
            while q > 0 and P[q+1] != T[i]:
                q = t[q]                #When the next character fails to match (P[q+1]!=T[i]), the value of q is recalculated according to the prefix function
                if P[q+1] == T[i]:
                    q += 1
                if q == m:              #When the value of q (the number of characters already matched) is equal to the length of the pattern P, we have found a matching string
                    print (i-m+1)
                    q = 0


#Test case 1: Input string "of" from "Pirates of the Caribbean" -> output: 9
#Comment: 
#Let's assume that the prefix function has been obtained, that is, we don't care about how the prefix function is calculated. Then when we already have a way to get the prefix function, the next step is to match the pattern P.

#Line 6 calls the function longest_prefix_suffix to calculate the prefix function of mode P. 
#Line 8 begins to scan the text T sequentially, and note that the variable q records the number of characters that successfully match the pattern P at this moment. 
#When the next character fails to match (P[q+1]!=T[i]), the value of q is recalculated according to the prefix function, such as the two lines of code 9 and 10. 
#The value of q is simply incremented by 1 when a match is successful. In the last 13 lines, when the value of q (the number of characters already matched) is equal to the length of the pattern P, we have found a matching string.


