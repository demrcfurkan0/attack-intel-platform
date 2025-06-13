
```
attack-simulation
├─ Dockerfile
├─ app
│  ├─ __init__.py
│  ├─ core
│  │  ├─ __init__.py
│  │  ├─ config.py
│  │  ├─ event_handler.py
│  │  ├─ state.py
│  │  └─ utils.py
│  ├─ database
│  │  ├─ __init__.py
│  │  └─ database.py
│  ├─ main.py
│  ├─ models.py
│  ├─ routes.py
│  ├─ services
│  │  ├─ __init__.py
│  │  └─ simulation_handler.py
│  └─ simulations
│     ├─ __init__.py
│     ├─ brute_force_simulation.py
│     ├─ ddos_simulation.py
│     ├─ simulation_params.py
│     ├─ sqli_simulation.py
│     └─ utils.py
├─ bun.lockb
├─ components.json
├─ docker-compose.yml
├─ eslint.config.js
├─ index.html
├─ models
│  ├─ feature_columns.json
│  ├─ final_scaler.pkl
│  └─ final_xgboost_model.pkl
├─ package-lock.json
├─ package.json
├─ postcss.config.js
├─ public
│  ├─ favicon.ico
│  ├─ placeholder.svg
│  └─ robots.txt
├─ requirements.txt
├─ src
│  ├─ App.css
│  ├─ App.tsx
│  ├─ components
│  │  ├─ AlertNotificationCenter.tsx
│  │  ├─ AttackLogVisualization.tsx
│  │  ├─ AttackSimulationPanel.tsx
│  │  ├─ AttackTrendsChart.tsx
│  │  ├─ DetectionMetricsChart.tsx
│  │  ├─ ResponseCenter.tsx
│  │  ├─ UserManagement.tsx
│  │  └─ ui
│  │     ├─ accordion.tsx
│  │     ├─ alert-dialog.tsx
│  │     ├─ alert.tsx
│  │     ├─ aspect-ratio.tsx
│  │     ├─ avatar.tsx
│  │     ├─ badge.tsx
│  │     ├─ breadcrumb.tsx
│  │     ├─ button.tsx
│  │     ├─ calendar.tsx
│  │     ├─ card.tsx
│  │     ├─ carousel.tsx
│  │     ├─ chart.tsx
│  │     ├─ checkbox.tsx
│  │     ├─ collapsible.tsx
│  │     ├─ command.tsx
│  │     ├─ context-menu.tsx
│  │     ├─ dialog.tsx
│  │     ├─ drawer.tsx
│  │     ├─ dropdown-menu.tsx
│  │     ├─ form.tsx
│  │     ├─ hover-card.tsx
│  │     ├─ input-otp.tsx
│  │     ├─ input.tsx
│  │     ├─ label.tsx
│  │     ├─ menubar.tsx
│  │     ├─ navigation-menu.tsx
│  │     ├─ pagination.tsx
│  │     ├─ popover.tsx
│  │     ├─ progress.tsx
│  │     ├─ radio-group.tsx
│  │     ├─ resizable.tsx
│  │     ├─ scroll-area.tsx
│  │     ├─ select.tsx
│  │     ├─ separator.tsx
│  │     ├─ sheet.tsx
│  │     ├─ sidebar.tsx
│  │     ├─ skeleton.tsx
│  │     ├─ slider.tsx
│  │     ├─ sonner.tsx
│  │     ├─ switch.tsx
│  │     ├─ table.tsx
│  │     ├─ tabs.tsx
│  │     ├─ textarea.tsx
│  │     ├─ toast.tsx
│  │     ├─ toaster.tsx
│  │     ├─ toggle-group.tsx
│  │     ├─ toggle.tsx
│  │     ├─ tooltip.tsx
│  │     └─ use-toast.ts
│  ├─ hooks
│  │  ├─ use-mobile.tsx
│  │  └─ use-toast.ts
│  ├─ index.css
│  ├─ lib
│  │  ├─ apiClient.ts
│  │  └─ utils.ts
│  ├─ main.tsx
│  ├─ pages
│  │  ├─ Index.tsx
│  │  └─ NotFound.tsx
│  ├─ services
│  │  ├─ reportService.ts
│  │  └─ simulationService.ts
│  ├─ types
│  │  └─ apiTypes.ts
│  └─ vite-env.d.ts
├─ tailwind.config.ts
├─ tsconfig.app.json
├─ tsconfig.json
├─ tsconfig.node.json
└─ vite.config.ts

```
```
attack-intel-platform-1
├─ .dockerignore
├─ Dockerfile
├─ README.md
├─ app
│  ├─ __init__.py
│  ├─ core
│  │  ├─ __init__.py
│  │  ├─ config.py
│  │  ├─ event_handler.py
│  │  ├─ security.py
│  │  ├─ state.py
│  │  ├─ utils.py
│  │  └─ ws_manager.py
│  ├─ database
│  │  ├─ __init__.py
│  │  └─ database.py
│  ├─ main.py
│  ├─ models.py
│  ├─ routes.py
│  ├─ services
│  │  ├─ __init__.py
│  │  └─ simulation_handler.py
│  └─ simulations
│     ├─ __init__.py
│     ├─ brute_force_simulation.py
│     ├─ ddos_simulation.py
│     ├─ simulation_params.py
│     ├─ sqli_simulation.py
│     └─ utils.py
├─ bun.lockb
├─ components.json
├─ docker-compose.yml
├─ eslint.config.js
├─ index.html
├─ models
│  ├─ feature_columns.json
│  ├─ final_scaler.pkl
│  └─ final_xgboost_model.pkl
├─ package-lock.json
├─ package.json
├─ postcss.config.js
├─ public
│  ├─ favicon.ico
│  ├─ placeholder.svg
│  └─ robots.txt
├─ requirements.txt
├─ src
│  ├─ App.css
│  ├─ App.tsx
│  ├─ components
│  │  ├─ AlertNotificationCenter.tsx
│  │  ├─ AttackLogVisualization.tsx
│  │  ├─ AttackSimulationPanel.tsx
│  │  ├─ AttackTrendsChart.tsx
│  │  ├─ DetectionMetricsChart.tsx
│  │  ├─ PrivateRoute.tsx
│  │  ├─ ResponseCenter.tsx
│  │  ├─ UserManagement.tsx
│  │  ├─ cards
│  │  │  ├─ ActiveThreatsCard.tsx
│  │  │  ├─ DetectionRateCard.tsx
│  │  │  └─ TotalSimulationsCard.tsx
│  │  └─ ui
│  │     ├─ accordion.tsx
│  │     ├─ alert-dialog.tsx
│  │     ├─ alert.tsx
│  │     ├─ aspect-ratio.tsx
│  │     ├─ avatar.tsx
│  │     ├─ badge.tsx
│  │     ├─ breadcrumb.tsx
│  │     ├─ button.tsx
│  │     ├─ calendar.tsx
│  │     ├─ card.tsx
│  │     ├─ carousel.tsx
│  │     ├─ chart.tsx
│  │     ├─ checkbox.tsx
│  │     ├─ collapsible.tsx
│  │     ├─ command.tsx
│  │     ├─ context-menu.tsx
│  │     ├─ dialog.tsx
│  │     ├─ drawer.tsx
│  │     ├─ dropdown-menu.tsx
│  │     ├─ form.tsx
│  │     ├─ hover-card.tsx
│  │     ├─ input-otp.tsx
│  │     ├─ input.tsx
│  │     ├─ label.tsx
│  │     ├─ menubar.tsx
│  │     ├─ navigation-menu.tsx
│  │     ├─ pagination.tsx
│  │     ├─ popover.tsx
│  │     ├─ progress.tsx
│  │     ├─ radio-group.tsx
│  │     ├─ resizable.tsx
│  │     ├─ scroll-area.tsx
│  │     ├─ select.tsx
│  │     ├─ separator.tsx
│  │     ├─ sheet.tsx
│  │     ├─ sidebar.tsx
│  │     ├─ skeleton.tsx
│  │     ├─ slider.tsx
│  │     ├─ sonner.tsx
│  │     ├─ switch.tsx
│  │     ├─ table.tsx
│  │     ├─ tabs.tsx
│  │     ├─ textarea.tsx
│  │     ├─ toast.tsx
│  │     ├─ toaster.tsx
│  │     ├─ toggle-group.tsx
│  │     ├─ toggle.tsx
│  │     ├─ tooltip.tsx
│  │     └─ use-toast.ts
│  ├─ hooks
│  │  ├─ use-mobile.tsx
│  │  └─ use-toast.ts
│  ├─ index.css
│  ├─ lib
│  │  ├─ apiClient.ts
│  │  └─ utils.ts
│  ├─ main.tsx
│  ├─ pages
│  │  ├─ DashboardContainer.tsx
│  │  ├─ Index.tsx
│  │  ├─ LoginPage.tsx
│  │  └─ NotFound.tsx
│  ├─ services
│  │  ├─ authService.ts
│  │  ├─ reportService.ts
│  │  ├─ responseService.ts
│  │  ├─ simulationService.ts
│  │  ├─ statisticsService.ts
│  │  └─ userService.ts
│  ├─ types
│  │  └─ apiTypes.ts
│  └─ vite-env.d.ts
├─ tailwind.config.ts
├─ tsconfig.app.json
├─ tsconfig.json
├─ tsconfig.node.json
└─ vite.config.ts

```