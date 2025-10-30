int minNumberOperations(int* target, int targetSize) {
    int result=target[0];
    for(int i=1;i<targetSize;i++){
        if (target[i]>target[i-1])
            result+=target[i]-target[i-1];            
    }
    return result;
}
