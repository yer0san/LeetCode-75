// difficulty: easy
// topics: two pointers, string

class Solution {
public:
    string reverseVowels(string s) {
        set<char> sett= {'a','e','i','o','u','A','E','I','O','U'};
        int l = 0;
        int r = s.length()-1;
        char temp;
        while (l < r){
            if (sett.count(s[l]) && sett.count(s[r])){
                temp = s[l];
                s[l] = s[r];
                s[r] = temp;
                l++;
                r--;
            }
            else if (!(sett.count(s[l])) && !(sett.count(s[r]))){
                l++;
                r--;
            }
            else if (!(sett.count(s[l])) )
                l++;
            else{
                r--;
            }
        }
        return s;
    }
};
