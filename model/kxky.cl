__kernel void kxky(const float k_n0, const float k_m0, const float delta_k_n, const float delta_k_m, const float C1, const float C2, const float phi0, const float theta0, const float delta_phi, const float delta_theta, const int j_max, const int i_max, __global float* input, __global float* output)
{
    unsigned int m = get_global_id(0);
    //unsigned int mSize = get_global_size(0);
    unsigned int n = get_global_id(1);
    unsigned int nSize = get_global_size(1);
 	//printf("n: %d, i_max: %d, nSize: %d -- m: %d, j_max: %d, mSize: %d\n",n,i_max,nSize,m,j_max,mSize);

	float k_n = k_n0 + n * delta_k_n;
	float k_m = k_m0 + m * delta_k_m;

	float phi_n_rad = asin(k_n * C1);
	float phi_n = phi_n_rad * C2;		
	float i_n = (phi_n - phi0)/delta_phi;
	if(i_n>=0 && i_n<=i_max){
		float theta_m = asin( k_m * C1 / cos( phi_n_rad ) ) * C2;
		float j_m = (theta_m - theta0)/delta_theta;
		if(j_m >=0 && j_m <= j_max){
			unsigned int i_1 = floor(i_n);
			unsigned int i_2 = ceil(i_n);
			unsigned int j_1 = floor(j_m);
			unsigned int j_2 = ceil(j_m);
			float wR = i_n - i_1;
			float wL = 1 - wR;
			float wU = j_m - j_1;
			float wD = 1 - wU;
			//printf("%d:%d\n",m,n);
			output[n+nSize*m] = input[j_1*nSize+i_1]*wL*wD + input[j_2*nSize+i_1]*wR*wD + input[j_1*nSize+i_2]*wL*wU + input[j_2*nSize+i_2]*wR*wU;
		}else{
			output[n+nSize*m] = 0;
		}
	}else{
		output[n+nSize*m] = 0;
	}
}
