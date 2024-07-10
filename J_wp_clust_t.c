
#include<stdio.h>
#include<stdlib.h>
#include<math.h>

#include "/home/mohanty/util/rndxor.c"
#define LLx   2048
#define LLy  1024
#define sqLL    (LLx*LLy)
#define MM 2000

 
 //uint64_t sd[2]={8142396154175,9018612629};
 uint64_t sd[2]={8142615417598,9023186629};
 char  s[sqLL], v[sqLL]; int nbr[sqLL][4], clust[sqLL];
 double w,rho,p,J; 
int  Lx,Ly,N,sqL,pos[sqLL]; 
 double pp[4][6];
 
 
 
void nbr2d() {  int i,j,k; 
for(i=0;i<Lx; i++){ 
for(j=0;j<Ly; j++){
k =  j*Lx +i; nbr[k][0]=  j*Lx+ ((i+1)%Lx)  ; nbr[k][1]=  ((j+1)%Ly)*Lx+i; 
nbr[k][2]=  ( (i-1+Lx)%Lx) +j*Lx; nbr[k][3]=  i + Lx*((j-1+Ly)%Ly); }}
}



double cp(){ int i,j; double y, x,z; x=1+3*p; y=x+w; z= x+2*w;
pp[0][0]=1; pp[0][1]=1+p; pp[0][2]=1+2*p;pp[0][3]=x;pp[0][4]=y;pp[0][5]=z;
pp[1][0]=p; pp[1][1]=1+p; pp[1][2]=1+2*p;pp[1][3]=x;pp[1][4]=y;pp[1][5]=z;
pp[2][0]=p; pp[2][1]=p; pp[2][2]=1+2*p;pp[2][3]=x;pp[2][4]=y;pp[2][5]=z;
pp[3][0]=p; pp[3][1]=p; pp[3][2]=p;pp[3][3]=x;pp[3][4]=y; pp[3][5]=z;
for(i=0;i<4;i++) for(j=0;j<6;j++) pp[i][j]/=z;
}



//---------------- for q<=1 -----------------


char  H(int i){char k,eng=0; if(s[i]){for(k=0;k<4;k++) eng -=s[nbr[i][k]];} return 2*eng;}

void updateJ()
{ int i,j,j1,m; char k,kp; double rn, ei,ef;

 for(j1=0;j1<N;j1++)
 {	
  m=  rndx()*N; i=pos[m]; k=0; rn=rndx(); while(rn>=pp[v[i]][k]) k++;  
  if(k<4)
  {
    j=nbr[i][k];
    if(!s[j] )
    {
     ei = H(i);s[j]=1;s[i]=0;ef= H(j);
     s[j]= ef<=ei  ? 1: rndx() <exp(- J*(ef-ei));s[i]=!s[j];
	if(s[j])  v[j]=v[i], pos[m]=j;  
    }
  }
  else v[i] = (v[i]+ (k%2?1:3))%4; //(1+ k%3 +v[i]) %4;
 }
}



void update()
{ int i,j,j1,m; char k; double rn;

 for(j1=0;j1<N;j1++)
 {	
  m=  rndx()*N; i=pos[m]; k=0; rn=rndx(); while(rn>pp[v[i]][k]) k++;  
  if(k<4){j=nbr[i][k]; if(!s[j])s[i]=0,s[j]=1,v[j]=v[i],pos[m]=j;}
  else v[i] =   (v[i]+ (k%2?1:3))%4; 
 }
}



int getf4(){int n,i,k,nhbr[5]; for(k=0;k<5;k++) nhbr[k]=0;  for(n=0;n<N; n++) i=pos[n], nhbr[ s[nbr[i][0]] +  s[nbr[i][1]]   +  s[nbr[i][2]]  +  s[nbr[i][3]] ]++; return(nhbr[4]); }



void init() {int k=0,i; for(i=0;i<sqL;i++) s[i]=0, v[i]=  rndx()*4; 
 while(k<N) {i= rndx()*sqL; if  (!s[i]) s[i]=1,  pos[k]=i, k++;}}


// Function to perform percolation
void percolate(int i, int label) { int k;   
    if(clust[i]!=1) return; clust[i]= label; // Assign the label
    for(k=0;k<4;k++) percolate(nbr[i][k], label); }

// Function to find the largest cluster of particles
int  maxClust() {
    int i, j;
    int label = 2; // Start labeling from 2
  int max_size = 0;
     for(i = 0; i < sqL; i++)clust[i]=s[i];
    for(i = 0; i < sqL; i++) if(clust[i]==1) {percolate(i, label); label++;}
        int sizes[MM];    
    for(i = 0; i < label; i++) sizes[i] = 0;
    for(i = 0; i < sqL; i++)  if(clust[i]) sizes[clust[i]]++;
     for(i = 0; i < label; i++) if(sizes[i]> max_size)  max_size = sizes[i];     return (max_size);                 
      }
      
    void init1() { int k=0,i,j,n; for(i=0;i<sqL;i++) s[i]=0, v[i]=  rndx()*4;
i=0;n=0;  while(n<N){ for(j=0;j<Ly;j++) k=j*Lx +i,  pos[n]=k,s[k]=1, n++; i++;}}   
      
int main(int argc, char *argv[])
{ int i,j,k,t,l,m,M,z,e; 

double sz[MM],  sz2[MM],  sz4[MM],  f4[MM],  f42[MM], f44[MM];
long tt[MM];
char fl[50]; FILE *pt;int unit,Tmax,u,ENS;




Lx = atoi(argv[1]);  Ly = atoi(argv[2]); rho=atof(argv[3]);  p=atof(argv[4]);  w=atof(argv[5]);  J=atof(argv[6]);  u= atoi(argv[7]); e= atoi(argv[8]); M= atoi(argv[9]);

sqL=Lx*Ly; N= sqL*rho;  rho= 1.*N/sqL; unit= pow(10.,u);ENS= pow(10.,e);nbr2d();cp();
tt[0]=0; for(i=1;i<MM; i++)  tt[i]= tt[i-1]*1.01 +1;

sprintf(fl, "%sL%dr%.2f_p%.2f_w%.3f_M%d.dat", argv[10],Lx,rho,p,w,M);

for(e=1;e<ENS;e++)
{ //printf("%d\n", e);
for(u=0;u<unit;u++){ 
t=0; m=0; init(); z=maxClust();sz[m]+=z; z*=z;  sz2[t] +=z;  sz4[t]+=z*z; z=getf4();  f4[t]+=z; z*=z;  f42[t] +=z;  f44[t]+=z*z; 
for(m=1; m<M;m++) { while(t<tt[m]) update(), t++;
 z=maxClust();  sz[m]+=z; z*=z;  sz2[m] +=z;  sz4[m]+=z*z; z=getf4(); f4[m]+=z; z*=z;  f42[m] +=z;  f44[t]+=z*z;   }}
pt=fopen(fl,"w");
for(m=0; m<M;m++)fprintf(pt,"%ld %lf  %lf %lf %lf  %lf %lf\n", tt[m], sz[m]/unit/e, sz2[m]/unit/e,  sz4[m]/unit/e,  f4[m]/unit/e, f42[m]/unit/e,  f44[m]/unit/e );
fprintf(pt," %d x %d  ensembles are  done - Lx=%d Ly=%d rho= %lf p=%lf w=%lf J=%lf  M=%d\n", e,unit,Lx,Ly,rho,p,w,J,M);
fclose(pt);
}


}


