M = readmatrix('bounds.csv');
estimate = M(:, 1); lcb = M(:, 2); ucb = M(:, 3);
n = length(M);
x = 1:1:n;
X = [x, fliplr(x)];
eig1 = 0.5*(1+sqrt(1-4/9));
eig2 = 0.5*(1-sqrt(1-4/9));
true_val = eig1*log2(1/eig1) + eig2*log2(1/eig2);
inBetweeen = [lcb.', fliplr(ucb.')];
hold on;
grid on;
set(gca,'fontsize', 32);


h = fill(X, inBetweeen, 'b', 'FaceAlpha',0.2, 'DisplayName', 'Confidence Interval (\delta - 0.01)', 'LineWidth', 1, 'EdgeColor','white', 'EdgeAlpha',0.2);
yline(true_val, 'Color', 'red', 'LineStyle','-.', 'LineWidth', 2, 'DisplayName','True Entropy Value');
plot(x, estimate, 'LineWidth', 2, 'DisplayName', 'Estimated Entropy', 'Color','b');
xlh = xlabel("No. of Rounds", "VerticalAlignment","top");
ylh = ylabel("Entanglement Entropy", "VerticalAlignment","bottom");
xticks(0:20000:100000);
xticklabels({'0', '20000', '40000', '60000', '80000', '100000'});
yticks(0.0:0.2:1.0);
ytickformat("%.1f");

lgd = legend;
ax = gca;
%ax.Color = [0.8, 0.8, 0.8];
ax.Color = [0.9176, 0.9176, 0.9529];
ax.GridColor = 'white';
ax.GridAlpha = 0.7;

f = gcf;
%exportgraphics(f, 'bounds.jpg', 'Resolution', 400);
xlim([-5000, 105000]);
hold off;                      