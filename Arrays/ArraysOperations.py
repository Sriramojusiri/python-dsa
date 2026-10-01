a=[1,2,3,4,5,6]
def travesal(arr):
  print('[',end="")
  for i in range(len(arr)-1):
    print(arr[i],end=",")
  print(arr[-1],end=']')
travesal(a)
a=[1,2,3,4,5,6]  

def traversal(arr):
  print('[',end="")
  for i in range(len(arr)-1):
    print(arr[i],end=",")
  print(arr[-1],end=']')
def insert(val,ind,arr):
  ar2=[0 for i in range(len(arr)+1)]
  for i in range(0,ind):
    ar2[i]=arr[i]
  for i in range (ind,len(arr)):
    ar2[i+1]=arr[i]
  ar2[ind]=val
  return ar2
traversal(a)    
a=insert(10,2,a)
print()
traversal(a)
a=insert(20,2,a)
print()
traversal(a)


def delete(ind,arr):
    ar=[0 for i in range(len(a)-1)]
    for i in range(ind):
     ar[i]=a[i]
    for i in range(ind+1,len(a)):
     ar[i-1]=a[i]
    return(ar)
a=[1,2,3,4,5]
print(a)
a=delete(2,a)
print(a)
  
public class OneDimensionalArray // class name can't have spaces
{
    public static void main(String[] args) // 'public' lowercase, 'String[] args'
    {
        int a[] = new int[5]; // size must be 5 because we use indexes 0 to 4
        
        a[0] = 10; // you wrote a[10] but array size is only 5
        a[1] = 20;
        a[2] = 40; // you wrote 70, but output shows 40
        a[3] = 210;
        a[4] = 50;
        
        // to print with index like a[0]=10
        for (int i = 0; i < 5; i++) 
        {
            System.out.println("a[" + i + "] = " + a[i]); // 'System' not 'Systemy'
        }
    }
}


a=[1,2,3,4,5,6]
def leftshift(a,key):

  ar=[0]*(len(a))
  j=0
  for i in range(key,len(a)):
  
    ar[j]=a[i]
    j+=1
  for i in range(len(a)-key,len(a)):
    ar[j]=a[i]
    j=j+1
  print(ar)
a=[1,2,3]
a=leftshift(a,1)



a=[1,2,3,4,5,6]
def maxi(key,a):
   max=0
   sum=6
   for i in range(key,len(a)):
     sum+=a[i]
     sum-=a[i-key]
     if sum>max:
         max=sum
   print(max)
maxi(3,a)

def maxavg(key,arr):
    sum=10
    for i in range(key,len(arr)):
        sum=sum+a[i]-a[i-key]
        maxavg=sum/key 
        if maxavg==sum:
            maxavg=sum
    print(maxavg)
a=[1,2,3,4,5,6]
maxavg(4,a)


        