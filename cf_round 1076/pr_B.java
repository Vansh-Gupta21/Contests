import java.util.Scanner;

public class pr_B {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t=sc.nextInt();
        while(t-->0){
            int n=sc.nextInt();
            int[] a = new int[n];
            for(int i=0; i<n; i++){
                a[i] = sc.nextInt();
            }

            boolean isOpComp = false;

            for(int i=0; i<n && !isOpComp; i++){
                int maxVal = a[i];
                int maxPos = i;

                for(int j=i+1; j<n; j++){
                    if(a[j]>maxVal){
                        maxVal=a[j];
                        maxPos=j;
                    }
                }

                if(maxVal>a[i]){
                    rev(a, i, maxPos);
                    isOpComp=true;
                }
            }
            for(int i=0; i<n; i++){
                System.out.print(a[i]+" ");
            }
            System.out.println();
        }
    }

    public static void rev(int[] arr, int l, int r){
        while (l<r){
            int temp=arr[l];
            arr[l]=arr[r];
            arr[r]=temp;
            l++;
            r--;
        }
    }
}
