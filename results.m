M = readmatrix('results.csv');
noiseless = M(:, 1); noisy = M(:, 2); quantum = M(:, 3);
n = length(M);

x = 1:1:n;

eig1 = 0.5*(1+sqrt(1-4/9));
eig2 = 0.5*(1-sqrt(1-4/9));
true_val = eig1*log2(1/eig1) + eig2*log2(1/eig2);

hold on;
grid on;
set(gca, 'fontsize', 32);

yline(true_val, 'Color', 'red', 'LineStyle','-.', 'LineWidth', 2, 'DisplayName','True Entropy Value');
plot(x, noiseless, 'LineWidth', 2.5, 'DisplayName', 'Noiseless (Ideal)', 'Color', '#4169E1');
plot(x, noisy, 'LineWidth', 2.5, 'DisplayName', 'Simulated Backend (IBM-Brisbane)', 'Color', '#FFA500');
plot(x, quantum, 'LineWidth', 2.5, 'DisplayName', 'Quantum Backend (IBM-Brisbane)', 'Color', '#3CB371');

xlabel("No. of Rounds");
ylabel("Entanglement Entropy");

xticks(0:20000:100000);
xticklabels({'0', '20000', '40000', '60000', '100000'})

yticks(0.0:0.2:1.0);
ytickformat("%.1f");

lgd = legend;
ax = gca;

ax.Color = [0.9176, 0.9176, 0.9529];
ax.GridColor = 'white';
ax.GridAlpha = 0.7;
xlim([-5000, 105000]);

hold off;
