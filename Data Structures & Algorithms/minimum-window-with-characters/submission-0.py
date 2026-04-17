class Solution:
    def minWindow(self, s: str, t: str) -> str:
      if t=="":return ""
      countt,windows={},{}
      for c in t:
         countt[c]=1+countt.get(c,0)
      have,need=0,len(countt)
      l=0
      res,resLen=[-1,-1],float('infinity')
      for r in range(len(s)):
         c=s[r]
         windows[c]=1+windows.get(c,0)
         if c in t and windows[c]==countt[c]:
            have+=1
         while have==need:
            if (r-l+1)<resLen:
               resLen=min(resLen,r-l+1)
               res=[l,r]
            windows[s[l]]-=1
            if s[l]in t and windows[s[l]]<countt[s[l]]:
               have-=1
            l+=1
      l,r=res
      return s[l:r+1] if resLen!=float('infinity') else ''
            
