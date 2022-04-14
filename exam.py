double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int i = 0, j = 0, k = 0;
    int *arr = (int *)malloc(sizeof(int) * (nums1Size + nums2Size));
    while (i < nums1Size && j < nums2Size) {
        if (nums1[i] < nums2[j]) {
            arr[k] = nums1[i];
            i++;
        } else {
            arr[k] = nums2[j];
            j++;
        }
        k++;
    }
    while (i < nums1Size) {
        arr[k] = nums1[i];
        i++;
        k++;
    }
    while (j < nums2Size) {
        arr[k] = nums2[j];
 
        j++;   
        k++;

    }
    int mid = (nums1Size + nums2Size) / 2;
    if ((nums1Size + nums2Size) % 2 == 0) {
        return (arr[mid] + arr[mid - 1]) / 2.0;
    } else {
        return arr[mid];
    }
}

