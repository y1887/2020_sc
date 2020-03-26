function output = student(a, b)
[m1, n1] = size(a);
[m2, n2] = size(b);

m = max(m1, m2);
n = max(n1, n2);

A = [[a zeros(m1, n - n1)]; zeros(m - m1, n)];
B = [[b zeros(m2, n - n2)]; zeros(m - m2, n)];

N = A+B;
output = max(max(N));
end
