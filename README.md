
```
attack-intel-platform-1
├─ .env
├─ app
│  ├─ core
│  │  ├─ config.py
│  │  ├─ event_handler.py
│  │  ├─ state.py
│  │  ├─ utils.py
│  │  └─ __init__.py
│  ├─ database
│  │  ├─ database.py
│  │  └─ __init__.py
│  ├─ main.py
│  ├─ models.py
│  ├─ routes.py
│  ├─ services
│  │  ├─ simulation_handler.py
│  │  └─ __init__.py
│  ├─ simulations
│  │  ├─ brute_force_simulation.py
│  │  ├─ ddos_simulation.py
│  │  ├─ simulation_params.py
│  │  ├─ sqli_simulation.py
│  │  ├─ utils.py
│  │  └─ __init__.py
│  └─ __init__.py
├─ bun.lockb
├─ components.json
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
│  │  ├─ ui
│  │  │  ├─ accordion.tsx
│  │  │  ├─ alert-dialog.tsx
│  │  │  ├─ alert.tsx
│  │  │  ├─ aspect-ratio.tsx
│  │  │  ├─ avatar.tsx
│  │  │  ├─ badge.tsx
│  │  │  ├─ breadcrumb.tsx
│  │  │  ├─ button.tsx
│  │  │  ├─ calendar.tsx
│  │  │  ├─ card.tsx
│  │  │  ├─ carousel.tsx
│  │  │  ├─ chart.tsx
│  │  │  ├─ checkbox.tsx
│  │  │  ├─ collapsible.tsx
│  │  │  ├─ command.tsx
│  │  │  ├─ context-menu.tsx
│  │  │  ├─ dialog.tsx
│  │  │  ├─ drawer.tsx
│  │  │  ├─ dropdown-menu.tsx
│  │  │  ├─ form.tsx
│  │  │  ├─ hover-card.tsx
│  │  │  ├─ input-otp.tsx
│  │  │  ├─ input.tsx
│  │  │  ├─ label.tsx
│  │  │  ├─ menubar.tsx
│  │  │  ├─ navigation-menu.tsx
│  │  │  ├─ pagination.tsx
│  │  │  ├─ popover.tsx
│  │  │  ├─ progress.tsx
│  │  │  ├─ radio-group.tsx
│  │  │  ├─ resizable.tsx
│  │  │  ├─ scroll-area.tsx
│  │  │  ├─ select.tsx
│  │  │  ├─ separator.tsx
│  │  │  ├─ sheet.tsx
│  │  │  ├─ sidebar.tsx
│  │  │  ├─ skeleton.tsx
│  │  │  ├─ slider.tsx
│  │  │  ├─ sonner.tsx
│  │  │  ├─ switch.tsx
│  │  │  ├─ table.tsx
│  │  │  ├─ tabs.tsx
│  │  │  ├─ textarea.tsx
│  │  │  ├─ toast.tsx
│  │  │  ├─ toaster.tsx
│  │  │  ├─ toggle-group.tsx
│  │  │  ├─ toggle.tsx
│  │  │  ├─ tooltip.tsx
│  │  │  └─ use-toast.ts
│  │  └─ UserManagement.tsx
│  ├─ hooks
│  │  ├─ use-mobile.tsx
│  │  └─ use-toast.ts
│  ├─ index.css
│  ├─ lib
│  │  └─ utils.ts
│  ├─ main.tsx
│  ├─ pages
│  │  ├─ Index.tsx
│  │  └─ NotFound.tsx
│  └─ vite-env.d.ts
├─ tailwind.config.ts
├─ tsconfig.app.json
├─ tsconfig.json
├─ tsconfig.node.json
├─ venv
│  ├─ bin
│  │  ├─ activate
│  │  ├─ activate.csh
│  │  ├─ activate.fish
│  │  ├─ Activate.ps1
│  │  ├─ dotenv
│  │  ├─ email_validator
│  │  ├─ f2py
│  │  ├─ fastapi
│  │  ├─ httpx
│  │  ├─ markdown-it
│  │  ├─ numpy-config
│  │  ├─ pip
│  │  ├─ pip3
│  │  ├─ pip3.12
│  │  ├─ pygmentize
│  │  ├─ python
│  │  ├─ python3
│  │  ├─ python3.12
│  │  ├─ typer
│  │  ├─ uvicorn
│  │  ├─ watchfiles
│  │  └─ websockets
│  ├─ lib
│  │  └─ python3.12
│  │     └─ site-packages
│  │        ├─ annotated_types
│  │        │  ├─ py.typed
│  │        │  ├─ test_cases.py
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     ├─ test_cases.cpython-312.pyc
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ annotated_types-0.7.0.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ licenses
│  │        │  │  └─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  └─ WHEEL
│  │        ├─ anyio
│  │        │  ├─ abc
│  │        │  │  ├─ _eventloop.py
│  │        │  │  ├─ _resources.py
│  │        │  │  ├─ _sockets.py
│  │        │  │  ├─ _streams.py
│  │        │  │  ├─ _subprocesses.py
│  │        │  │  ├─ _tasks.py
│  │        │  │  ├─ _testing.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ _eventloop.cpython-312.pyc
│  │        │  │     ├─ _resources.cpython-312.pyc
│  │        │  │     ├─ _sockets.cpython-312.pyc
│  │        │  │     ├─ _streams.cpython-312.pyc
│  │        │  │     ├─ _subprocesses.cpython-312.pyc
│  │        │  │     ├─ _tasks.cpython-312.pyc
│  │        │  │     ├─ _testing.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ from_thread.py
│  │        │  ├─ lowlevel.py
│  │        │  ├─ py.typed
│  │        │  ├─ pytest_plugin.py
│  │        │  ├─ streams
│  │        │  │  ├─ buffered.py
│  │        │  │  ├─ file.py
│  │        │  │  ├─ memory.py
│  │        │  │  ├─ stapled.py
│  │        │  │  ├─ text.py
│  │        │  │  ├─ tls.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ buffered.cpython-312.pyc
│  │        │  │     ├─ file.cpython-312.pyc
│  │        │  │     ├─ memory.cpython-312.pyc
│  │        │  │     ├─ stapled.cpython-312.pyc
│  │        │  │     ├─ text.cpython-312.pyc
│  │        │  │     ├─ tls.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ to_interpreter.py
│  │        │  ├─ to_process.py
│  │        │  ├─ to_thread.py
│  │        │  ├─ _backends
│  │        │  │  ├─ _asyncio.py
│  │        │  │  ├─ _trio.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ _asyncio.cpython-312.pyc
│  │        │  │     ├─ _trio.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ _core
│  │        │  │  ├─ _asyncio_selector_thread.py
│  │        │  │  ├─ _eventloop.py
│  │        │  │  ├─ _exceptions.py
│  │        │  │  ├─ _fileio.py
│  │        │  │  ├─ _resources.py
│  │        │  │  ├─ _signals.py
│  │        │  │  ├─ _sockets.py
│  │        │  │  ├─ _streams.py
│  │        │  │  ├─ _subprocesses.py
│  │        │  │  ├─ _synchronization.py
│  │        │  │  ├─ _tasks.py
│  │        │  │  ├─ _tempfile.py
│  │        │  │  ├─ _testing.py
│  │        │  │  ├─ _typedattr.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ _asyncio_selector_thread.cpython-312.pyc
│  │        │  │     ├─ _eventloop.cpython-312.pyc
│  │        │  │     ├─ _exceptions.cpython-312.pyc
│  │        │  │     ├─ _fileio.cpython-312.pyc
│  │        │  │     ├─ _resources.cpython-312.pyc
│  │        │  │     ├─ _signals.cpython-312.pyc
│  │        │  │     ├─ _sockets.cpython-312.pyc
│  │        │  │     ├─ _streams.cpython-312.pyc
│  │        │  │     ├─ _subprocesses.cpython-312.pyc
│  │        │  │     ├─ _synchronization.cpython-312.pyc
│  │        │  │     ├─ _tasks.cpython-312.pyc
│  │        │  │     ├─ _tempfile.cpython-312.pyc
│  │        │  │     ├─ _testing.cpython-312.pyc
│  │        │  │     ├─ _typedattr.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     ├─ from_thread.cpython-312.pyc
│  │        │     ├─ lowlevel.cpython-312.pyc
│  │        │     ├─ pytest_plugin.cpython-312.pyc
│  │        │     ├─ to_interpreter.cpython-312.pyc
│  │        │     ├─ to_process.cpython-312.pyc
│  │        │     ├─ to_thread.cpython-312.pyc
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ anyio-4.9.0.dist-info
│  │        │  ├─ entry_points.txt
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ top_level.txt
│  │        │  └─ WHEEL
│  │        ├─ asyncio
│  │        │  ├─ base_events.py
│  │        │  ├─ base_subprocess.py
│  │        │  ├─ constants.py
│  │        │  ├─ coroutines.py
│  │        │  ├─ events.py
│  │        │  ├─ futures.py
│  │        │  ├─ locks.py
│  │        │  ├─ log.py
│  │        │  ├─ proactor_events.py
│  │        │  ├─ protocols.py
│  │        │  ├─ queues.py
│  │        │  ├─ selectors.py
│  │        │  ├─ selector_events.py
│  │        │  ├─ sslproto.py
│  │        │  ├─ streams.py
│  │        │  ├─ subprocess.py
│  │        │  ├─ tasks.py
│  │        │  ├─ test_support.py
│  │        │  ├─ test_utils.py
│  │        │  ├─ transports.py
│  │        │  ├─ unix_events.py
│  │        │  ├─ windows_events.py
│  │        │  ├─ windows_utils.py
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     ├─ base_subprocess.cpython-312.pyc
│  │        │     ├─ constants.cpython-312.pyc
│  │        │     ├─ coroutines.cpython-312.pyc
│  │        │     ├─ events.cpython-312.pyc
│  │        │     ├─ futures.cpython-312.pyc
│  │        │     ├─ locks.cpython-312.pyc
│  │        │     ├─ log.cpython-312.pyc
│  │        │     ├─ proactor_events.cpython-312.pyc
│  │        │     ├─ protocols.cpython-312.pyc
│  │        │     ├─ queues.cpython-312.pyc
│  │        │     ├─ selectors.cpython-312.pyc
│  │        │     ├─ selector_events.cpython-312.pyc
│  │        │     ├─ sslproto.cpython-312.pyc
│  │        │     ├─ streams.cpython-312.pyc
│  │        │     ├─ subprocess.cpython-312.pyc
│  │        │     ├─ test_support.cpython-312.pyc
│  │        │     ├─ test_utils.cpython-312.pyc
│  │        │     ├─ transports.cpython-312.pyc
│  │        │     ├─ unix_events.cpython-312.pyc
│  │        │     ├─ windows_utils.cpython-312.pyc
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ asyncio-3.4.3.dist-info
│  │        │  ├─ DESCRIPTION.rst
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ metadata.json
│  │        │  ├─ RECORD
│  │        │  ├─ REQUESTED
│  │        │  ├─ top_level.txt
│  │        │  └─ WHEEL
│  │        ├─ bson
│  │        │  ├─ binary.py
│  │        │  ├─ bson-endian.h
│  │        │  ├─ buffer.c
│  │        │  ├─ buffer.h
│  │        │  ├─ code.py
│  │        │  ├─ codec_options.py
│  │        │  ├─ datetime_ms.py
│  │        │  ├─ dbref.py
│  │        │  ├─ decimal128.py
│  │        │  ├─ errors.py
│  │        │  ├─ int64.py
│  │        │  ├─ json_util.py
│  │        │  ├─ max_key.py
│  │        │  ├─ min_key.py
│  │        │  ├─ objectid.py
│  │        │  ├─ py.typed
│  │        │  ├─ raw_bson.py
│  │        │  ├─ regex.py
│  │        │  ├─ son.py
│  │        │  ├─ time64.c
│  │        │  ├─ time64.h
│  │        │  ├─ time64_config.h
│  │        │  ├─ time64_limits.h
│  │        │  ├─ timestamp.py
│  │        │  ├─ typings.py
│  │        │  ├─ tz_util.py
│  │        │  ├─ _cbson.cpython-310-darwin.so
│  │        │  ├─ _cbson.cpython-311-darwin.so
│  │        │  ├─ _cbson.cpython-312-darwin.so
│  │        │  ├─ _cbson.cpython-39-darwin.so
│  │        │  ├─ _cbsonmodule.c
│  │        │  ├─ _cbsonmodule.h
│  │        │  ├─ _helpers.py
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     ├─ binary.cpython-312.pyc
│  │        │     ├─ code.cpython-312.pyc
│  │        │     ├─ codec_options.cpython-312.pyc
│  │        │     ├─ datetime_ms.cpython-312.pyc
│  │        │     ├─ dbref.cpython-312.pyc
│  │        │     ├─ decimal128.cpython-312.pyc
│  │        │     ├─ errors.cpython-312.pyc
│  │        │     ├─ int64.cpython-312.pyc
│  │        │     ├─ json_util.cpython-312.pyc
│  │        │     ├─ max_key.cpython-312.pyc
│  │        │     ├─ min_key.cpython-312.pyc
│  │        │     ├─ objectid.cpython-312.pyc
│  │        │     ├─ raw_bson.cpython-312.pyc
│  │        │     ├─ regex.cpython-312.pyc
│  │        │     ├─ son.cpython-312.pyc
│  │        │     ├─ timestamp.cpython-312.pyc
│  │        │     ├─ typings.cpython-312.pyc
│  │        │     ├─ tz_util.cpython-312.pyc
│  │        │     ├─ _helpers.cpython-312.pyc
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ certifi
│  │        │  ├─ cacert.pem
│  │        │  ├─ core.py
│  │        │  ├─ py.typed
│  │        │  ├─ __init__.py
│  │        │  ├─ __main__.py
│  │        │  └─ __pycache__
│  │        │     ├─ core.cpython-312.pyc
│  │        │     ├─ __init__.cpython-312.pyc
│  │        │     └─ __main__.cpython-312.pyc
│  │        ├─ certifi-2025.4.26.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ licenses
│  │        │  │  └─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ top_level.txt
│  │        │  └─ WHEEL
│  │        ├─ click
│  │        │  ├─ core.py
│  │        │  ├─ decorators.py
│  │        │  ├─ exceptions.py
│  │        │  ├─ formatting.py
│  │        │  ├─ globals.py
│  │        │  ├─ parser.py
│  │        │  ├─ py.typed
│  │        │  ├─ shell_completion.py
│  │        │  ├─ termui.py
│  │        │  ├─ testing.py
│  │        │  ├─ types.py
│  │        │  ├─ utils.py
│  │        │  ├─ _compat.py
│  │        │  ├─ _termui_impl.py
│  │        │  ├─ _textwrap.py
│  │        │  ├─ _winconsole.py
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     ├─ core.cpython-312.pyc
│  │        │     ├─ decorators.cpython-312.pyc
│  │        │     ├─ exceptions.cpython-312.pyc
│  │        │     ├─ formatting.cpython-312.pyc
│  │        │     ├─ globals.cpython-312.pyc
│  │        │     ├─ parser.cpython-312.pyc
│  │        │     ├─ shell_completion.cpython-312.pyc
│  │        │     ├─ termui.cpython-312.pyc
│  │        │     ├─ testing.cpython-312.pyc
│  │        │     ├─ types.cpython-312.pyc
│  │        │     ├─ utils.cpython-312.pyc
│  │        │     ├─ _compat.cpython-312.pyc
│  │        │     ├─ _termui_impl.cpython-312.pyc
│  │        │     ├─ _textwrap.cpython-312.pyc
│  │        │     ├─ _winconsole.cpython-312.pyc
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ click-8.2.1.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ licenses
│  │        │  │  └─ LICENSE.txt
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  └─ WHEEL
│  │        ├─ dateutil
│  │        │  ├─ easter.py
│  │        │  ├─ parser
│  │        │  │  ├─ isoparser.py
│  │        │  │  ├─ _parser.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ isoparser.cpython-312.pyc
│  │        │  │     ├─ _parser.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ relativedelta.py
│  │        │  ├─ rrule.py
│  │        │  ├─ tz
│  │        │  │  ├─ tz.py
│  │        │  │  ├─ win.py
│  │        │  │  ├─ _common.py
│  │        │  │  ├─ _factories.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ tz.cpython-312.pyc
│  │        │  │     ├─ win.cpython-312.pyc
│  │        │  │     ├─ _common.cpython-312.pyc
│  │        │  │     ├─ _factories.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ tzwin.py
│  │        │  ├─ utils.py
│  │        │  ├─ zoneinfo
│  │        │  │  ├─ dateutil-zoneinfo.tar.gz
│  │        │  │  ├─ rebuild.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ rebuild.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ _common.py
│  │        │  ├─ _version.py
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     ├─ easter.cpython-312.pyc
│  │        │     ├─ relativedelta.cpython-312.pyc
│  │        │     ├─ rrule.cpython-312.pyc
│  │        │     ├─ tzwin.cpython-312.pyc
│  │        │     ├─ utils.cpython-312.pyc
│  │        │     ├─ _common.cpython-312.pyc
│  │        │     ├─ _version.cpython-312.pyc
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ dns
│  │        │  ├─ asyncbackend.py
│  │        │  ├─ asyncquery.py
│  │        │  ├─ asyncresolver.py
│  │        │  ├─ dnssec.py
│  │        │  ├─ dnssecalgs
│  │        │  │  ├─ base.py
│  │        │  │  ├─ cryptography.py
│  │        │  │  ├─ dsa.py
│  │        │  │  ├─ ecdsa.py
│  │        │  │  ├─ eddsa.py
│  │        │  │  ├─ rsa.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ base.cpython-312.pyc
│  │        │  │     ├─ cryptography.cpython-312.pyc
│  │        │  │     ├─ dsa.cpython-312.pyc
│  │        │  │     ├─ ecdsa.cpython-312.pyc
│  │        │  │     ├─ eddsa.cpython-312.pyc
│  │        │  │     ├─ rsa.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ dnssectypes.py
│  │        │  ├─ e164.py
│  │        │  ├─ edns.py
│  │        │  ├─ entropy.py
│  │        │  ├─ enum.py
│  │        │  ├─ exception.py
│  │        │  ├─ flags.py
│  │        │  ├─ grange.py
│  │        │  ├─ immutable.py
│  │        │  ├─ inet.py
│  │        │  ├─ ipv4.py
│  │        │  ├─ ipv6.py
│  │        │  ├─ message.py
│  │        │  ├─ name.py
│  │        │  ├─ namedict.py
│  │        │  ├─ nameserver.py
│  │        │  ├─ node.py
│  │        │  ├─ opcode.py
│  │        │  ├─ py.typed
│  │        │  ├─ query.py
│  │        │  ├─ quic
│  │        │  │  ├─ _asyncio.py
│  │        │  │  ├─ _common.py
│  │        │  │  ├─ _sync.py
│  │        │  │  ├─ _trio.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ _asyncio.cpython-312.pyc
│  │        │  │     ├─ _common.cpython-312.pyc
│  │        │  │     ├─ _sync.cpython-312.pyc
│  │        │  │     ├─ _trio.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ rcode.py
│  │        │  ├─ rdata.py
│  │        │  ├─ rdataclass.py
│  │        │  ├─ rdataset.py
│  │        │  ├─ rdatatype.py
│  │        │  ├─ rdtypes
│  │        │  │  ├─ ANY
│  │        │  │  │  ├─ AFSDB.py
│  │        │  │  │  ├─ AMTRELAY.py
│  │        │  │  │  ├─ AVC.py
│  │        │  │  │  ├─ CAA.py
│  │        │  │  │  ├─ CDNSKEY.py
│  │        │  │  │  ├─ CDS.py
│  │        │  │  │  ├─ CERT.py
│  │        │  │  │  ├─ CNAME.py
│  │        │  │  │  ├─ CSYNC.py
│  │        │  │  │  ├─ DLV.py
│  │        │  │  │  ├─ DNAME.py
│  │        │  │  │  ├─ DNSKEY.py
│  │        │  │  │  ├─ DS.py
│  │        │  │  │  ├─ EUI48.py
│  │        │  │  │  ├─ EUI64.py
│  │        │  │  │  ├─ GPOS.py
│  │        │  │  │  ├─ HINFO.py
│  │        │  │  │  ├─ HIP.py
│  │        │  │  │  ├─ ISDN.py
│  │        │  │  │  ├─ L32.py
│  │        │  │  │  ├─ L64.py
│  │        │  │  │  ├─ LOC.py
│  │        │  │  │  ├─ LP.py
│  │        │  │  │  ├─ MX.py
│  │        │  │  │  ├─ NID.py
│  │        │  │  │  ├─ NINFO.py
│  │        │  │  │  ├─ NS.py
│  │        │  │  │  ├─ NSEC.py
│  │        │  │  │  ├─ NSEC3.py
│  │        │  │  │  ├─ NSEC3PARAM.py
│  │        │  │  │  ├─ OPENPGPKEY.py
│  │        │  │  │  ├─ OPT.py
│  │        │  │  │  ├─ PTR.py
│  │        │  │  │  ├─ RESINFO.py
│  │        │  │  │  ├─ RP.py
│  │        │  │  │  ├─ RRSIG.py
│  │        │  │  │  ├─ RT.py
│  │        │  │  │  ├─ SMIMEA.py
│  │        │  │  │  ├─ SOA.py
│  │        │  │  │  ├─ SPF.py
│  │        │  │  │  ├─ SSHFP.py
│  │        │  │  │  ├─ TKEY.py
│  │        │  │  │  ├─ TLSA.py
│  │        │  │  │  ├─ TSIG.py
│  │        │  │  │  ├─ TXT.py
│  │        │  │  │  ├─ URI.py
│  │        │  │  │  ├─ WALLET.py
│  │        │  │  │  ├─ X25.py
│  │        │  │  │  ├─ ZONEMD.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ AFSDB.cpython-312.pyc
│  │        │  │  │     ├─ AMTRELAY.cpython-312.pyc
│  │        │  │  │     ├─ AVC.cpython-312.pyc
│  │        │  │  │     ├─ CAA.cpython-312.pyc
│  │        │  │  │     ├─ CDNSKEY.cpython-312.pyc
│  │        │  │  │     ├─ CDS.cpython-312.pyc
│  │        │  │  │     ├─ CERT.cpython-312.pyc
│  │        │  │  │     ├─ CNAME.cpython-312.pyc
│  │        │  │  │     ├─ CSYNC.cpython-312.pyc
│  │        │  │  │     ├─ DLV.cpython-312.pyc
│  │        │  │  │     ├─ DNAME.cpython-312.pyc
│  │        │  │  │     ├─ DNSKEY.cpython-312.pyc
│  │        │  │  │     ├─ DS.cpython-312.pyc
│  │        │  │  │     ├─ EUI48.cpython-312.pyc
│  │        │  │  │     ├─ EUI64.cpython-312.pyc
│  │        │  │  │     ├─ GPOS.cpython-312.pyc
│  │        │  │  │     ├─ HINFO.cpython-312.pyc
│  │        │  │  │     ├─ HIP.cpython-312.pyc
│  │        │  │  │     ├─ ISDN.cpython-312.pyc
│  │        │  │  │     ├─ L32.cpython-312.pyc
│  │        │  │  │     ├─ L64.cpython-312.pyc
│  │        │  │  │     ├─ LOC.cpython-312.pyc
│  │        │  │  │     ├─ LP.cpython-312.pyc
│  │        │  │  │     ├─ MX.cpython-312.pyc
│  │        │  │  │     ├─ NID.cpython-312.pyc
│  │        │  │  │     ├─ NINFO.cpython-312.pyc
│  │        │  │  │     ├─ NS.cpython-312.pyc
│  │        │  │  │     ├─ NSEC.cpython-312.pyc
│  │        │  │  │     ├─ NSEC3.cpython-312.pyc
│  │        │  │  │     ├─ NSEC3PARAM.cpython-312.pyc
│  │        │  │  │     ├─ OPENPGPKEY.cpython-312.pyc
│  │        │  │  │     ├─ OPT.cpython-312.pyc
│  │        │  │  │     ├─ PTR.cpython-312.pyc
│  │        │  │  │     ├─ RESINFO.cpython-312.pyc
│  │        │  │  │     ├─ RP.cpython-312.pyc
│  │        │  │  │     ├─ RRSIG.cpython-312.pyc
│  │        │  │  │     ├─ RT.cpython-312.pyc
│  │        │  │  │     ├─ SMIMEA.cpython-312.pyc
│  │        │  │  │     ├─ SOA.cpython-312.pyc
│  │        │  │  │     ├─ SPF.cpython-312.pyc
│  │        │  │  │     ├─ SSHFP.cpython-312.pyc
│  │        │  │  │     ├─ TKEY.cpython-312.pyc
│  │        │  │  │     ├─ TLSA.cpython-312.pyc
│  │        │  │  │     ├─ TSIG.cpython-312.pyc
│  │        │  │  │     ├─ TXT.cpython-312.pyc
│  │        │  │  │     ├─ URI.cpython-312.pyc
│  │        │  │  │     ├─ WALLET.cpython-312.pyc
│  │        │  │  │     ├─ X25.cpython-312.pyc
│  │        │  │  │     ├─ ZONEMD.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ CH
│  │        │  │  │  ├─ A.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ A.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ dnskeybase.py
│  │        │  │  ├─ dsbase.py
│  │        │  │  ├─ euibase.py
│  │        │  │  ├─ IN
│  │        │  │  │  ├─ A.py
│  │        │  │  │  ├─ AAAA.py
│  │        │  │  │  ├─ APL.py
│  │        │  │  │  ├─ DHCID.py
│  │        │  │  │  ├─ HTTPS.py
│  │        │  │  │  ├─ IPSECKEY.py
│  │        │  │  │  ├─ KX.py
│  │        │  │  │  ├─ NAPTR.py
│  │        │  │  │  ├─ NSAP.py
│  │        │  │  │  ├─ NSAP_PTR.py
│  │        │  │  │  ├─ PX.py
│  │        │  │  │  ├─ SRV.py
│  │        │  │  │  ├─ SVCB.py
│  │        │  │  │  ├─ WKS.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ A.cpython-312.pyc
│  │        │  │  │     ├─ AAAA.cpython-312.pyc
│  │        │  │  │     ├─ APL.cpython-312.pyc
│  │        │  │  │     ├─ DHCID.cpython-312.pyc
│  │        │  │  │     ├─ HTTPS.cpython-312.pyc
│  │        │  │  │     ├─ IPSECKEY.cpython-312.pyc
│  │        │  │  │     ├─ KX.cpython-312.pyc
│  │        │  │  │     ├─ NAPTR.cpython-312.pyc
│  │        │  │  │     ├─ NSAP.cpython-312.pyc
│  │        │  │  │     ├─ NSAP_PTR.cpython-312.pyc
│  │        │  │  │     ├─ PX.cpython-312.pyc
│  │        │  │  │     ├─ SRV.cpython-312.pyc
│  │        │  │  │     ├─ SVCB.cpython-312.pyc
│  │        │  │  │     ├─ WKS.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ mxbase.py
│  │        │  │  ├─ nsbase.py
│  │        │  │  ├─ svcbbase.py
│  │        │  │  ├─ tlsabase.py
│  │        │  │  ├─ txtbase.py
│  │        │  │  ├─ util.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ dnskeybase.cpython-312.pyc
│  │        │  │     ├─ dsbase.cpython-312.pyc
│  │        │  │     ├─ euibase.cpython-312.pyc
│  │        │  │     ├─ mxbase.cpython-312.pyc
│  │        │  │     ├─ nsbase.cpython-312.pyc
│  │        │  │     ├─ svcbbase.cpython-312.pyc
│  │        │  │     ├─ tlsabase.cpython-312.pyc
│  │        │  │     ├─ txtbase.cpython-312.pyc
│  │        │  │     ├─ util.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ renderer.py
│  │        │  ├─ resolver.py
│  │        │  ├─ reversename.py
│  │        │  ├─ rrset.py
│  │        │  ├─ serial.py
│  │        │  ├─ set.py
│  │        │  ├─ tokenizer.py
│  │        │  ├─ transaction.py
│  │        │  ├─ tsig.py
│  │        │  ├─ tsigkeyring.py
│  │        │  ├─ ttl.py
│  │        │  ├─ update.py
│  │        │  ├─ version.py
│  │        │  ├─ versioned.py
│  │        │  ├─ win32util.py
│  │        │  ├─ wire.py
│  │        │  ├─ xfr.py
│  │        │  ├─ zone.py
│  │        │  ├─ zonefile.py
│  │        │  ├─ zonetypes.py
│  │        │  ├─ _asyncbackend.py
│  │        │  ├─ _asyncio_backend.py
│  │        │  ├─ _ddr.py
│  │        │  ├─ _features.py
│  │        │  ├─ _immutable_ctx.py
│  │        │  ├─ _trio_backend.py
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     ├─ asyncbackend.cpython-312.pyc
│  │        │     ├─ asyncquery.cpython-312.pyc
│  │        │     ├─ asyncresolver.cpython-312.pyc
│  │        │     ├─ dnssec.cpython-312.pyc
│  │        │     ├─ dnssectypes.cpython-312.pyc
│  │        │     ├─ e164.cpython-312.pyc
│  │        │     ├─ edns.cpython-312.pyc
│  │        │     ├─ entropy.cpython-312.pyc
│  │        │     ├─ enum.cpython-312.pyc
│  │        │     ├─ exception.cpython-312.pyc
│  │        │     ├─ flags.cpython-312.pyc
│  │        │     ├─ grange.cpython-312.pyc
│  │        │     ├─ immutable.cpython-312.pyc
│  │        │     ├─ inet.cpython-312.pyc
│  │        │     ├─ ipv4.cpython-312.pyc
│  │        │     ├─ ipv6.cpython-312.pyc
│  │        │     ├─ message.cpython-312.pyc
│  │        │     ├─ name.cpython-312.pyc
│  │        │     ├─ namedict.cpython-312.pyc
│  │        │     ├─ nameserver.cpython-312.pyc
│  │        │     ├─ node.cpython-312.pyc
│  │        │     ├─ opcode.cpython-312.pyc
│  │        │     ├─ query.cpython-312.pyc
│  │        │     ├─ rcode.cpython-312.pyc
│  │        │     ├─ rdata.cpython-312.pyc
│  │        │     ├─ rdataclass.cpython-312.pyc
│  │        │     ├─ rdataset.cpython-312.pyc
│  │        │     ├─ rdatatype.cpython-312.pyc
│  │        │     ├─ renderer.cpython-312.pyc
│  │        │     ├─ resolver.cpython-312.pyc
│  │        │     ├─ reversename.cpython-312.pyc
│  │        │     ├─ rrset.cpython-312.pyc
│  │        │     ├─ serial.cpython-312.pyc
│  │        │     ├─ set.cpython-312.pyc
│  │        │     ├─ tokenizer.cpython-312.pyc
│  │        │     ├─ transaction.cpython-312.pyc
│  │        │     ├─ tsig.cpython-312.pyc
│  │        │     ├─ tsigkeyring.cpython-312.pyc
│  │        │     ├─ ttl.cpython-312.pyc
│  │        │     ├─ update.cpython-312.pyc
│  │        │     ├─ version.cpython-312.pyc
│  │        │     ├─ versioned.cpython-312.pyc
│  │        │     ├─ win32util.cpython-312.pyc
│  │        │     ├─ wire.cpython-312.pyc
│  │        │     ├─ xfr.cpython-312.pyc
│  │        │     ├─ zone.cpython-312.pyc
│  │        │     ├─ zonefile.cpython-312.pyc
│  │        │     ├─ zonetypes.cpython-312.pyc
│  │        │     ├─ _asyncbackend.cpython-312.pyc
│  │        │     ├─ _asyncio_backend.cpython-312.pyc
│  │        │     ├─ _ddr.cpython-312.pyc
│  │        │     ├─ _features.cpython-312.pyc
│  │        │     ├─ _immutable_ctx.cpython-312.pyc
│  │        │     ├─ _trio_backend.cpython-312.pyc
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ dnspython-2.7.0.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ licenses
│  │        │  │  └─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  └─ WHEEL
│  │        ├─ dotenv
│  │        │  ├─ cli.py
│  │        │  ├─ ipython.py
│  │        │  ├─ main.py
│  │        │  ├─ parser.py
│  │        │  ├─ py.typed
│  │        │  ├─ variables.py
│  │        │  ├─ version.py
│  │        │  ├─ __init__.py
│  │        │  ├─ __main__.py
│  │        │  └─ __pycache__
│  │        │     ├─ cli.cpython-312.pyc
│  │        │     ├─ ipython.cpython-312.pyc
│  │        │     ├─ main.cpython-312.pyc
│  │        │     ├─ parser.cpython-312.pyc
│  │        │     ├─ variables.cpython-312.pyc
│  │        │     ├─ version.cpython-312.pyc
│  │        │     ├─ __init__.cpython-312.pyc
│  │        │     └─ __main__.cpython-312.pyc
│  │        ├─ email_validator
│  │        │  ├─ deliverability.py
│  │        │  ├─ exceptions_types.py
│  │        │  ├─ py.typed
│  │        │  ├─ rfc_constants.py
│  │        │  ├─ syntax.py
│  │        │  ├─ validate_email.py
│  │        │  ├─ version.py
│  │        │  ├─ __init__.py
│  │        │  ├─ __main__.py
│  │        │  └─ __pycache__
│  │        │     ├─ deliverability.cpython-312.pyc
│  │        │     ├─ exceptions_types.cpython-312.pyc
│  │        │     ├─ rfc_constants.cpython-312.pyc
│  │        │     ├─ syntax.cpython-312.pyc
│  │        │     ├─ validate_email.cpython-312.pyc
│  │        │     ├─ version.cpython-312.pyc
│  │        │     ├─ __init__.cpython-312.pyc
│  │        │     └─ __main__.cpython-312.pyc
│  │        ├─ email_validator-2.2.0.dist-info
│  │        │  ├─ entry_points.txt
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ top_level.txt
│  │        │  └─ WHEEL
│  │        ├─ fastapi
│  │        │  ├─ applications.py
│  │        │  ├─ background.py
│  │        │  ├─ cli.py
│  │        │  ├─ concurrency.py
│  │        │  ├─ datastructures.py
│  │        │  ├─ dependencies
│  │        │  │  ├─ models.py
│  │        │  │  ├─ utils.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ models.cpython-312.pyc
│  │        │  │     ├─ utils.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ encoders.py
│  │        │  ├─ exceptions.py
│  │        │  ├─ exception_handlers.py
│  │        │  ├─ logger.py
│  │        │  ├─ middleware
│  │        │  │  ├─ cors.py
│  │        │  │  ├─ gzip.py
│  │        │  │  ├─ httpsredirect.py
│  │        │  │  ├─ trustedhost.py
│  │        │  │  ├─ wsgi.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ cors.cpython-312.pyc
│  │        │  │     ├─ gzip.cpython-312.pyc
│  │        │  │     ├─ httpsredirect.cpython-312.pyc
│  │        │  │     ├─ trustedhost.cpython-312.pyc
│  │        │  │     ├─ wsgi.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ openapi
│  │        │  │  ├─ constants.py
│  │        │  │  ├─ docs.py
│  │        │  │  ├─ models.py
│  │        │  │  ├─ utils.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ constants.cpython-312.pyc
│  │        │  │     ├─ docs.cpython-312.pyc
│  │        │  │     ├─ models.cpython-312.pyc
│  │        │  │     ├─ utils.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ params.py
│  │        │  ├─ param_functions.py
│  │        │  ├─ py.typed
│  │        │  ├─ requests.py
│  │        │  ├─ responses.py
│  │        │  ├─ routing.py
│  │        │  ├─ security
│  │        │  │  ├─ api_key.py
│  │        │  │  ├─ base.py
│  │        │  │  ├─ http.py
│  │        │  │  ├─ oauth2.py
│  │        │  │  ├─ open_id_connect_url.py
│  │        │  │  ├─ utils.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ api_key.cpython-312.pyc
│  │        │  │     ├─ base.cpython-312.pyc
│  │        │  │     ├─ http.cpython-312.pyc
│  │        │  │     ├─ oauth2.cpython-312.pyc
│  │        │  │     ├─ open_id_connect_url.cpython-312.pyc
│  │        │  │     ├─ utils.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ staticfiles.py
│  │        │  ├─ templating.py
│  │        │  ├─ testclient.py
│  │        │  ├─ types.py
│  │        │  ├─ utils.py
│  │        │  ├─ websockets.py
│  │        │  ├─ _compat.py
│  │        │  ├─ __init__.py
│  │        │  ├─ __main__.py
│  │        │  └─ __pycache__
│  │        │     ├─ applications.cpython-312.pyc
│  │        │     ├─ background.cpython-312.pyc
│  │        │     ├─ cli.cpython-312.pyc
│  │        │     ├─ concurrency.cpython-312.pyc
│  │        │     ├─ datastructures.cpython-312.pyc
│  │        │     ├─ encoders.cpython-312.pyc
│  │        │     ├─ exceptions.cpython-312.pyc
│  │        │     ├─ exception_handlers.cpython-312.pyc
│  │        │     ├─ logger.cpython-312.pyc
│  │        │     ├─ params.cpython-312.pyc
│  │        │     ├─ param_functions.cpython-312.pyc
│  │        │     ├─ requests.cpython-312.pyc
│  │        │     ├─ responses.cpython-312.pyc
│  │        │     ├─ routing.cpython-312.pyc
│  │        │     ├─ staticfiles.cpython-312.pyc
│  │        │     ├─ templating.cpython-312.pyc
│  │        │     ├─ testclient.cpython-312.pyc
│  │        │     ├─ types.cpython-312.pyc
│  │        │     ├─ utils.cpython-312.pyc
│  │        │     ├─ websockets.cpython-312.pyc
│  │        │     ├─ _compat.cpython-312.pyc
│  │        │     ├─ __init__.cpython-312.pyc
│  │        │     └─ __main__.cpython-312.pyc
│  │        ├─ fastapi-0.115.12.dist-info
│  │        │  ├─ entry_points.txt
│  │        │  ├─ INSTALLER
│  │        │  ├─ licenses
│  │        │  │  └─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ REQUESTED
│  │        │  └─ WHEEL
│  │        ├─ fastapi_cli
│  │        │  ├─ cli.py
│  │        │  ├─ discover.py
│  │        │  ├─ exceptions.py
│  │        │  ├─ logging.py
│  │        │  ├─ py.typed
│  │        │  ├─ utils
│  │        │  │  ├─ cli.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ cli.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ __init__.py
│  │        │  ├─ __main__.py
│  │        │  └─ __pycache__
│  │        │     ├─ cli.cpython-312.pyc
│  │        │     ├─ discover.cpython-312.pyc
│  │        │     ├─ exceptions.cpython-312.pyc
│  │        │     ├─ logging.cpython-312.pyc
│  │        │     ├─ __init__.cpython-312.pyc
│  │        │     └─ __main__.cpython-312.pyc
│  │        ├─ fastapi_cli-0.0.7.dist-info
│  │        │  ├─ entry_points.txt
│  │        │  ├─ INSTALLER
│  │        │  ├─ licenses
│  │        │  │  └─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  └─ WHEEL
│  │        ├─ gridfs
│  │        │  ├─ asynchronous
│  │        │  │  ├─ grid_file.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ grid_file.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ errors.py
│  │        │  ├─ grid_file.py
│  │        │  ├─ grid_file_shared.py
│  │        │  ├─ py.typed
│  │        │  ├─ synchronous
│  │        │  │  ├─ grid_file.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ grid_file.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     ├─ errors.cpython-312.pyc
│  │        │     ├─ grid_file.cpython-312.pyc
│  │        │     ├─ grid_file_shared.cpython-312.pyc
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ h11
│  │        │  ├─ py.typed
│  │        │  ├─ _abnf.py
│  │        │  ├─ _connection.py
│  │        │  ├─ _events.py
│  │        │  ├─ _headers.py
│  │        │  ├─ _readers.py
│  │        │  ├─ _receivebuffer.py
│  │        │  ├─ _state.py
│  │        │  ├─ _util.py
│  │        │  ├─ _version.py
│  │        │  ├─ _writers.py
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     ├─ _abnf.cpython-312.pyc
│  │        │     ├─ _connection.cpython-312.pyc
│  │        │     ├─ _events.cpython-312.pyc
│  │        │     ├─ _headers.cpython-312.pyc
│  │        │     ├─ _readers.cpython-312.pyc
│  │        │     ├─ _receivebuffer.cpython-312.pyc
│  │        │     ├─ _state.cpython-312.pyc
│  │        │     ├─ _util.cpython-312.pyc
│  │        │     ├─ _version.cpython-312.pyc
│  │        │     ├─ _writers.cpython-312.pyc
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ h11-0.16.0.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ licenses
│  │        │  │  └─ LICENSE.txt
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ top_level.txt
│  │        │  └─ WHEEL
│  │        ├─ httpcore
│  │        │  ├─ py.typed
│  │        │  ├─ _api.py
│  │        │  ├─ _async
│  │        │  │  ├─ connection.py
│  │        │  │  ├─ connection_pool.py
│  │        │  │  ├─ http11.py
│  │        │  │  ├─ http2.py
│  │        │  │  ├─ http_proxy.py
│  │        │  │  ├─ interfaces.py
│  │        │  │  ├─ socks_proxy.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ connection.cpython-312.pyc
│  │        │  │     ├─ connection_pool.cpython-312.pyc
│  │        │  │     ├─ http11.cpython-312.pyc
│  │        │  │     ├─ http2.cpython-312.pyc
│  │        │  │     ├─ http_proxy.cpython-312.pyc
│  │        │  │     ├─ interfaces.cpython-312.pyc
│  │        │  │     ├─ socks_proxy.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ _backends
│  │        │  │  ├─ anyio.py
│  │        │  │  ├─ auto.py
│  │        │  │  ├─ base.py
│  │        │  │  ├─ mock.py
│  │        │  │  ├─ sync.py
│  │        │  │  ├─ trio.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ anyio.cpython-312.pyc
│  │        │  │     ├─ auto.cpython-312.pyc
│  │        │  │     ├─ base.cpython-312.pyc
│  │        │  │     ├─ mock.cpython-312.pyc
│  │        │  │     ├─ sync.cpython-312.pyc
│  │        │  │     ├─ trio.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ _exceptions.py
│  │        │  ├─ _models.py
│  │        │  ├─ _ssl.py
│  │        │  ├─ _sync
│  │        │  │  ├─ connection.py
│  │        │  │  ├─ connection_pool.py
│  │        │  │  ├─ http11.py
│  │        │  │  ├─ http2.py
│  │        │  │  ├─ http_proxy.py
│  │        │  │  ├─ interfaces.py
│  │        │  │  ├─ socks_proxy.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ connection.cpython-312.pyc
│  │        │  │     ├─ connection_pool.cpython-312.pyc
│  │        │  │     ├─ http11.cpython-312.pyc
│  │        │  │     ├─ http2.cpython-312.pyc
│  │        │  │     ├─ http_proxy.cpython-312.pyc
│  │        │  │     ├─ interfaces.cpython-312.pyc
│  │        │  │     ├─ socks_proxy.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ _synchronization.py
│  │        │  ├─ _trace.py
│  │        │  ├─ _utils.py
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     ├─ _api.cpython-312.pyc
│  │        │     ├─ _exceptions.cpython-312.pyc
│  │        │     ├─ _models.cpython-312.pyc
│  │        │     ├─ _ssl.cpython-312.pyc
│  │        │     ├─ _synchronization.cpython-312.pyc
│  │        │     ├─ _trace.cpython-312.pyc
│  │        │     ├─ _utils.cpython-312.pyc
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ httpcore-1.0.9.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ licenses
│  │        │  │  └─ LICENSE.md
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  └─ WHEEL
│  │        ├─ httptools
│  │        │  ├─ parser
│  │        │  │  ├─ cparser.pxd
│  │        │  │  ├─ errors.py
│  │        │  │  ├─ parser.cpython-312-darwin.so
│  │        │  │  ├─ parser.pyx
│  │        │  │  ├─ python.pxd
│  │        │  │  ├─ url_cparser.pxd
│  │        │  │  ├─ url_parser.cpython-312-darwin.so
│  │        │  │  ├─ url_parser.pyx
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ errors.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ _version.py
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     ├─ _version.cpython-312.pyc
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ httptools-0.6.4.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ top_level.txt
│  │        │  └─ WHEEL
│  │        ├─ httpx
│  │        │  ├─ py.typed
│  │        │  ├─ _api.py
│  │        │  ├─ _auth.py
│  │        │  ├─ _client.py
│  │        │  ├─ _config.py
│  │        │  ├─ _content.py
│  │        │  ├─ _decoders.py
│  │        │  ├─ _exceptions.py
│  │        │  ├─ _main.py
│  │        │  ├─ _models.py
│  │        │  ├─ _multipart.py
│  │        │  ├─ _status_codes.py
│  │        │  ├─ _transports
│  │        │  │  ├─ asgi.py
│  │        │  │  ├─ base.py
│  │        │  │  ├─ default.py
│  │        │  │  ├─ mock.py
│  │        │  │  ├─ wsgi.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ asgi.cpython-312.pyc
│  │        │  │     ├─ base.cpython-312.pyc
│  │        │  │     ├─ default.cpython-312.pyc
│  │        │  │     ├─ mock.cpython-312.pyc
│  │        │  │     ├─ wsgi.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ _types.py
│  │        │  ├─ _urlparse.py
│  │        │  ├─ _urls.py
│  │        │  ├─ _utils.py
│  │        │  ├─ __init__.py
│  │        │  ├─ __pycache__
│  │        │  │  ├─ _api.cpython-312.pyc
│  │        │  │  ├─ _auth.cpython-312.pyc
│  │        │  │  ├─ _client.cpython-312.pyc
│  │        │  │  ├─ _config.cpython-312.pyc
│  │        │  │  ├─ _content.cpython-312.pyc
│  │        │  │  ├─ _decoders.cpython-312.pyc
│  │        │  │  ├─ _exceptions.cpython-312.pyc
│  │        │  │  ├─ _main.cpython-312.pyc
│  │        │  │  ├─ _models.cpython-312.pyc
│  │        │  │  ├─ _multipart.cpython-312.pyc
│  │        │  │  ├─ _status_codes.cpython-312.pyc
│  │        │  │  ├─ _types.cpython-312.pyc
│  │        │  │  ├─ _urlparse.cpython-312.pyc
│  │        │  │  ├─ _urls.cpython-312.pyc
│  │        │  │  ├─ _utils.cpython-312.pyc
│  │        │  │  ├─ __init__.cpython-312.pyc
│  │        │  │  └─ __version__.cpython-312.pyc
│  │        │  └─ __version__.py
│  │        ├─ httpx-0.28.1.dist-info
│  │        │  ├─ entry_points.txt
│  │        │  ├─ INSTALLER
│  │        │  ├─ licenses
│  │        │  │  └─ LICENSE.md
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  └─ WHEEL
│  │        ├─ idna
│  │        │  ├─ codec.py
│  │        │  ├─ compat.py
│  │        │  ├─ core.py
│  │        │  ├─ idnadata.py
│  │        │  ├─ intranges.py
│  │        │  ├─ package_data.py
│  │        │  ├─ py.typed
│  │        │  ├─ uts46data.py
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     ├─ codec.cpython-312.pyc
│  │        │     ├─ compat.cpython-312.pyc
│  │        │     ├─ core.cpython-312.pyc
│  │        │     ├─ idnadata.cpython-312.pyc
│  │        │     ├─ intranges.cpython-312.pyc
│  │        │     ├─ package_data.cpython-312.pyc
│  │        │     ├─ uts46data.cpython-312.pyc
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ idna-3.10.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE.md
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  └─ WHEEL
│  │        ├─ itsdangerous
│  │        │  ├─ encoding.py
│  │        │  ├─ exc.py
│  │        │  ├─ py.typed
│  │        │  ├─ serializer.py
│  │        │  ├─ signer.py
│  │        │  ├─ timed.py
│  │        │  ├─ url_safe.py
│  │        │  ├─ _json.py
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     ├─ encoding.cpython-312.pyc
│  │        │     ├─ exc.cpython-312.pyc
│  │        │     ├─ serializer.cpython-312.pyc
│  │        │     ├─ signer.cpython-312.pyc
│  │        │     ├─ timed.cpython-312.pyc
│  │        │     ├─ url_safe.cpython-312.pyc
│  │        │     ├─ _json.cpython-312.pyc
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ itsdangerous-2.2.0.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE.txt
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  └─ WHEEL
│  │        ├─ jinja2
│  │        │  ├─ async_utils.py
│  │        │  ├─ bccache.py
│  │        │  ├─ compiler.py
│  │        │  ├─ constants.py
│  │        │  ├─ debug.py
│  │        │  ├─ defaults.py
│  │        │  ├─ environment.py
│  │        │  ├─ exceptions.py
│  │        │  ├─ ext.py
│  │        │  ├─ filters.py
│  │        │  ├─ idtracking.py
│  │        │  ├─ lexer.py
│  │        │  ├─ loaders.py
│  │        │  ├─ meta.py
│  │        │  ├─ nativetypes.py
│  │        │  ├─ nodes.py
│  │        │  ├─ optimizer.py
│  │        │  ├─ parser.py
│  │        │  ├─ py.typed
│  │        │  ├─ runtime.py
│  │        │  ├─ sandbox.py
│  │        │  ├─ tests.py
│  │        │  ├─ utils.py
│  │        │  ├─ visitor.py
│  │        │  ├─ _identifier.py
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     ├─ async_utils.cpython-312.pyc
│  │        │     ├─ bccache.cpython-312.pyc
│  │        │     ├─ compiler.cpython-312.pyc
│  │        │     ├─ constants.cpython-312.pyc
│  │        │     ├─ debug.cpython-312.pyc
│  │        │     ├─ defaults.cpython-312.pyc
│  │        │     ├─ environment.cpython-312.pyc
│  │        │     ├─ exceptions.cpython-312.pyc
│  │        │     ├─ ext.cpython-312.pyc
│  │        │     ├─ filters.cpython-312.pyc
│  │        │     ├─ idtracking.cpython-312.pyc
│  │        │     ├─ lexer.cpython-312.pyc
│  │        │     ├─ loaders.cpython-312.pyc
│  │        │     ├─ meta.cpython-312.pyc
│  │        │     ├─ nativetypes.cpython-312.pyc
│  │        │     ├─ nodes.cpython-312.pyc
│  │        │     ├─ optimizer.cpython-312.pyc
│  │        │     ├─ parser.cpython-312.pyc
│  │        │     ├─ runtime.cpython-312.pyc
│  │        │     ├─ sandbox.cpython-312.pyc
│  │        │     ├─ tests.cpython-312.pyc
│  │        │     ├─ utils.cpython-312.pyc
│  │        │     ├─ visitor.cpython-312.pyc
│  │        │     ├─ _identifier.cpython-312.pyc
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ jinja2-3.1.6.dist-info
│  │        │  ├─ entry_points.txt
│  │        │  ├─ INSTALLER
│  │        │  ├─ licenses
│  │        │  │  └─ LICENSE.txt
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  └─ WHEEL
│  │        ├─ joblib
│  │        │  ├─ backports.py
│  │        │  ├─ compressor.py
│  │        │  ├─ disk.py
│  │        │  ├─ executor.py
│  │        │  ├─ externals
│  │        │  │  ├─ cloudpickle
│  │        │  │  │  ├─ cloudpickle.py
│  │        │  │  │  ├─ cloudpickle_fast.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ cloudpickle.cpython-312.pyc
│  │        │  │  │     ├─ cloudpickle_fast.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ loky
│  │        │  │  │  ├─ backend
│  │        │  │  │  │  ├─ context.py
│  │        │  │  │  │  ├─ fork_exec.py
│  │        │  │  │  │  ├─ popen_loky_posix.py
│  │        │  │  │  │  ├─ popen_loky_win32.py
│  │        │  │  │  │  ├─ process.py
│  │        │  │  │  │  ├─ queues.py
│  │        │  │  │  │  ├─ reduction.py
│  │        │  │  │  │  ├─ resource_tracker.py
│  │        │  │  │  │  ├─ spawn.py
│  │        │  │  │  │  ├─ synchronize.py
│  │        │  │  │  │  ├─ utils.py
│  │        │  │  │  │  ├─ _posix_reduction.py
│  │        │  │  │  │  ├─ _win_reduction.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ context.cpython-312.pyc
│  │        │  │  │  │     ├─ fork_exec.cpython-312.pyc
│  │        │  │  │  │     ├─ popen_loky_posix.cpython-312.pyc
│  │        │  │  │  │     ├─ popen_loky_win32.cpython-312.pyc
│  │        │  │  │  │     ├─ process.cpython-312.pyc
│  │        │  │  │  │     ├─ queues.cpython-312.pyc
│  │        │  │  │  │     ├─ reduction.cpython-312.pyc
│  │        │  │  │  │     ├─ resource_tracker.cpython-312.pyc
│  │        │  │  │  │     ├─ spawn.cpython-312.pyc
│  │        │  │  │  │     ├─ synchronize.cpython-312.pyc
│  │        │  │  │  │     ├─ utils.cpython-312.pyc
│  │        │  │  │  │     ├─ _posix_reduction.cpython-312.pyc
│  │        │  │  │  │     ├─ _win_reduction.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ cloudpickle_wrapper.py
│  │        │  │  │  ├─ initializers.py
│  │        │  │  │  ├─ process_executor.py
│  │        │  │  │  ├─ reusable_executor.py
│  │        │  │  │  ├─ _base.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ cloudpickle_wrapper.cpython-312.pyc
│  │        │  │  │     ├─ initializers.cpython-312.pyc
│  │        │  │  │     ├─ process_executor.cpython-312.pyc
│  │        │  │  │     ├─ reusable_executor.cpython-312.pyc
│  │        │  │  │     ├─ _base.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ func_inspect.py
│  │        │  ├─ hashing.py
│  │        │  ├─ logger.py
│  │        │  ├─ memory.py
│  │        │  ├─ numpy_pickle.py
│  │        │  ├─ numpy_pickle_compat.py
│  │        │  ├─ numpy_pickle_utils.py
│  │        │  ├─ parallel.py
│  │        │  ├─ pool.py
│  │        │  ├─ test
│  │        │  │  ├─ common.py
│  │        │  │  ├─ data
│  │        │  │  │  ├─ create_numpy_pickle.py
│  │        │  │  │  ├─ joblib_0.10.0_compressed_pickle_py27_np16.gz
│  │        │  │  │  ├─ joblib_0.10.0_compressed_pickle_py27_np17.gz
│  │        │  │  │  ├─ joblib_0.10.0_compressed_pickle_py33_np18.gz
│  │        │  │  │  ├─ joblib_0.10.0_compressed_pickle_py34_np19.gz
│  │        │  │  │  ├─ joblib_0.10.0_compressed_pickle_py35_np19.gz
│  │        │  │  │  ├─ joblib_0.10.0_pickle_py27_np17.pkl
│  │        │  │  │  ├─ joblib_0.10.0_pickle_py27_np17.pkl.bz2
│  │        │  │  │  ├─ joblib_0.10.0_pickle_py27_np17.pkl.gzip
│  │        │  │  │  ├─ joblib_0.10.0_pickle_py27_np17.pkl.lzma
│  │        │  │  │  ├─ joblib_0.10.0_pickle_py27_np17.pkl.xz
│  │        │  │  │  ├─ joblib_0.10.0_pickle_py33_np18.pkl
│  │        │  │  │  ├─ joblib_0.10.0_pickle_py33_np18.pkl.bz2
│  │        │  │  │  ├─ joblib_0.10.0_pickle_py33_np18.pkl.gzip
│  │        │  │  │  ├─ joblib_0.10.0_pickle_py33_np18.pkl.lzma
│  │        │  │  │  ├─ joblib_0.10.0_pickle_py33_np18.pkl.xz
│  │        │  │  │  ├─ joblib_0.10.0_pickle_py34_np19.pkl
│  │        │  │  │  ├─ joblib_0.10.0_pickle_py34_np19.pkl.bz2
│  │        │  │  │  ├─ joblib_0.10.0_pickle_py34_np19.pkl.gzip
│  │        │  │  │  ├─ joblib_0.10.0_pickle_py34_np19.pkl.lzma
│  │        │  │  │  ├─ joblib_0.10.0_pickle_py34_np19.pkl.xz
│  │        │  │  │  ├─ joblib_0.10.0_pickle_py35_np19.pkl
│  │        │  │  │  ├─ joblib_0.10.0_pickle_py35_np19.pkl.bz2
│  │        │  │  │  ├─ joblib_0.10.0_pickle_py35_np19.pkl.gzip
│  │        │  │  │  ├─ joblib_0.10.0_pickle_py35_np19.pkl.lzma
│  │        │  │  │  ├─ joblib_0.10.0_pickle_py35_np19.pkl.xz
│  │        │  │  │  ├─ joblib_0.11.0_compressed_pickle_py36_np111.gz
│  │        │  │  │  ├─ joblib_0.11.0_pickle_py36_np111.pkl
│  │        │  │  │  ├─ joblib_0.11.0_pickle_py36_np111.pkl.bz2
│  │        │  │  │  ├─ joblib_0.11.0_pickle_py36_np111.pkl.gzip
│  │        │  │  │  ├─ joblib_0.11.0_pickle_py36_np111.pkl.lzma
│  │        │  │  │  ├─ joblib_0.11.0_pickle_py36_np111.pkl.xz
│  │        │  │  │  ├─ joblib_0.8.4_compressed_pickle_py27_np17.gz
│  │        │  │  │  ├─ joblib_0.9.2_compressed_pickle_py27_np16.gz
│  │        │  │  │  ├─ joblib_0.9.2_compressed_pickle_py27_np17.gz
│  │        │  │  │  ├─ joblib_0.9.2_compressed_pickle_py34_np19.gz
│  │        │  │  │  ├─ joblib_0.9.2_compressed_pickle_py35_np19.gz
│  │        │  │  │  ├─ joblib_0.9.2_pickle_py27_np16.pkl
│  │        │  │  │  ├─ joblib_0.9.2_pickle_py27_np16.pkl_01.npy
│  │        │  │  │  ├─ joblib_0.9.2_pickle_py27_np16.pkl_02.npy
│  │        │  │  │  ├─ joblib_0.9.2_pickle_py27_np16.pkl_03.npy
│  │        │  │  │  ├─ joblib_0.9.2_pickle_py27_np16.pkl_04.npy
│  │        │  │  │  ├─ joblib_0.9.2_pickle_py27_np17.pkl
│  │        │  │  │  ├─ joblib_0.9.2_pickle_py27_np17.pkl_01.npy
│  │        │  │  │  ├─ joblib_0.9.2_pickle_py27_np17.pkl_02.npy
│  │        │  │  │  ├─ joblib_0.9.2_pickle_py27_np17.pkl_03.npy
│  │        │  │  │  ├─ joblib_0.9.2_pickle_py27_np17.pkl_04.npy
│  │        │  │  │  ├─ joblib_0.9.2_pickle_py33_np18.pkl
│  │        │  │  │  ├─ joblib_0.9.2_pickle_py33_np18.pkl_01.npy
│  │        │  │  │  ├─ joblib_0.9.2_pickle_py33_np18.pkl_02.npy
│  │        │  │  │  ├─ joblib_0.9.2_pickle_py33_np18.pkl_03.npy
│  │        │  │  │  ├─ joblib_0.9.2_pickle_py33_np18.pkl_04.npy
│  │        │  │  │  ├─ joblib_0.9.2_pickle_py34_np19.pkl
│  │        │  │  │  ├─ joblib_0.9.2_pickle_py34_np19.pkl_01.npy
│  │        │  │  │  ├─ joblib_0.9.2_pickle_py34_np19.pkl_02.npy
│  │        │  │  │  ├─ joblib_0.9.2_pickle_py34_np19.pkl_03.npy
│  │        │  │  │  ├─ joblib_0.9.2_pickle_py34_np19.pkl_04.npy
│  │        │  │  │  ├─ joblib_0.9.2_pickle_py35_np19.pkl
│  │        │  │  │  ├─ joblib_0.9.2_pickle_py35_np19.pkl_01.npy
│  │        │  │  │  ├─ joblib_0.9.2_pickle_py35_np19.pkl_02.npy
│  │        │  │  │  ├─ joblib_0.9.2_pickle_py35_np19.pkl_03.npy
│  │        │  │  │  ├─ joblib_0.9.2_pickle_py35_np19.pkl_04.npy
│  │        │  │  │  ├─ joblib_0.9.4.dev0_compressed_cache_size_pickle_py35_np19.gz
│  │        │  │  │  ├─ joblib_0.9.4.dev0_compressed_cache_size_pickle_py35_np19.gz_01.npy.z
│  │        │  │  │  ├─ joblib_0.9.4.dev0_compressed_cache_size_pickle_py35_np19.gz_02.npy.z
│  │        │  │  │  ├─ joblib_0.9.4.dev0_compressed_cache_size_pickle_py35_np19.gz_03.npy.z
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ create_numpy_pickle.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ testutils.py
│  │        │  │  ├─ test_backports.py
│  │        │  │  ├─ test_cloudpickle_wrapper.py
│  │        │  │  ├─ test_config.py
│  │        │  │  ├─ test_dask.py
│  │        │  │  ├─ test_disk.py
│  │        │  │  ├─ test_func_inspect.py
│  │        │  │  ├─ test_func_inspect_special_encoding.py
│  │        │  │  ├─ test_hashing.py
│  │        │  │  ├─ test_init.py
│  │        │  │  ├─ test_logger.py
│  │        │  │  ├─ test_memmapping.py
│  │        │  │  ├─ test_memory.py
│  │        │  │  ├─ test_memory_async.py
│  │        │  │  ├─ test_missing_multiprocessing.py
│  │        │  │  ├─ test_module.py
│  │        │  │  ├─ test_numpy_pickle.py
│  │        │  │  ├─ test_numpy_pickle_compat.py
│  │        │  │  ├─ test_numpy_pickle_utils.py
│  │        │  │  ├─ test_parallel.py
│  │        │  │  ├─ test_store_backends.py
│  │        │  │  ├─ test_testing.py
│  │        │  │  ├─ test_utils.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ common.cpython-312.pyc
│  │        │  │     ├─ testutils.cpython-312.pyc
│  │        │  │     ├─ test_backports.cpython-312.pyc
│  │        │  │     ├─ test_cloudpickle_wrapper.cpython-312.pyc
│  │        │  │     ├─ test_config.cpython-312.pyc
│  │        │  │     ├─ test_dask.cpython-312.pyc
│  │        │  │     ├─ test_disk.cpython-312.pyc
│  │        │  │     ├─ test_func_inspect.cpython-312.pyc
│  │        │  │     ├─ test_func_inspect_special_encoding.cpython-312.pyc
│  │        │  │     ├─ test_hashing.cpython-312.pyc
│  │        │  │     ├─ test_init.cpython-312.pyc
│  │        │  │     ├─ test_logger.cpython-312.pyc
│  │        │  │     ├─ test_memmapping.cpython-312.pyc
│  │        │  │     ├─ test_memory.cpython-312.pyc
│  │        │  │     ├─ test_memory_async.cpython-312.pyc
│  │        │  │     ├─ test_missing_multiprocessing.cpython-312.pyc
│  │        │  │     ├─ test_module.cpython-312.pyc
│  │        │  │     ├─ test_numpy_pickle.cpython-312.pyc
│  │        │  │     ├─ test_numpy_pickle_compat.cpython-312.pyc
│  │        │  │     ├─ test_numpy_pickle_utils.cpython-312.pyc
│  │        │  │     ├─ test_parallel.cpython-312.pyc
│  │        │  │     ├─ test_store_backends.cpython-312.pyc
│  │        │  │     ├─ test_testing.cpython-312.pyc
│  │        │  │     ├─ test_utils.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ testing.py
│  │        │  ├─ _cloudpickle_wrapper.py
│  │        │  ├─ _dask.py
│  │        │  ├─ _memmapping_reducer.py
│  │        │  ├─ _multiprocessing_helpers.py
│  │        │  ├─ _parallel_backends.py
│  │        │  ├─ _store_backends.py
│  │        │  ├─ _utils.py
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     ├─ backports.cpython-312.pyc
│  │        │     ├─ compressor.cpython-312.pyc
│  │        │     ├─ disk.cpython-312.pyc
│  │        │     ├─ executor.cpython-312.pyc
│  │        │     ├─ func_inspect.cpython-312.pyc
│  │        │     ├─ hashing.cpython-312.pyc
│  │        │     ├─ logger.cpython-312.pyc
│  │        │     ├─ memory.cpython-312.pyc
│  │        │     ├─ numpy_pickle.cpython-312.pyc
│  │        │     ├─ numpy_pickle_compat.cpython-312.pyc
│  │        │     ├─ numpy_pickle_utils.cpython-312.pyc
│  │        │     ├─ parallel.cpython-312.pyc
│  │        │     ├─ pool.cpython-312.pyc
│  │        │     ├─ testing.cpython-312.pyc
│  │        │     ├─ _cloudpickle_wrapper.cpython-312.pyc
│  │        │     ├─ _dask.cpython-312.pyc
│  │        │     ├─ _memmapping_reducer.cpython-312.pyc
│  │        │     ├─ _multiprocessing_helpers.cpython-312.pyc
│  │        │     ├─ _parallel_backends.cpython-312.pyc
│  │        │     ├─ _store_backends.cpython-312.pyc
│  │        │     ├─ _utils.cpython-312.pyc
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ joblib-1.5.1.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ licenses
│  │        │  │  └─ LICENSE.txt
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ REQUESTED
│  │        │  ├─ top_level.txt
│  │        │  └─ WHEEL
│  │        ├─ markdown_it
│  │        │  ├─ cli
│  │        │  │  ├─ parse.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ parse.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ common
│  │        │  │  ├─ entities.py
│  │        │  │  ├─ html_blocks.py
│  │        │  │  ├─ html_re.py
│  │        │  │  ├─ normalize_url.py
│  │        │  │  ├─ utils.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ entities.cpython-312.pyc
│  │        │  │     ├─ html_blocks.cpython-312.pyc
│  │        │  │     ├─ html_re.cpython-312.pyc
│  │        │  │     ├─ normalize_url.cpython-312.pyc
│  │        │  │     ├─ utils.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ helpers
│  │        │  │  ├─ parse_link_destination.py
│  │        │  │  ├─ parse_link_label.py
│  │        │  │  ├─ parse_link_title.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ parse_link_destination.cpython-312.pyc
│  │        │  │     ├─ parse_link_label.cpython-312.pyc
│  │        │  │     ├─ parse_link_title.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ main.py
│  │        │  ├─ parser_block.py
│  │        │  ├─ parser_core.py
│  │        │  ├─ parser_inline.py
│  │        │  ├─ port.yaml
│  │        │  ├─ presets
│  │        │  │  ├─ commonmark.py
│  │        │  │  ├─ default.py
│  │        │  │  ├─ zero.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ commonmark.cpython-312.pyc
│  │        │  │     ├─ default.cpython-312.pyc
│  │        │  │     ├─ zero.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ py.typed
│  │        │  ├─ renderer.py
│  │        │  ├─ ruler.py
│  │        │  ├─ rules_block
│  │        │  │  ├─ blockquote.py
│  │        │  │  ├─ code.py
│  │        │  │  ├─ fence.py
│  │        │  │  ├─ heading.py
│  │        │  │  ├─ hr.py
│  │        │  │  ├─ html_block.py
│  │        │  │  ├─ lheading.py
│  │        │  │  ├─ list.py
│  │        │  │  ├─ paragraph.py
│  │        │  │  ├─ reference.py
│  │        │  │  ├─ state_block.py
│  │        │  │  ├─ table.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ blockquote.cpython-312.pyc
│  │        │  │     ├─ code.cpython-312.pyc
│  │        │  │     ├─ fence.cpython-312.pyc
│  │        │  │     ├─ heading.cpython-312.pyc
│  │        │  │     ├─ hr.cpython-312.pyc
│  │        │  │     ├─ html_block.cpython-312.pyc
│  │        │  │     ├─ lheading.cpython-312.pyc
│  │        │  │     ├─ list.cpython-312.pyc
│  │        │  │     ├─ paragraph.cpython-312.pyc
│  │        │  │     ├─ reference.cpython-312.pyc
│  │        │  │     ├─ state_block.cpython-312.pyc
│  │        │  │     ├─ table.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ rules_core
│  │        │  │  ├─ block.py
│  │        │  │  ├─ inline.py
│  │        │  │  ├─ linkify.py
│  │        │  │  ├─ normalize.py
│  │        │  │  ├─ replacements.py
│  │        │  │  ├─ smartquotes.py
│  │        │  │  ├─ state_core.py
│  │        │  │  ├─ text_join.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ block.cpython-312.pyc
│  │        │  │     ├─ inline.cpython-312.pyc
│  │        │  │     ├─ linkify.cpython-312.pyc
│  │        │  │     ├─ normalize.cpython-312.pyc
│  │        │  │     ├─ replacements.cpython-312.pyc
│  │        │  │     ├─ smartquotes.cpython-312.pyc
│  │        │  │     ├─ state_core.cpython-312.pyc
│  │        │  │     ├─ text_join.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ rules_inline
│  │        │  │  ├─ autolink.py
│  │        │  │  ├─ backticks.py
│  │        │  │  ├─ balance_pairs.py
│  │        │  │  ├─ emphasis.py
│  │        │  │  ├─ entity.py
│  │        │  │  ├─ escape.py
│  │        │  │  ├─ fragments_join.py
│  │        │  │  ├─ html_inline.py
│  │        │  │  ├─ image.py
│  │        │  │  ├─ link.py
│  │        │  │  ├─ linkify.py
│  │        │  │  ├─ newline.py
│  │        │  │  ├─ state_inline.py
│  │        │  │  ├─ strikethrough.py
│  │        │  │  ├─ text.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ autolink.cpython-312.pyc
│  │        │  │     ├─ backticks.cpython-312.pyc
│  │        │  │     ├─ balance_pairs.cpython-312.pyc
│  │        │  │     ├─ emphasis.cpython-312.pyc
│  │        │  │     ├─ entity.cpython-312.pyc
│  │        │  │     ├─ escape.cpython-312.pyc
│  │        │  │     ├─ fragments_join.cpython-312.pyc
│  │        │  │     ├─ html_inline.cpython-312.pyc
│  │        │  │     ├─ image.cpython-312.pyc
│  │        │  │     ├─ link.cpython-312.pyc
│  │        │  │     ├─ linkify.cpython-312.pyc
│  │        │  │     ├─ newline.cpython-312.pyc
│  │        │  │     ├─ state_inline.cpython-312.pyc
│  │        │  │     ├─ strikethrough.cpython-312.pyc
│  │        │  │     ├─ text.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ token.py
│  │        │  ├─ tree.py
│  │        │  ├─ utils.py
│  │        │  ├─ _compat.py
│  │        │  ├─ _punycode.py
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     ├─ main.cpython-312.pyc
│  │        │     ├─ parser_block.cpython-312.pyc
│  │        │     ├─ parser_core.cpython-312.pyc
│  │        │     ├─ parser_inline.cpython-312.pyc
│  │        │     ├─ renderer.cpython-312.pyc
│  │        │     ├─ ruler.cpython-312.pyc
│  │        │     ├─ token.cpython-312.pyc
│  │        │     ├─ tree.cpython-312.pyc
│  │        │     ├─ utils.cpython-312.pyc
│  │        │     ├─ _compat.cpython-312.pyc
│  │        │     ├─ _punycode.cpython-312.pyc
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ markdown_it_py-3.0.0.dist-info
│  │        │  ├─ entry_points.txt
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE
│  │        │  ├─ LICENSE.markdown-it
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  └─ WHEEL
│  │        ├─ markupsafe
│  │        │  ├─ py.typed
│  │        │  ├─ _native.py
│  │        │  ├─ _speedups.c
│  │        │  ├─ _speedups.cpython-312-darwin.so
│  │        │  ├─ _speedups.pyi
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     ├─ _native.cpython-312.pyc
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ MarkupSafe-3.0.2.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE.txt
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ top_level.txt
│  │        │  └─ WHEEL
│  │        ├─ mdurl
│  │        │  ├─ py.typed
│  │        │  ├─ _decode.py
│  │        │  ├─ _encode.py
│  │        │  ├─ _format.py
│  │        │  ├─ _parse.py
│  │        │  ├─ _url.py
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     ├─ _decode.cpython-312.pyc
│  │        │     ├─ _encode.cpython-312.pyc
│  │        │     ├─ _format.cpython-312.pyc
│  │        │     ├─ _parse.cpython-312.pyc
│  │        │     ├─ _url.cpython-312.pyc
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ mdurl-0.1.2.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  └─ WHEEL
│  │        ├─ multipart
│  │        │  ├─ decoders.py
│  │        │  ├─ exceptions.py
│  │        │  ├─ multipart.py
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     ├─ decoders.cpython-312.pyc
│  │        │     ├─ exceptions.cpython-312.pyc
│  │        │     ├─ multipart.cpython-312.pyc
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ numpy
│  │        │  ├─ char
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ __init__.pyi
│  │        │  │  └─ __pycache__
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ compat
│  │        │  │  ├─ py3k.py
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ py3k.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ conftest.py
│  │        │  ├─ core
│  │        │  │  ├─ arrayprint.py
│  │        │  │  ├─ defchararray.py
│  │        │  │  ├─ einsumfunc.py
│  │        │  │  ├─ fromnumeric.py
│  │        │  │  ├─ function_base.py
│  │        │  │  ├─ getlimits.py
│  │        │  │  ├─ multiarray.py
│  │        │  │  ├─ numeric.py
│  │        │  │  ├─ numerictypes.py
│  │        │  │  ├─ overrides.py
│  │        │  │  ├─ overrides.pyi
│  │        │  │  ├─ records.py
│  │        │  │  ├─ shape_base.py
│  │        │  │  ├─ umath.py
│  │        │  │  ├─ _dtype.py
│  │        │  │  ├─ _dtype.pyi
│  │        │  │  ├─ _dtype_ctypes.py
│  │        │  │  ├─ _dtype_ctypes.pyi
│  │        │  │  ├─ _internal.py
│  │        │  │  ├─ _multiarray_umath.py
│  │        │  │  ├─ _utils.py
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ __init__.pyi
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ arrayprint.cpython-312.pyc
│  │        │  │     ├─ defchararray.cpython-312.pyc
│  │        │  │     ├─ einsumfunc.cpython-312.pyc
│  │        │  │     ├─ fromnumeric.cpython-312.pyc
│  │        │  │     ├─ function_base.cpython-312.pyc
│  │        │  │     ├─ getlimits.cpython-312.pyc
│  │        │  │     ├─ multiarray.cpython-312.pyc
│  │        │  │     ├─ numeric.cpython-312.pyc
│  │        │  │     ├─ numerictypes.cpython-312.pyc
│  │        │  │     ├─ overrides.cpython-312.pyc
│  │        │  │     ├─ records.cpython-312.pyc
│  │        │  │     ├─ shape_base.cpython-312.pyc
│  │        │  │     ├─ umath.cpython-312.pyc
│  │        │  │     ├─ _dtype.cpython-312.pyc
│  │        │  │     ├─ _dtype_ctypes.cpython-312.pyc
│  │        │  │     ├─ _internal.cpython-312.pyc
│  │        │  │     ├─ _multiarray_umath.cpython-312.pyc
│  │        │  │     ├─ _utils.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ ctypeslib.py
│  │        │  ├─ ctypeslib.pyi
│  │        │  ├─ doc
│  │        │  │  ├─ ufuncs.py
│  │        │  │  └─ __pycache__
│  │        │  │     └─ ufuncs.cpython-312.pyc
│  │        │  ├─ dtypes.py
│  │        │  ├─ dtypes.pyi
│  │        │  ├─ exceptions.py
│  │        │  ├─ exceptions.pyi
│  │        │  ├─ f2py
│  │        │  │  ├─ auxfuncs.py
│  │        │  │  ├─ capi_maps.py
│  │        │  │  ├─ cb_rules.py
│  │        │  │  ├─ cfuncs.py
│  │        │  │  ├─ common_rules.py
│  │        │  │  ├─ crackfortran.py
│  │        │  │  ├─ diagnose.py
│  │        │  │  ├─ f2py2e.py
│  │        │  │  ├─ f90mod_rules.py
│  │        │  │  ├─ func2subr.py
│  │        │  │  ├─ rules.py
│  │        │  │  ├─ setup.cfg
│  │        │  │  ├─ src
│  │        │  │  │  ├─ fortranobject.c
│  │        │  │  │  └─ fortranobject.h
│  │        │  │  ├─ symbolic.py
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ src
│  │        │  │  │  │  ├─ abstract_interface
│  │        │  │  │  │  │  ├─ foo.f90
│  │        │  │  │  │  │  └─ gh18403_mod.f90
│  │        │  │  │  │  ├─ array_from_pyobj
│  │        │  │  │  │  │  └─ wrapmodule.c
│  │        │  │  │  │  ├─ assumed_shape
│  │        │  │  │  │  │  ├─ .f2py_f2cmap
│  │        │  │  │  │  │  ├─ foo_free.f90
│  │        │  │  │  │  │  ├─ foo_mod.f90
│  │        │  │  │  │  │  ├─ foo_use.f90
│  │        │  │  │  │  │  └─ precision.f90
│  │        │  │  │  │  ├─ block_docstring
│  │        │  │  │  │  │  └─ foo.f
│  │        │  │  │  │  ├─ callback
│  │        │  │  │  │  │  ├─ foo.f
│  │        │  │  │  │  │  ├─ gh17797.f90
│  │        │  │  │  │  │  ├─ gh18335.f90
│  │        │  │  │  │  │  ├─ gh25211.f
│  │        │  │  │  │  │  ├─ gh25211.pyf
│  │        │  │  │  │  │  └─ gh26681.f90
│  │        │  │  │  │  ├─ cli
│  │        │  │  │  │  │  ├─ gh_22819.pyf
│  │        │  │  │  │  │  ├─ hi77.f
│  │        │  │  │  │  │  └─ hiworld.f90
│  │        │  │  │  │  ├─ common
│  │        │  │  │  │  │  ├─ block.f
│  │        │  │  │  │  │  └─ gh19161.f90
│  │        │  │  │  │  ├─ crackfortran
│  │        │  │  │  │  │  ├─ accesstype.f90
│  │        │  │  │  │  │  ├─ common_with_division.f
│  │        │  │  │  │  │  ├─ data_common.f
│  │        │  │  │  │  │  ├─ data_multiplier.f
│  │        │  │  │  │  │  ├─ data_stmts.f90
│  │        │  │  │  │  │  ├─ data_with_comments.f
│  │        │  │  │  │  │  ├─ foo_deps.f90
│  │        │  │  │  │  │  ├─ gh15035.f
│  │        │  │  │  │  │  ├─ gh17859.f
│  │        │  │  │  │  │  ├─ gh22648.pyf
│  │        │  │  │  │  │  ├─ gh23533.f
│  │        │  │  │  │  │  ├─ gh23598.f90
│  │        │  │  │  │  │  ├─ gh23598Warn.f90
│  │        │  │  │  │  │  ├─ gh23879.f90
│  │        │  │  │  │  │  ├─ gh27697.f90
│  │        │  │  │  │  │  ├─ gh2848.f90
│  │        │  │  │  │  │  ├─ operators.f90
│  │        │  │  │  │  │  ├─ privatemod.f90
│  │        │  │  │  │  │  ├─ publicmod.f90
│  │        │  │  │  │  │  ├─ pubprivmod.f90
│  │        │  │  │  │  │  └─ unicode_comment.f90
│  │        │  │  │  │  ├─ f2cmap
│  │        │  │  │  │  │  ├─ .f2py_f2cmap
│  │        │  │  │  │  │  └─ isoFortranEnvMap.f90
│  │        │  │  │  │  ├─ isocintrin
│  │        │  │  │  │  │  └─ isoCtests.f90
│  │        │  │  │  │  ├─ kind
│  │        │  │  │  │  │  └─ foo.f90
│  │        │  │  │  │  ├─ mixed
│  │        │  │  │  │  │  ├─ foo.f
│  │        │  │  │  │  │  ├─ foo_fixed.f90
│  │        │  │  │  │  │  └─ foo_free.f90
│  │        │  │  │  │  ├─ modules
│  │        │  │  │  │  │  ├─ gh25337
│  │        │  │  │  │  │  │  ├─ data.f90
│  │        │  │  │  │  │  │  └─ use_data.f90
│  │        │  │  │  │  │  ├─ gh26920
│  │        │  │  │  │  │  │  ├─ two_mods_with_no_public_entities.f90
│  │        │  │  │  │  │  │  └─ two_mods_with_one_public_routine.f90
│  │        │  │  │  │  │  ├─ module_data_docstring.f90
│  │        │  │  │  │  │  └─ use_modules.f90
│  │        │  │  │  │  ├─ negative_bounds
│  │        │  │  │  │  │  └─ issue_20853.f90
│  │        │  │  │  │  ├─ parameter
│  │        │  │  │  │  │  ├─ constant_array.f90
│  │        │  │  │  │  │  ├─ constant_both.f90
│  │        │  │  │  │  │  ├─ constant_compound.f90
│  │        │  │  │  │  │  ├─ constant_integer.f90
│  │        │  │  │  │  │  ├─ constant_non_compound.f90
│  │        │  │  │  │  │  └─ constant_real.f90
│  │        │  │  │  │  ├─ quoted_character
│  │        │  │  │  │  │  └─ foo.f
│  │        │  │  │  │  ├─ regression
│  │        │  │  │  │  │  ├─ AB.inc
│  │        │  │  │  │  │  ├─ assignOnlyModule.f90
│  │        │  │  │  │  │  ├─ datonly.f90
│  │        │  │  │  │  │  ├─ f77comments.f
│  │        │  │  │  │  │  ├─ f77fixedform.f95
│  │        │  │  │  │  │  ├─ f90continuation.f90
│  │        │  │  │  │  │  ├─ incfile.f90
│  │        │  │  │  │  │  ├─ inout.f90
│  │        │  │  │  │  │  └─ lower_f2py_fortran.f90
│  │        │  │  │  │  ├─ return_character
│  │        │  │  │  │  │  ├─ foo77.f
│  │        │  │  │  │  │  └─ foo90.f90
│  │        │  │  │  │  ├─ return_complex
│  │        │  │  │  │  │  ├─ foo77.f
│  │        │  │  │  │  │  └─ foo90.f90
│  │        │  │  │  │  ├─ return_integer
│  │        │  │  │  │  │  ├─ foo77.f
│  │        │  │  │  │  │  └─ foo90.f90
│  │        │  │  │  │  ├─ return_logical
│  │        │  │  │  │  │  ├─ foo77.f
│  │        │  │  │  │  │  └─ foo90.f90
│  │        │  │  │  │  ├─ return_real
│  │        │  │  │  │  │  ├─ foo77.f
│  │        │  │  │  │  │  └─ foo90.f90
│  │        │  │  │  │  ├─ routines
│  │        │  │  │  │  │  ├─ funcfortranname.f
│  │        │  │  │  │  │  ├─ funcfortranname.pyf
│  │        │  │  │  │  │  ├─ subrout.f
│  │        │  │  │  │  │  └─ subrout.pyf
│  │        │  │  │  │  ├─ size
│  │        │  │  │  │  │  └─ foo.f90
│  │        │  │  │  │  ├─ string
│  │        │  │  │  │  │  ├─ char.f90
│  │        │  │  │  │  │  ├─ fixed_string.f90
│  │        │  │  │  │  │  ├─ gh24008.f
│  │        │  │  │  │  │  ├─ gh24662.f90
│  │        │  │  │  │  │  ├─ gh25286.f90
│  │        │  │  │  │  │  ├─ gh25286.pyf
│  │        │  │  │  │  │  ├─ gh25286_bc.pyf
│  │        │  │  │  │  │  ├─ scalar_string.f90
│  │        │  │  │  │  │  └─ string.f
│  │        │  │  │  │  └─ value_attrspec
│  │        │  │  │  │     └─ gh21665.f90
│  │        │  │  │  ├─ test_abstract_interface.py
│  │        │  │  │  ├─ test_array_from_pyobj.py
│  │        │  │  │  ├─ test_assumed_shape.py
│  │        │  │  │  ├─ test_block_docstring.py
│  │        │  │  │  ├─ test_callback.py
│  │        │  │  │  ├─ test_character.py
│  │        │  │  │  ├─ test_common.py
│  │        │  │  │  ├─ test_crackfortran.py
│  │        │  │  │  ├─ test_data.py
│  │        │  │  │  ├─ test_docs.py
│  │        │  │  │  ├─ test_f2cmap.py
│  │        │  │  │  ├─ test_f2py2e.py
│  │        │  │  │  ├─ test_isoc.py
│  │        │  │  │  ├─ test_kind.py
│  │        │  │  │  ├─ test_mixed.py
│  │        │  │  │  ├─ test_modules.py
│  │        │  │  │  ├─ test_parameter.py
│  │        │  │  │  ├─ test_pyf_src.py
│  │        │  │  │  ├─ test_quoted_character.py
│  │        │  │  │  ├─ test_regression.py
│  │        │  │  │  ├─ test_return_character.py
│  │        │  │  │  ├─ test_return_complex.py
│  │        │  │  │  ├─ test_return_integer.py
│  │        │  │  │  ├─ test_return_logical.py
│  │        │  │  │  ├─ test_return_real.py
│  │        │  │  │  ├─ test_routines.py
│  │        │  │  │  ├─ test_semicolon_split.py
│  │        │  │  │  ├─ test_size.py
│  │        │  │  │  ├─ test_string.py
│  │        │  │  │  ├─ test_symbolic.py
│  │        │  │  │  ├─ test_value_attrspec.py
│  │        │  │  │  ├─ util.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_abstract_interface.cpython-312.pyc
│  │        │  │  │     ├─ test_array_from_pyobj.cpython-312.pyc
│  │        │  │  │     ├─ test_assumed_shape.cpython-312.pyc
│  │        │  │  │     ├─ test_block_docstring.cpython-312.pyc
│  │        │  │  │     ├─ test_callback.cpython-312.pyc
│  │        │  │  │     ├─ test_character.cpython-312.pyc
│  │        │  │  │     ├─ test_common.cpython-312.pyc
│  │        │  │  │     ├─ test_crackfortran.cpython-312.pyc
│  │        │  │  │     ├─ test_data.cpython-312.pyc
│  │        │  │  │     ├─ test_docs.cpython-312.pyc
│  │        │  │  │     ├─ test_f2cmap.cpython-312.pyc
│  │        │  │  │     ├─ test_f2py2e.cpython-312.pyc
│  │        │  │  │     ├─ test_isoc.cpython-312.pyc
│  │        │  │  │     ├─ test_kind.cpython-312.pyc
│  │        │  │  │     ├─ test_mixed.cpython-312.pyc
│  │        │  │  │     ├─ test_modules.cpython-312.pyc
│  │        │  │  │     ├─ test_parameter.cpython-312.pyc
│  │        │  │  │     ├─ test_pyf_src.cpython-312.pyc
│  │        │  │  │     ├─ test_quoted_character.cpython-312.pyc
│  │        │  │  │     ├─ test_regression.cpython-312.pyc
│  │        │  │  │     ├─ test_return_character.cpython-312.pyc
│  │        │  │  │     ├─ test_return_complex.cpython-312.pyc
│  │        │  │  │     ├─ test_return_integer.cpython-312.pyc
│  │        │  │  │     ├─ test_return_logical.cpython-312.pyc
│  │        │  │  │     ├─ test_return_real.cpython-312.pyc
│  │        │  │  │     ├─ test_routines.cpython-312.pyc
│  │        │  │  │     ├─ test_semicolon_split.cpython-312.pyc
│  │        │  │  │     ├─ test_size.cpython-312.pyc
│  │        │  │  │     ├─ test_string.cpython-312.pyc
│  │        │  │  │     ├─ test_symbolic.cpython-312.pyc
│  │        │  │  │     ├─ test_value_attrspec.cpython-312.pyc
│  │        │  │  │     ├─ util.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ use_rules.py
│  │        │  │  ├─ _backends
│  │        │  │  │  ├─ meson.build.template
│  │        │  │  │  ├─ _backend.py
│  │        │  │  │  ├─ _distutils.py
│  │        │  │  │  ├─ _meson.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ _backend.cpython-312.pyc
│  │        │  │  │     ├─ _distutils.cpython-312.pyc
│  │        │  │  │     ├─ _meson.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _isocbind.py
│  │        │  │  ├─ _src_pyf.py
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ __init__.pyi
│  │        │  │  ├─ __main__.py
│  │        │  │  ├─ __pycache__
│  │        │  │  │  ├─ auxfuncs.cpython-312.pyc
│  │        │  │  │  ├─ capi_maps.cpython-312.pyc
│  │        │  │  │  ├─ cb_rules.cpython-312.pyc
│  │        │  │  │  ├─ cfuncs.cpython-312.pyc
│  │        │  │  │  ├─ common_rules.cpython-312.pyc
│  │        │  │  │  ├─ crackfortran.cpython-312.pyc
│  │        │  │  │  ├─ diagnose.cpython-312.pyc
│  │        │  │  │  ├─ f2py2e.cpython-312.pyc
│  │        │  │  │  ├─ f90mod_rules.cpython-312.pyc
│  │        │  │  │  ├─ func2subr.cpython-312.pyc
│  │        │  │  │  ├─ rules.cpython-312.pyc
│  │        │  │  │  ├─ symbolic.cpython-312.pyc
│  │        │  │  │  ├─ use_rules.cpython-312.pyc
│  │        │  │  │  ├─ _isocbind.cpython-312.pyc
│  │        │  │  │  ├─ _src_pyf.cpython-312.pyc
│  │        │  │  │  ├─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ __main__.cpython-312.pyc
│  │        │  │  │  └─ __version__.cpython-312.pyc
│  │        │  │  └─ __version__.py
│  │        │  ├─ fft
│  │        │  │  ├─ helper.py
│  │        │  │  ├─ helper.pyi
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ test_helper.py
│  │        │  │  │  ├─ test_pocketfft.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_helper.cpython-312.pyc
│  │        │  │  │     ├─ test_pocketfft.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _helper.py
│  │        │  │  ├─ _helper.pyi
│  │        │  │  ├─ _pocketfft.py
│  │        │  │  ├─ _pocketfft.pyi
│  │        │  │  ├─ _pocketfft_umath.cpython-312-darwin.so
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ __init__.pyi
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ helper.cpython-312.pyc
│  │        │  │     ├─ _helper.cpython-312.pyc
│  │        │  │     ├─ _pocketfft.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ lib
│  │        │  │  ├─ array_utils.py
│  │        │  │  ├─ array_utils.pyi
│  │        │  │  ├─ format.py
│  │        │  │  ├─ format.pyi
│  │        │  │  ├─ introspect.py
│  │        │  │  ├─ introspect.pyi
│  │        │  │  ├─ mixins.py
│  │        │  │  ├─ mixins.pyi
│  │        │  │  ├─ npyio.py
│  │        │  │  ├─ npyio.pyi
│  │        │  │  ├─ recfunctions.py
│  │        │  │  ├─ recfunctions.pyi
│  │        │  │  ├─ scimath.py
│  │        │  │  ├─ scimath.pyi
│  │        │  │  ├─ stride_tricks.py
│  │        │  │  ├─ stride_tricks.pyi
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ data
│  │        │  │  │  │  ├─ py2-np0-objarr.npy
│  │        │  │  │  │  ├─ py2-objarr.npy
│  │        │  │  │  │  ├─ py2-objarr.npz
│  │        │  │  │  │  ├─ py3-objarr.npy
│  │        │  │  │  │  ├─ py3-objarr.npz
│  │        │  │  │  │  ├─ python3.npy
│  │        │  │  │  │  └─ win64python2.npy
│  │        │  │  │  ├─ test_arraypad.py
│  │        │  │  │  ├─ test_arraysetops.py
│  │        │  │  │  ├─ test_arrayterator.py
│  │        │  │  │  ├─ test_array_utils.py
│  │        │  │  │  ├─ test_format.py
│  │        │  │  │  ├─ test_function_base.py
│  │        │  │  │  ├─ test_histograms.py
│  │        │  │  │  ├─ test_index_tricks.py
│  │        │  │  │  ├─ test_io.py
│  │        │  │  │  ├─ test_loadtxt.py
│  │        │  │  │  ├─ test_mixins.py
│  │        │  │  │  ├─ test_nanfunctions.py
│  │        │  │  │  ├─ test_packbits.py
│  │        │  │  │  ├─ test_polynomial.py
│  │        │  │  │  ├─ test_recfunctions.py
│  │        │  │  │  ├─ test_regression.py
│  │        │  │  │  ├─ test_shape_base.py
│  │        │  │  │  ├─ test_stride_tricks.py
│  │        │  │  │  ├─ test_twodim_base.py
│  │        │  │  │  ├─ test_type_check.py
│  │        │  │  │  ├─ test_ufunclike.py
│  │        │  │  │  ├─ test_utils.py
│  │        │  │  │  ├─ test__datasource.py
│  │        │  │  │  ├─ test__iotools.py
│  │        │  │  │  ├─ test__version.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_arraypad.cpython-312.pyc
│  │        │  │  │     ├─ test_arraysetops.cpython-312.pyc
│  │        │  │  │     ├─ test_arrayterator.cpython-312.pyc
│  │        │  │  │     ├─ test_array_utils.cpython-312.pyc
│  │        │  │  │     ├─ test_format.cpython-312.pyc
│  │        │  │  │     ├─ test_function_base.cpython-312.pyc
│  │        │  │  │     ├─ test_histograms.cpython-312.pyc
│  │        │  │  │     ├─ test_index_tricks.cpython-312.pyc
│  │        │  │  │     ├─ test_io.cpython-312.pyc
│  │        │  │  │     ├─ test_loadtxt.cpython-312.pyc
│  │        │  │  │     ├─ test_mixins.cpython-312.pyc
│  │        │  │  │     ├─ test_nanfunctions.cpython-312.pyc
│  │        │  │  │     ├─ test_packbits.cpython-312.pyc
│  │        │  │  │     ├─ test_polynomial.cpython-312.pyc
│  │        │  │  │     ├─ test_recfunctions.cpython-312.pyc
│  │        │  │  │     ├─ test_regression.cpython-312.pyc
│  │        │  │  │     ├─ test_shape_base.cpython-312.pyc
│  │        │  │  │     ├─ test_stride_tricks.cpython-312.pyc
│  │        │  │  │     ├─ test_twodim_base.cpython-312.pyc
│  │        │  │  │     ├─ test_type_check.cpython-312.pyc
│  │        │  │  │     ├─ test_ufunclike.cpython-312.pyc
│  │        │  │  │     ├─ test_utils.cpython-312.pyc
│  │        │  │  │     ├─ test__datasource.cpython-312.pyc
│  │        │  │  │     ├─ test__iotools.cpython-312.pyc
│  │        │  │  │     ├─ test__version.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ user_array.py
│  │        │  │  ├─ user_array.pyi
│  │        │  │  ├─ _arraypad_impl.py
│  │        │  │  ├─ _arraypad_impl.pyi
│  │        │  │  ├─ _arraysetops_impl.py
│  │        │  │  ├─ _arraysetops_impl.pyi
│  │        │  │  ├─ _arrayterator_impl.py
│  │        │  │  ├─ _arrayterator_impl.pyi
│  │        │  │  ├─ _array_utils_impl.py
│  │        │  │  ├─ _array_utils_impl.pyi
│  │        │  │  ├─ _datasource.py
│  │        │  │  ├─ _datasource.pyi
│  │        │  │  ├─ _function_base_impl.py
│  │        │  │  ├─ _function_base_impl.pyi
│  │        │  │  ├─ _histograms_impl.py
│  │        │  │  ├─ _histograms_impl.pyi
│  │        │  │  ├─ _index_tricks_impl.py
│  │        │  │  ├─ _index_tricks_impl.pyi
│  │        │  │  ├─ _iotools.py
│  │        │  │  ├─ _iotools.pyi
│  │        │  │  ├─ _nanfunctions_impl.py
│  │        │  │  ├─ _nanfunctions_impl.pyi
│  │        │  │  ├─ _npyio_impl.py
│  │        │  │  ├─ _npyio_impl.pyi
│  │        │  │  ├─ _polynomial_impl.py
│  │        │  │  ├─ _polynomial_impl.pyi
│  │        │  │  ├─ _scimath_impl.py
│  │        │  │  ├─ _scimath_impl.pyi
│  │        │  │  ├─ _shape_base_impl.py
│  │        │  │  ├─ _shape_base_impl.pyi
│  │        │  │  ├─ _stride_tricks_impl.py
│  │        │  │  ├─ _stride_tricks_impl.pyi
│  │        │  │  ├─ _twodim_base_impl.py
│  │        │  │  ├─ _twodim_base_impl.pyi
│  │        │  │  ├─ _type_check_impl.py
│  │        │  │  ├─ _type_check_impl.pyi
│  │        │  │  ├─ _ufunclike_impl.py
│  │        │  │  ├─ _ufunclike_impl.pyi
│  │        │  │  ├─ _user_array_impl.py
│  │        │  │  ├─ _user_array_impl.pyi
│  │        │  │  ├─ _utils_impl.py
│  │        │  │  ├─ _utils_impl.pyi
│  │        │  │  ├─ _version.py
│  │        │  │  ├─ _version.pyi
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ __init__.pyi
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ array_utils.cpython-312.pyc
│  │        │  │     ├─ format.cpython-312.pyc
│  │        │  │     ├─ introspect.cpython-312.pyc
│  │        │  │     ├─ mixins.cpython-312.pyc
│  │        │  │     ├─ npyio.cpython-312.pyc
│  │        │  │     ├─ recfunctions.cpython-312.pyc
│  │        │  │     ├─ scimath.cpython-312.pyc
│  │        │  │     ├─ stride_tricks.cpython-312.pyc
│  │        │  │     ├─ user_array.cpython-312.pyc
│  │        │  │     ├─ _arraypad_impl.cpython-312.pyc
│  │        │  │     ├─ _arraysetops_impl.cpython-312.pyc
│  │        │  │     ├─ _arrayterator_impl.cpython-312.pyc
│  │        │  │     ├─ _array_utils_impl.cpython-312.pyc
│  │        │  │     ├─ _datasource.cpython-312.pyc
│  │        │  │     ├─ _function_base_impl.cpython-312.pyc
│  │        │  │     ├─ _histograms_impl.cpython-312.pyc
│  │        │  │     ├─ _index_tricks_impl.cpython-312.pyc
│  │        │  │     ├─ _iotools.cpython-312.pyc
│  │        │  │     ├─ _nanfunctions_impl.cpython-312.pyc
│  │        │  │     ├─ _npyio_impl.cpython-312.pyc
│  │        │  │     ├─ _polynomial_impl.cpython-312.pyc
│  │        │  │     ├─ _scimath_impl.cpython-312.pyc
│  │        │  │     ├─ _shape_base_impl.cpython-312.pyc
│  │        │  │     ├─ _stride_tricks_impl.cpython-312.pyc
│  │        │  │     ├─ _twodim_base_impl.cpython-312.pyc
│  │        │  │     ├─ _type_check_impl.cpython-312.pyc
│  │        │  │     ├─ _ufunclike_impl.cpython-312.pyc
│  │        │  │     ├─ _user_array_impl.cpython-312.pyc
│  │        │  │     ├─ _utils_impl.cpython-312.pyc
│  │        │  │     ├─ _version.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ linalg
│  │        │  │  ├─ lapack_lite.cpython-312-darwin.so
│  │        │  │  ├─ lapack_lite.pyi
│  │        │  │  ├─ linalg.py
│  │        │  │  ├─ linalg.pyi
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ test_deprecations.py
│  │        │  │  │  ├─ test_linalg.py
│  │        │  │  │  ├─ test_regression.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_deprecations.cpython-312.pyc
│  │        │  │  │     ├─ test_linalg.cpython-312.pyc
│  │        │  │  │     ├─ test_regression.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _linalg.py
│  │        │  │  ├─ _linalg.pyi
│  │        │  │  ├─ _umath_linalg.cpython-312-darwin.so
│  │        │  │  ├─ _umath_linalg.pyi
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ __init__.pyi
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ linalg.cpython-312.pyc
│  │        │  │     ├─ _linalg.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ ma
│  │        │  │  ├─ API_CHANGES.txt
│  │        │  │  ├─ core.py
│  │        │  │  ├─ core.pyi
│  │        │  │  ├─ extras.py
│  │        │  │  ├─ extras.pyi
│  │        │  │  ├─ LICENSE
│  │        │  │  ├─ mrecords.py
│  │        │  │  ├─ mrecords.pyi
│  │        │  │  ├─ README.rst
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ test_arrayobject.py
│  │        │  │  │  ├─ test_core.py
│  │        │  │  │  ├─ test_deprecations.py
│  │        │  │  │  ├─ test_extras.py
│  │        │  │  │  ├─ test_mrecords.py
│  │        │  │  │  ├─ test_old_ma.py
│  │        │  │  │  ├─ test_regression.py
│  │        │  │  │  ├─ test_subclassing.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_arrayobject.cpython-312.pyc
│  │        │  │  │     ├─ test_core.cpython-312.pyc
│  │        │  │  │     ├─ test_deprecations.cpython-312.pyc
│  │        │  │  │     ├─ test_extras.cpython-312.pyc
│  │        │  │  │     ├─ test_mrecords.cpython-312.pyc
│  │        │  │  │     ├─ test_old_ma.cpython-312.pyc
│  │        │  │  │     ├─ test_regression.cpython-312.pyc
│  │        │  │  │     ├─ test_subclassing.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ testutils.py
│  │        │  │  ├─ timer_comparison.py
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ __init__.pyi
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ core.cpython-312.pyc
│  │        │  │     ├─ extras.cpython-312.pyc
│  │        │  │     ├─ mrecords.cpython-312.pyc
│  │        │  │     ├─ testutils.cpython-312.pyc
│  │        │  │     ├─ timer_comparison.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ matlib.py
│  │        │  ├─ matlib.pyi
│  │        │  ├─ matrixlib
│  │        │  │  ├─ defmatrix.py
│  │        │  │  ├─ defmatrix.pyi
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ test_defmatrix.py
│  │        │  │  │  ├─ test_interaction.py
│  │        │  │  │  ├─ test_masked_matrix.py
│  │        │  │  │  ├─ test_matrix_linalg.py
│  │        │  │  │  ├─ test_multiarray.py
│  │        │  │  │  ├─ test_numeric.py
│  │        │  │  │  ├─ test_regression.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_defmatrix.cpython-312.pyc
│  │        │  │  │     ├─ test_interaction.cpython-312.pyc
│  │        │  │  │     ├─ test_masked_matrix.cpython-312.pyc
│  │        │  │  │     ├─ test_matrix_linalg.cpython-312.pyc
│  │        │  │  │     ├─ test_multiarray.cpython-312.pyc
│  │        │  │  │     ├─ test_numeric.cpython-312.pyc
│  │        │  │  │     ├─ test_regression.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ __init__.pyi
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ defmatrix.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ polynomial
│  │        │  │  ├─ chebyshev.py
│  │        │  │  ├─ chebyshev.pyi
│  │        │  │  ├─ hermite.py
│  │        │  │  ├─ hermite.pyi
│  │        │  │  ├─ hermite_e.py
│  │        │  │  ├─ hermite_e.pyi
│  │        │  │  ├─ laguerre.py
│  │        │  │  ├─ laguerre.pyi
│  │        │  │  ├─ legendre.py
│  │        │  │  ├─ legendre.pyi
│  │        │  │  ├─ polynomial.py
│  │        │  │  ├─ polynomial.pyi
│  │        │  │  ├─ polyutils.py
│  │        │  │  ├─ polyutils.pyi
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ test_chebyshev.py
│  │        │  │  │  ├─ test_classes.py
│  │        │  │  │  ├─ test_hermite.py
│  │        │  │  │  ├─ test_hermite_e.py
│  │        │  │  │  ├─ test_laguerre.py
│  │        │  │  │  ├─ test_legendre.py
│  │        │  │  │  ├─ test_polynomial.py
│  │        │  │  │  ├─ test_polyutils.py
│  │        │  │  │  ├─ test_printing.py
│  │        │  │  │  ├─ test_symbol.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_chebyshev.cpython-312.pyc
│  │        │  │  │     ├─ test_classes.cpython-312.pyc
│  │        │  │  │     ├─ test_hermite.cpython-312.pyc
│  │        │  │  │     ├─ test_hermite_e.cpython-312.pyc
│  │        │  │  │     ├─ test_laguerre.cpython-312.pyc
│  │        │  │  │     ├─ test_legendre.cpython-312.pyc
│  │        │  │  │     ├─ test_polynomial.cpython-312.pyc
│  │        │  │  │     ├─ test_polyutils.cpython-312.pyc
│  │        │  │  │     ├─ test_printing.cpython-312.pyc
│  │        │  │  │     ├─ test_symbol.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _polybase.py
│  │        │  │  ├─ _polybase.pyi
│  │        │  │  ├─ _polytypes.pyi
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ __init__.pyi
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ chebyshev.cpython-312.pyc
│  │        │  │     ├─ hermite.cpython-312.pyc
│  │        │  │     ├─ hermite_e.cpython-312.pyc
│  │        │  │     ├─ laguerre.cpython-312.pyc
│  │        │  │     ├─ legendre.cpython-312.pyc
│  │        │  │     ├─ polynomial.cpython-312.pyc
│  │        │  │     ├─ polyutils.cpython-312.pyc
│  │        │  │     ├─ _polybase.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ py.typed
│  │        │  ├─ random
│  │        │  │  ├─ bit_generator.cpython-312-darwin.so
│  │        │  │  ├─ bit_generator.pxd
│  │        │  │  ├─ bit_generator.pyi
│  │        │  │  ├─ c_distributions.pxd
│  │        │  │  ├─ lib
│  │        │  │  │  └─ libnpyrandom.a
│  │        │  │  ├─ LICENSE.md
│  │        │  │  ├─ mtrand.cpython-312-darwin.so
│  │        │  │  ├─ mtrand.pyi
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ data
│  │        │  │  │  │  ├─ generator_pcg64_np121.pkl.gz
│  │        │  │  │  │  ├─ generator_pcg64_np126.pkl.gz
│  │        │  │  │  │  ├─ mt19937-testset-1.csv
│  │        │  │  │  │  ├─ mt19937-testset-2.csv
│  │        │  │  │  │  ├─ pcg64-testset-1.csv
│  │        │  │  │  │  ├─ pcg64-testset-2.csv
│  │        │  │  │  │  ├─ pcg64dxsm-testset-1.csv
│  │        │  │  │  │  ├─ pcg64dxsm-testset-2.csv
│  │        │  │  │  │  ├─ philox-testset-1.csv
│  │        │  │  │  │  ├─ philox-testset-2.csv
│  │        │  │  │  │  ├─ sfc64-testset-1.csv
│  │        │  │  │  │  ├─ sfc64-testset-2.csv
│  │        │  │  │  │  ├─ sfc64_np126.pkl.gz
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ test_direct.py
│  │        │  │  │  ├─ test_extending.py
│  │        │  │  │  ├─ test_generator_mt19937.py
│  │        │  │  │  ├─ test_generator_mt19937_regressions.py
│  │        │  │  │  ├─ test_random.py
│  │        │  │  │  ├─ test_randomstate.py
│  │        │  │  │  ├─ test_randomstate_regression.py
│  │        │  │  │  ├─ test_regression.py
│  │        │  │  │  ├─ test_seed_sequence.py
│  │        │  │  │  ├─ test_smoke.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_direct.cpython-312.pyc
│  │        │  │  │     ├─ test_extending.cpython-312.pyc
│  │        │  │  │     ├─ test_generator_mt19937.cpython-312.pyc
│  │        │  │  │     ├─ test_generator_mt19937_regressions.cpython-312.pyc
│  │        │  │  │     ├─ test_random.cpython-312.pyc
│  │        │  │  │     ├─ test_randomstate.cpython-312.pyc
│  │        │  │  │     ├─ test_randomstate_regression.cpython-312.pyc
│  │        │  │  │     ├─ test_regression.cpython-312.pyc
│  │        │  │  │     ├─ test_seed_sequence.cpython-312.pyc
│  │        │  │  │     ├─ test_smoke.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _bounded_integers.cpython-312-darwin.so
│  │        │  │  ├─ _bounded_integers.pxd
│  │        │  │  ├─ _common.cpython-312-darwin.so
│  │        │  │  ├─ _common.pxd
│  │        │  │  ├─ _examples
│  │        │  │  │  ├─ cffi
│  │        │  │  │  │  ├─ extending.py
│  │        │  │  │  │  ├─ parse.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ extending.cpython-312.pyc
│  │        │  │  │  │     └─ parse.cpython-312.pyc
│  │        │  │  │  ├─ cython
│  │        │  │  │  │  ├─ extending.pyx
│  │        │  │  │  │  ├─ extending_distributions.pyx
│  │        │  │  │  │  └─ meson.build
│  │        │  │  │  └─ numba
│  │        │  │  │     ├─ extending.py
│  │        │  │  │     ├─ extending_distributions.py
│  │        │  │  │     └─ __pycache__
│  │        │  │  │        ├─ extending.cpython-312.pyc
│  │        │  │  │        └─ extending_distributions.cpython-312.pyc
│  │        │  │  ├─ _generator.cpython-312-darwin.so
│  │        │  │  ├─ _generator.pyi
│  │        │  │  ├─ _mt19937.cpython-312-darwin.so
│  │        │  │  ├─ _mt19937.pyi
│  │        │  │  ├─ _pcg64.cpython-312-darwin.so
│  │        │  │  ├─ _pcg64.pyi
│  │        │  │  ├─ _philox.cpython-312-darwin.so
│  │        │  │  ├─ _philox.pyi
│  │        │  │  ├─ _pickle.py
│  │        │  │  ├─ _pickle.pyi
│  │        │  │  ├─ _sfc64.cpython-312-darwin.so
│  │        │  │  ├─ _sfc64.pyi
│  │        │  │  ├─ __init__.pxd
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ __init__.pyi
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ _pickle.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ rec
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ __init__.pyi
│  │        │  │  └─ __pycache__
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ strings
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ __init__.pyi
│  │        │  │  └─ __pycache__
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ testing
│  │        │  │  ├─ overrides.py
│  │        │  │  ├─ overrides.pyi
│  │        │  │  ├─ print_coercion_tables.py
│  │        │  │  ├─ print_coercion_tables.pyi
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ test_utils.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_utils.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _private
│  │        │  │  │  ├─ extbuild.py
│  │        │  │  │  ├─ extbuild.pyi
│  │        │  │  │  ├─ utils.py
│  │        │  │  │  ├─ utils.pyi
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ __init__.pyi
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ extbuild.cpython-312.pyc
│  │        │  │  │     ├─ utils.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ __init__.pyi
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ overrides.cpython-312.pyc
│  │        │  │     ├─ print_coercion_tables.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ tests
│  │        │  │  ├─ test_configtool.py
│  │        │  │  ├─ test_ctypeslib.py
│  │        │  │  ├─ test_lazyloading.py
│  │        │  │  ├─ test_matlib.py
│  │        │  │  ├─ test_numpy_config.py
│  │        │  │  ├─ test_numpy_version.py
│  │        │  │  ├─ test_public_api.py
│  │        │  │  ├─ test_reloading.py
│  │        │  │  ├─ test_scripts.py
│  │        │  │  ├─ test_warnings.py
│  │        │  │  ├─ test__all__.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ test_configtool.cpython-312.pyc
│  │        │  │     ├─ test_ctypeslib.cpython-312.pyc
│  │        │  │     ├─ test_lazyloading.cpython-312.pyc
│  │        │  │     ├─ test_matlib.cpython-312.pyc
│  │        │  │     ├─ test_numpy_config.cpython-312.pyc
│  │        │  │     ├─ test_numpy_version.cpython-312.pyc
│  │        │  │     ├─ test_public_api.cpython-312.pyc
│  │        │  │     ├─ test_reloading.cpython-312.pyc
│  │        │  │     ├─ test_scripts.cpython-312.pyc
│  │        │  │     ├─ test_warnings.cpython-312.pyc
│  │        │  │     ├─ test__all__.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ typing
│  │        │  │  ├─ mypy_plugin.py
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ data
│  │        │  │  │  │  ├─ fail
│  │        │  │  │  │  │  ├─ arithmetic.pyi
│  │        │  │  │  │  │  ├─ arrayprint.pyi
│  │        │  │  │  │  │  ├─ arrayterator.pyi
│  │        │  │  │  │  │  ├─ array_constructors.pyi
│  │        │  │  │  │  │  ├─ array_like.pyi
│  │        │  │  │  │  │  ├─ array_pad.pyi
│  │        │  │  │  │  │  ├─ bitwise_ops.pyi
│  │        │  │  │  │  │  ├─ char.pyi
│  │        │  │  │  │  │  ├─ chararray.pyi
│  │        │  │  │  │  │  ├─ comparisons.pyi
│  │        │  │  │  │  │  ├─ constants.pyi
│  │        │  │  │  │  │  ├─ datasource.pyi
│  │        │  │  │  │  │  ├─ dtype.pyi
│  │        │  │  │  │  │  ├─ einsumfunc.pyi
│  │        │  │  │  │  │  ├─ flatiter.pyi
│  │        │  │  │  │  │  ├─ fromnumeric.pyi
│  │        │  │  │  │  │  ├─ histograms.pyi
│  │        │  │  │  │  │  ├─ index_tricks.pyi
│  │        │  │  │  │  │  ├─ lib_function_base.pyi
│  │        │  │  │  │  │  ├─ lib_polynomial.pyi
│  │        │  │  │  │  │  ├─ lib_utils.pyi
│  │        │  │  │  │  │  ├─ lib_version.pyi
│  │        │  │  │  │  │  ├─ linalg.pyi
│  │        │  │  │  │  │  ├─ memmap.pyi
│  │        │  │  │  │  │  ├─ modules.pyi
│  │        │  │  │  │  │  ├─ multiarray.pyi
│  │        │  │  │  │  │  ├─ ndarray.pyi
│  │        │  │  │  │  │  ├─ ndarray_misc.pyi
│  │        │  │  │  │  │  ├─ nditer.pyi
│  │        │  │  │  │  │  ├─ nested_sequence.pyi
│  │        │  │  │  │  │  ├─ npyio.pyi
│  │        │  │  │  │  │  ├─ numerictypes.pyi
│  │        │  │  │  │  │  ├─ random.pyi
│  │        │  │  │  │  │  ├─ rec.pyi
│  │        │  │  │  │  │  ├─ scalars.pyi
│  │        │  │  │  │  │  ├─ shape.pyi
│  │        │  │  │  │  │  ├─ shape_base.pyi
│  │        │  │  │  │  │  ├─ stride_tricks.pyi
│  │        │  │  │  │  │  ├─ strings.pyi
│  │        │  │  │  │  │  ├─ testing.pyi
│  │        │  │  │  │  │  ├─ twodim_base.pyi
│  │        │  │  │  │  │  ├─ type_check.pyi
│  │        │  │  │  │  │  ├─ ufunclike.pyi
│  │        │  │  │  │  │  ├─ ufuncs.pyi
│  │        │  │  │  │  │  ├─ ufunc_config.pyi
│  │        │  │  │  │  │  └─ warnings_and_errors.pyi
│  │        │  │  │  │  ├─ misc
│  │        │  │  │  │  │  └─ extended_precision.pyi
│  │        │  │  │  │  ├─ mypy.ini
│  │        │  │  │  │  ├─ pass
│  │        │  │  │  │  │  ├─ arithmetic.py
│  │        │  │  │  │  │  ├─ arrayprint.py
│  │        │  │  │  │  │  ├─ arrayterator.py
│  │        │  │  │  │  │  ├─ array_constructors.py
│  │        │  │  │  │  │  ├─ array_like.py
│  │        │  │  │  │  │  ├─ bitwise_ops.py
│  │        │  │  │  │  │  ├─ comparisons.py
│  │        │  │  │  │  │  ├─ dtype.py
│  │        │  │  │  │  │  ├─ einsumfunc.py
│  │        │  │  │  │  │  ├─ flatiter.py
│  │        │  │  │  │  │  ├─ fromnumeric.py
│  │        │  │  │  │  │  ├─ index_tricks.py
│  │        │  │  │  │  │  ├─ lib_user_array.py
│  │        │  │  │  │  │  ├─ lib_utils.py
│  │        │  │  │  │  │  ├─ lib_version.py
│  │        │  │  │  │  │  ├─ literal.py
│  │        │  │  │  │  │  ├─ ma.py
│  │        │  │  │  │  │  ├─ mod.py
│  │        │  │  │  │  │  ├─ modules.py
│  │        │  │  │  │  │  ├─ multiarray.py
│  │        │  │  │  │  │  ├─ ndarray_conversion.py
│  │        │  │  │  │  │  ├─ ndarray_misc.py
│  │        │  │  │  │  │  ├─ ndarray_shape_manipulation.py
│  │        │  │  │  │  │  ├─ nditer.py
│  │        │  │  │  │  │  ├─ numeric.py
│  │        │  │  │  │  │  ├─ numerictypes.py
│  │        │  │  │  │  │  ├─ random.py
│  │        │  │  │  │  │  ├─ recfunctions.py
│  │        │  │  │  │  │  ├─ scalars.py
│  │        │  │  │  │  │  ├─ shape.py
│  │        │  │  │  │  │  ├─ simple.py
│  │        │  │  │  │  │  ├─ simple_py3.py
│  │        │  │  │  │  │  ├─ ufunclike.py
│  │        │  │  │  │  │  ├─ ufuncs.py
│  │        │  │  │  │  │  ├─ ufunc_config.py
│  │        │  │  │  │  │  ├─ warnings_and_errors.py
│  │        │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │     ├─ arithmetic.cpython-312.pyc
│  │        │  │  │  │  │     ├─ arrayprint.cpython-312.pyc
│  │        │  │  │  │  │     ├─ arrayterator.cpython-312.pyc
│  │        │  │  │  │  │     ├─ array_constructors.cpython-312.pyc
│  │        │  │  │  │  │     ├─ array_like.cpython-312.pyc
│  │        │  │  │  │  │     ├─ bitwise_ops.cpython-312.pyc
│  │        │  │  │  │  │     ├─ comparisons.cpython-312.pyc
│  │        │  │  │  │  │     ├─ dtype.cpython-312.pyc
│  │        │  │  │  │  │     ├─ einsumfunc.cpython-312.pyc
│  │        │  │  │  │  │     ├─ flatiter.cpython-312.pyc
│  │        │  │  │  │  │     ├─ fromnumeric.cpython-312.pyc
│  │        │  │  │  │  │     ├─ index_tricks.cpython-312.pyc
│  │        │  │  │  │  │     ├─ lib_user_array.cpython-312.pyc
│  │        │  │  │  │  │     ├─ lib_utils.cpython-312.pyc
│  │        │  │  │  │  │     ├─ lib_version.cpython-312.pyc
│  │        │  │  │  │  │     ├─ literal.cpython-312.pyc
│  │        │  │  │  │  │     ├─ ma.cpython-312.pyc
│  │        │  │  │  │  │     ├─ mod.cpython-312.pyc
│  │        │  │  │  │  │     ├─ modules.cpython-312.pyc
│  │        │  │  │  │  │     ├─ multiarray.cpython-312.pyc
│  │        │  │  │  │  │     ├─ ndarray_conversion.cpython-312.pyc
│  │        │  │  │  │  │     ├─ ndarray_misc.cpython-312.pyc
│  │        │  │  │  │  │     ├─ ndarray_shape_manipulation.cpython-312.pyc
│  │        │  │  │  │  │     ├─ nditer.cpython-312.pyc
│  │        │  │  │  │  │     ├─ numeric.cpython-312.pyc
│  │        │  │  │  │  │     ├─ numerictypes.cpython-312.pyc
│  │        │  │  │  │  │     ├─ random.cpython-312.pyc
│  │        │  │  │  │  │     ├─ recfunctions.cpython-312.pyc
│  │        │  │  │  │  │     ├─ scalars.cpython-312.pyc
│  │        │  │  │  │  │     ├─ shape.cpython-312.pyc
│  │        │  │  │  │  │     ├─ simple.cpython-312.pyc
│  │        │  │  │  │  │     ├─ simple_py3.cpython-312.pyc
│  │        │  │  │  │  │     ├─ ufunclike.cpython-312.pyc
│  │        │  │  │  │  │     ├─ ufuncs.cpython-312.pyc
│  │        │  │  │  │  │     ├─ ufunc_config.cpython-312.pyc
│  │        │  │  │  │  │     └─ warnings_and_errors.cpython-312.pyc
│  │        │  │  │  │  └─ reveal
│  │        │  │  │  │     ├─ arithmetic.pyi
│  │        │  │  │  │     ├─ arraypad.pyi
│  │        │  │  │  │     ├─ arrayprint.pyi
│  │        │  │  │  │     ├─ arraysetops.pyi
│  │        │  │  │  │     ├─ arrayterator.pyi
│  │        │  │  │  │     ├─ array_api_info.pyi
│  │        │  │  │  │     ├─ array_constructors.pyi
│  │        │  │  │  │     ├─ bitwise_ops.pyi
│  │        │  │  │  │     ├─ char.pyi
│  │        │  │  │  │     ├─ chararray.pyi
│  │        │  │  │  │     ├─ comparisons.pyi
│  │        │  │  │  │     ├─ constants.pyi
│  │        │  │  │  │     ├─ ctypeslib.pyi
│  │        │  │  │  │     ├─ datasource.pyi
│  │        │  │  │  │     ├─ dtype.pyi
│  │        │  │  │  │     ├─ einsumfunc.pyi
│  │        │  │  │  │     ├─ emath.pyi
│  │        │  │  │  │     ├─ fft.pyi
│  │        │  │  │  │     ├─ flatiter.pyi
│  │        │  │  │  │     ├─ fromnumeric.pyi
│  │        │  │  │  │     ├─ getlimits.pyi
│  │        │  │  │  │     ├─ histograms.pyi
│  │        │  │  │  │     ├─ index_tricks.pyi
│  │        │  │  │  │     ├─ lib_function_base.pyi
│  │        │  │  │  │     ├─ lib_polynomial.pyi
│  │        │  │  │  │     ├─ lib_utils.pyi
│  │        │  │  │  │     ├─ lib_version.pyi
│  │        │  │  │  │     ├─ linalg.pyi
│  │        │  │  │  │     ├─ matrix.pyi
│  │        │  │  │  │     ├─ memmap.pyi
│  │        │  │  │  │     ├─ mod.pyi
│  │        │  │  │  │     ├─ modules.pyi
│  │        │  │  │  │     ├─ multiarray.pyi
│  │        │  │  │  │     ├─ nbit_base_example.pyi
│  │        │  │  │  │     ├─ ndarray_assignability.pyi
│  │        │  │  │  │     ├─ ndarray_conversion.pyi
│  │        │  │  │  │     ├─ ndarray_misc.pyi
│  │        │  │  │  │     ├─ ndarray_shape_manipulation.pyi
│  │        │  │  │  │     ├─ nditer.pyi
│  │        │  │  │  │     ├─ nested_sequence.pyi
│  │        │  │  │  │     ├─ npyio.pyi
│  │        │  │  │  │     ├─ numeric.pyi
│  │        │  │  │  │     ├─ numerictypes.pyi
│  │        │  │  │  │     ├─ polynomial_polybase.pyi
│  │        │  │  │  │     ├─ polynomial_polyutils.pyi
│  │        │  │  │  │     ├─ polynomial_series.pyi
│  │        │  │  │  │     ├─ random.pyi
│  │        │  │  │  │     ├─ rec.pyi
│  │        │  │  │  │     ├─ scalars.pyi
│  │        │  │  │  │     ├─ shape.pyi
│  │        │  │  │  │     ├─ shape_base.pyi
│  │        │  │  │  │     ├─ stride_tricks.pyi
│  │        │  │  │  │     ├─ strings.pyi
│  │        │  │  │  │     ├─ testing.pyi
│  │        │  │  │  │     ├─ twodim_base.pyi
│  │        │  │  │  │     ├─ type_check.pyi
│  │        │  │  │  │     ├─ ufunclike.pyi
│  │        │  │  │  │     ├─ ufuncs.pyi
│  │        │  │  │  │     ├─ ufunc_config.pyi
│  │        │  │  │  │     └─ warnings_and_errors.pyi
│  │        │  │  │  ├─ test_isfile.py
│  │        │  │  │  ├─ test_runtime.py
│  │        │  │  │  ├─ test_typing.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_isfile.cpython-312.pyc
│  │        │  │  │     ├─ test_runtime.cpython-312.pyc
│  │        │  │  │     ├─ test_typing.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ mypy_plugin.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ version.py
│  │        │  ├─ version.pyi
│  │        │  ├─ _array_api_info.py
│  │        │  ├─ _array_api_info.pyi
│  │        │  ├─ _configtool.py
│  │        │  ├─ _configtool.pyi
│  │        │  ├─ _core
│  │        │  │  ├─ arrayprint.py
│  │        │  │  ├─ arrayprint.pyi
│  │        │  │  ├─ cversions.py
│  │        │  │  ├─ defchararray.py
│  │        │  │  ├─ defchararray.pyi
│  │        │  │  ├─ einsumfunc.py
│  │        │  │  ├─ einsumfunc.pyi
│  │        │  │  ├─ fromnumeric.py
│  │        │  │  ├─ fromnumeric.pyi
│  │        │  │  ├─ function_base.py
│  │        │  │  ├─ function_base.pyi
│  │        │  │  ├─ getlimits.py
│  │        │  │  ├─ getlimits.pyi
│  │        │  │  ├─ include
│  │        │  │  │  └─ numpy
│  │        │  │  │     ├─ arrayobject.h
│  │        │  │  │     ├─ arrayscalars.h
│  │        │  │  │     ├─ dtype_api.h
│  │        │  │  │     ├─ halffloat.h
│  │        │  │  │     ├─ ndarrayobject.h
│  │        │  │  │     ├─ ndarraytypes.h
│  │        │  │  │     ├─ npy_1_7_deprecated_api.h
│  │        │  │  │     ├─ npy_2_compat.h
│  │        │  │  │     ├─ npy_2_complexcompat.h
│  │        │  │  │     ├─ npy_3kcompat.h
│  │        │  │  │     ├─ npy_common.h
│  │        │  │  │     ├─ npy_cpu.h
│  │        │  │  │     ├─ npy_endian.h
│  │        │  │  │     ├─ npy_math.h
│  │        │  │  │     ├─ npy_no_deprecated_api.h
│  │        │  │  │     ├─ npy_os.h
│  │        │  │  │     ├─ numpyconfig.h
│  │        │  │  │     ├─ random
│  │        │  │  │     │  ├─ bitgen.h
│  │        │  │  │     │  ├─ distributions.h
│  │        │  │  │     │  ├─ libdivide.h
│  │        │  │  │     │  └─ LICENSE.txt
│  │        │  │  │     ├─ ufuncobject.h
│  │        │  │  │     ├─ utils.h
│  │        │  │  │     ├─ _neighborhood_iterator_imp.h
│  │        │  │  │     ├─ _numpyconfig.h
│  │        │  │  │     ├─ _public_dtype_api_table.h
│  │        │  │  │     ├─ __multiarray_api.c
│  │        │  │  │     ├─ __multiarray_api.h
│  │        │  │  │     ├─ __ufunc_api.c
│  │        │  │  │     └─ __ufunc_api.h
│  │        │  │  ├─ lib
│  │        │  │  │  ├─ libnpymath.a
│  │        │  │  │  ├─ npy-pkg-config
│  │        │  │  │  │  ├─ mlib.ini
│  │        │  │  │  │  └─ npymath.ini
│  │        │  │  │  └─ pkgconfig
│  │        │  │  │     └─ numpy.pc
│  │        │  │  ├─ memmap.py
│  │        │  │  ├─ memmap.pyi
│  │        │  │  ├─ multiarray.py
│  │        │  │  ├─ multiarray.pyi
│  │        │  │  ├─ numeric.py
│  │        │  │  ├─ numeric.pyi
│  │        │  │  ├─ numerictypes.py
│  │        │  │  ├─ numerictypes.pyi
│  │        │  │  ├─ overrides.py
│  │        │  │  ├─ overrides.pyi
│  │        │  │  ├─ printoptions.py
│  │        │  │  ├─ printoptions.pyi
│  │        │  │  ├─ records.py
│  │        │  │  ├─ records.pyi
│  │        │  │  ├─ shape_base.py
│  │        │  │  ├─ shape_base.pyi
│  │        │  │  ├─ strings.py
│  │        │  │  ├─ strings.pyi
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ data
│  │        │  │  │  │  ├─ astype_copy.pkl
│  │        │  │  │  │  ├─ generate_umath_validation_data.cpp
│  │        │  │  │  │  ├─ recarray_from_file.fits
│  │        │  │  │  │  ├─ umath-validation-set-arccos.csv
│  │        │  │  │  │  ├─ umath-validation-set-arccosh.csv
│  │        │  │  │  │  ├─ umath-validation-set-arcsin.csv
│  │        │  │  │  │  ├─ umath-validation-set-arcsinh.csv
│  │        │  │  │  │  ├─ umath-validation-set-arctan.csv
│  │        │  │  │  │  ├─ umath-validation-set-arctanh.csv
│  │        │  │  │  │  ├─ umath-validation-set-cbrt.csv
│  │        │  │  │  │  ├─ umath-validation-set-cos.csv
│  │        │  │  │  │  ├─ umath-validation-set-cosh.csv
│  │        │  │  │  │  ├─ umath-validation-set-exp.csv
│  │        │  │  │  │  ├─ umath-validation-set-exp2.csv
│  │        │  │  │  │  ├─ umath-validation-set-expm1.csv
│  │        │  │  │  │  ├─ umath-validation-set-log.csv
│  │        │  │  │  │  ├─ umath-validation-set-log10.csv
│  │        │  │  │  │  ├─ umath-validation-set-log1p.csv
│  │        │  │  │  │  ├─ umath-validation-set-log2.csv
│  │        │  │  │  │  ├─ umath-validation-set-README.txt
│  │        │  │  │  │  ├─ umath-validation-set-sin.csv
│  │        │  │  │  │  ├─ umath-validation-set-sinh.csv
│  │        │  │  │  │  ├─ umath-validation-set-tan.csv
│  │        │  │  │  │  └─ umath-validation-set-tanh.csv
│  │        │  │  │  ├─ examples
│  │        │  │  │  │  ├─ cython
│  │        │  │  │  │  │  ├─ checks.pyx
│  │        │  │  │  │  │  ├─ meson.build
│  │        │  │  │  │  │  ├─ setup.py
│  │        │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │     └─ setup.cpython-312.pyc
│  │        │  │  │  │  └─ limited_api
│  │        │  │  │  │     ├─ limited_api1.c
│  │        │  │  │  │     ├─ limited_api2.pyx
│  │        │  │  │  │     ├─ limited_api_latest.c
│  │        │  │  │  │     ├─ meson.build
│  │        │  │  │  │     ├─ setup.py
│  │        │  │  │  │     └─ __pycache__
│  │        │  │  │  │        └─ setup.cpython-312.pyc
│  │        │  │  │  ├─ test_abc.py
│  │        │  │  │  ├─ test_api.py
│  │        │  │  │  ├─ test_argparse.py
│  │        │  │  │  ├─ test_arraymethod.py
│  │        │  │  │  ├─ test_arrayobject.py
│  │        │  │  │  ├─ test_arrayprint.py
│  │        │  │  │  ├─ test_array_api_info.py
│  │        │  │  │  ├─ test_array_coercion.py
│  │        │  │  │  ├─ test_array_interface.py
│  │        │  │  │  ├─ test_casting_floatingpoint_errors.py
│  │        │  │  │  ├─ test_casting_unittests.py
│  │        │  │  │  ├─ test_conversion_utils.py
│  │        │  │  │  ├─ test_cpu_dispatcher.py
│  │        │  │  │  ├─ test_cpu_features.py
│  │        │  │  │  ├─ test_custom_dtypes.py
│  │        │  │  │  ├─ test_cython.py
│  │        │  │  │  ├─ test_datetime.py
│  │        │  │  │  ├─ test_defchararray.py
│  │        │  │  │  ├─ test_deprecations.py
│  │        │  │  │  ├─ test_dlpack.py
│  │        │  │  │  ├─ test_dtype.py
│  │        │  │  │  ├─ test_einsum.py
│  │        │  │  │  ├─ test_errstate.py
│  │        │  │  │  ├─ test_extint128.py
│  │        │  │  │  ├─ test_function_base.py
│  │        │  │  │  ├─ test_getlimits.py
│  │        │  │  │  ├─ test_half.py
│  │        │  │  │  ├─ test_hashtable.py
│  │        │  │  │  ├─ test_indexerrors.py
│  │        │  │  │  ├─ test_indexing.py
│  │        │  │  │  ├─ test_item_selection.py
│  │        │  │  │  ├─ test_limited_api.py
│  │        │  │  │  ├─ test_longdouble.py
│  │        │  │  │  ├─ test_machar.py
│  │        │  │  │  ├─ test_memmap.py
│  │        │  │  │  ├─ test_mem_overlap.py
│  │        │  │  │  ├─ test_mem_policy.py
│  │        │  │  │  ├─ test_multiarray.py
│  │        │  │  │  ├─ test_multithreading.py
│  │        │  │  │  ├─ test_nditer.py
│  │        │  │  │  ├─ test_nep50_promotions.py
│  │        │  │  │  ├─ test_numeric.py
│  │        │  │  │  ├─ test_numerictypes.py
│  │        │  │  │  ├─ test_overrides.py
│  │        │  │  │  ├─ test_print.py
│  │        │  │  │  ├─ test_protocols.py
│  │        │  │  │  ├─ test_records.py
│  │        │  │  │  ├─ test_regression.py
│  │        │  │  │  ├─ test_scalarbuffer.py
│  │        │  │  │  ├─ test_scalarinherit.py
│  │        │  │  │  ├─ test_scalarmath.py
│  │        │  │  │  ├─ test_scalarprint.py
│  │        │  │  │  ├─ test_scalar_ctors.py
│  │        │  │  │  ├─ test_scalar_methods.py
│  │        │  │  │  ├─ test_shape_base.py
│  │        │  │  │  ├─ test_simd.py
│  │        │  │  │  ├─ test_simd_module.py
│  │        │  │  │  ├─ test_stringdtype.py
│  │        │  │  │  ├─ test_strings.py
│  │        │  │  │  ├─ test_ufunc.py
│  │        │  │  │  ├─ test_umath.py
│  │        │  │  │  ├─ test_umath_accuracy.py
│  │        │  │  │  ├─ test_umath_complex.py
│  │        │  │  │  ├─ test_unicode.py
│  │        │  │  │  ├─ test__exceptions.py
│  │        │  │  │  ├─ _locales.py
│  │        │  │  │  ├─ _natype.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_abc.cpython-312.pyc
│  │        │  │  │     ├─ test_api.cpython-312.pyc
│  │        │  │  │     ├─ test_argparse.cpython-312.pyc
│  │        │  │  │     ├─ test_arraymethod.cpython-312.pyc
│  │        │  │  │     ├─ test_arrayobject.cpython-312.pyc
│  │        │  │  │     ├─ test_arrayprint.cpython-312.pyc
│  │        │  │  │     ├─ test_array_api_info.cpython-312.pyc
│  │        │  │  │     ├─ test_array_coercion.cpython-312.pyc
│  │        │  │  │     ├─ test_array_interface.cpython-312.pyc
│  │        │  │  │     ├─ test_casting_floatingpoint_errors.cpython-312.pyc
│  │        │  │  │     ├─ test_casting_unittests.cpython-312.pyc
│  │        │  │  │     ├─ test_conversion_utils.cpython-312.pyc
│  │        │  │  │     ├─ test_cpu_dispatcher.cpython-312.pyc
│  │        │  │  │     ├─ test_cpu_features.cpython-312.pyc
│  │        │  │  │     ├─ test_custom_dtypes.cpython-312.pyc
│  │        │  │  │     ├─ test_cython.cpython-312.pyc
│  │        │  │  │     ├─ test_datetime.cpython-312.pyc
│  │        │  │  │     ├─ test_defchararray.cpython-312.pyc
│  │        │  │  │     ├─ test_deprecations.cpython-312.pyc
│  │        │  │  │     ├─ test_dlpack.cpython-312.pyc
│  │        │  │  │     ├─ test_dtype.cpython-312.pyc
│  │        │  │  │     ├─ test_einsum.cpython-312.pyc
│  │        │  │  │     ├─ test_errstate.cpython-312.pyc
│  │        │  │  │     ├─ test_extint128.cpython-312.pyc
│  │        │  │  │     ├─ test_function_base.cpython-312.pyc
│  │        │  │  │     ├─ test_getlimits.cpython-312.pyc
│  │        │  │  │     ├─ test_half.cpython-312.pyc
│  │        │  │  │     ├─ test_hashtable.cpython-312.pyc
│  │        │  │  │     ├─ test_indexerrors.cpython-312.pyc
│  │        │  │  │     ├─ test_indexing.cpython-312.pyc
│  │        │  │  │     ├─ test_item_selection.cpython-312.pyc
│  │        │  │  │     ├─ test_limited_api.cpython-312.pyc
│  │        │  │  │     ├─ test_longdouble.cpython-312.pyc
│  │        │  │  │     ├─ test_machar.cpython-312.pyc
│  │        │  │  │     ├─ test_memmap.cpython-312.pyc
│  │        │  │  │     ├─ test_mem_overlap.cpython-312.pyc
│  │        │  │  │     ├─ test_mem_policy.cpython-312.pyc
│  │        │  │  │     ├─ test_multiarray.cpython-312.pyc
│  │        │  │  │     ├─ test_multithreading.cpython-312.pyc
│  │        │  │  │     ├─ test_nditer.cpython-312.pyc
│  │        │  │  │     ├─ test_nep50_promotions.cpython-312.pyc
│  │        │  │  │     ├─ test_numeric.cpython-312.pyc
│  │        │  │  │     ├─ test_numerictypes.cpython-312.pyc
│  │        │  │  │     ├─ test_overrides.cpython-312.pyc
│  │        │  │  │     ├─ test_print.cpython-312.pyc
│  │        │  │  │     ├─ test_protocols.cpython-312.pyc
│  │        │  │  │     ├─ test_records.cpython-312.pyc
│  │        │  │  │     ├─ test_regression.cpython-312.pyc
│  │        │  │  │     ├─ test_scalarbuffer.cpython-312.pyc
│  │        │  │  │     ├─ test_scalarinherit.cpython-312.pyc
│  │        │  │  │     ├─ test_scalarmath.cpython-312.pyc
│  │        │  │  │     ├─ test_scalarprint.cpython-312.pyc
│  │        │  │  │     ├─ test_scalar_ctors.cpython-312.pyc
│  │        │  │  │     ├─ test_scalar_methods.cpython-312.pyc
│  │        │  │  │     ├─ test_shape_base.cpython-312.pyc
│  │        │  │  │     ├─ test_simd.cpython-312.pyc
│  │        │  │  │     ├─ test_simd_module.cpython-312.pyc
│  │        │  │  │     ├─ test_stringdtype.cpython-312.pyc
│  │        │  │  │     ├─ test_strings.cpython-312.pyc
│  │        │  │  │     ├─ test_ufunc.cpython-312.pyc
│  │        │  │  │     ├─ test_umath.cpython-312.pyc
│  │        │  │  │     ├─ test_umath_accuracy.cpython-312.pyc
│  │        │  │  │     ├─ test_umath_complex.cpython-312.pyc
│  │        │  │  │     ├─ test_unicode.cpython-312.pyc
│  │        │  │  │     ├─ test__exceptions.cpython-312.pyc
│  │        │  │  │     ├─ _locales.cpython-312.pyc
│  │        │  │  │     └─ _natype.cpython-312.pyc
│  │        │  │  ├─ umath.py
│  │        │  │  ├─ umath.pyi
│  │        │  │  ├─ _add_newdocs.py
│  │        │  │  ├─ _add_newdocs.pyi
│  │        │  │  ├─ _add_newdocs_scalars.py
│  │        │  │  ├─ _add_newdocs_scalars.pyi
│  │        │  │  ├─ _asarray.py
│  │        │  │  ├─ _asarray.pyi
│  │        │  │  ├─ _dtype.py
│  │        │  │  ├─ _dtype.pyi
│  │        │  │  ├─ _dtype_ctypes.py
│  │        │  │  ├─ _dtype_ctypes.pyi
│  │        │  │  ├─ _exceptions.py
│  │        │  │  ├─ _exceptions.pyi
│  │        │  │  ├─ _internal.py
│  │        │  │  ├─ _internal.pyi
│  │        │  │  ├─ _machar.py
│  │        │  │  ├─ _machar.pyi
│  │        │  │  ├─ _methods.py
│  │        │  │  ├─ _methods.pyi
│  │        │  │  ├─ _multiarray_tests.cpython-312-darwin.so
│  │        │  │  ├─ _multiarray_umath.cpython-312-darwin.so
│  │        │  │  ├─ _operand_flag_tests.cpython-312-darwin.so
│  │        │  │  ├─ _rational_tests.cpython-312-darwin.so
│  │        │  │  ├─ _simd.cpython-312-darwin.so
│  │        │  │  ├─ _simd.pyi
│  │        │  │  ├─ _string_helpers.py
│  │        │  │  ├─ _string_helpers.pyi
│  │        │  │  ├─ _struct_ufunc_tests.cpython-312-darwin.so
│  │        │  │  ├─ _type_aliases.py
│  │        │  │  ├─ _type_aliases.pyi
│  │        │  │  ├─ _ufunc_config.py
│  │        │  │  ├─ _ufunc_config.pyi
│  │        │  │  ├─ _umath_tests.cpython-312-darwin.so
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ __init__.pyi
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ arrayprint.cpython-312.pyc
│  │        │  │     ├─ cversions.cpython-312.pyc
│  │        │  │     ├─ defchararray.cpython-312.pyc
│  │        │  │     ├─ einsumfunc.cpython-312.pyc
│  │        │  │     ├─ fromnumeric.cpython-312.pyc
│  │        │  │     ├─ function_base.cpython-312.pyc
│  │        │  │     ├─ getlimits.cpython-312.pyc
│  │        │  │     ├─ memmap.cpython-312.pyc
│  │        │  │     ├─ multiarray.cpython-312.pyc
│  │        │  │     ├─ numeric.cpython-312.pyc
│  │        │  │     ├─ numerictypes.cpython-312.pyc
│  │        │  │     ├─ overrides.cpython-312.pyc
│  │        │  │     ├─ printoptions.cpython-312.pyc
│  │        │  │     ├─ records.cpython-312.pyc
│  │        │  │     ├─ shape_base.cpython-312.pyc
│  │        │  │     ├─ strings.cpython-312.pyc
│  │        │  │     ├─ umath.cpython-312.pyc
│  │        │  │     ├─ _add_newdocs.cpython-312.pyc
│  │        │  │     ├─ _add_newdocs_scalars.cpython-312.pyc
│  │        │  │     ├─ _asarray.cpython-312.pyc
│  │        │  │     ├─ _dtype.cpython-312.pyc
│  │        │  │     ├─ _dtype_ctypes.cpython-312.pyc
│  │        │  │     ├─ _exceptions.cpython-312.pyc
│  │        │  │     ├─ _internal.cpython-312.pyc
│  │        │  │     ├─ _machar.cpython-312.pyc
│  │        │  │     ├─ _methods.cpython-312.pyc
│  │        │  │     ├─ _string_helpers.cpython-312.pyc
│  │        │  │     ├─ _type_aliases.cpython-312.pyc
│  │        │  │     ├─ _ufunc_config.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ _distributor_init.py
│  │        │  ├─ _distributor_init.pyi
│  │        │  ├─ _expired_attrs_2_0.py
│  │        │  ├─ _expired_attrs_2_0.pyi
│  │        │  ├─ _globals.py
│  │        │  ├─ _globals.pyi
│  │        │  ├─ _pyinstaller
│  │        │  │  ├─ hook-numpy.py
│  │        │  │  ├─ hook-numpy.pyi
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ pyinstaller-smoke.py
│  │        │  │  │  ├─ test_pyinstaller.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ pyinstaller-smoke.cpython-312.pyc
│  │        │  │  │     ├─ test_pyinstaller.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ __init__.pyi
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ hook-numpy.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ _pytesttester.py
│  │        │  ├─ _pytesttester.pyi
│  │        │  ├─ _typing
│  │        │  │  ├─ _add_docstring.py
│  │        │  │  ├─ _array_like.py
│  │        │  │  ├─ _callable.pyi
│  │        │  │  ├─ _char_codes.py
│  │        │  │  ├─ _dtype_like.py
│  │        │  │  ├─ _extended_precision.py
│  │        │  │  ├─ _nbit.py
│  │        │  │  ├─ _nbit_base.py
│  │        │  │  ├─ _nested_sequence.py
│  │        │  │  ├─ _scalars.py
│  │        │  │  ├─ _shape.py
│  │        │  │  ├─ _ufunc.py
│  │        │  │  ├─ _ufunc.pyi
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ _add_docstring.cpython-312.pyc
│  │        │  │     ├─ _array_like.cpython-312.pyc
│  │        │  │     ├─ _char_codes.cpython-312.pyc
│  │        │  │     ├─ _dtype_like.cpython-312.pyc
│  │        │  │     ├─ _extended_precision.cpython-312.pyc
│  │        │  │     ├─ _nbit.cpython-312.pyc
│  │        │  │     ├─ _nbit_base.cpython-312.pyc
│  │        │  │     ├─ _nested_sequence.cpython-312.pyc
│  │        │  │     ├─ _scalars.cpython-312.pyc
│  │        │  │     ├─ _shape.cpython-312.pyc
│  │        │  │     ├─ _ufunc.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ _utils
│  │        │  │  ├─ _convertions.py
│  │        │  │  ├─ _convertions.pyi
│  │        │  │  ├─ _inspect.py
│  │        │  │  ├─ _inspect.pyi
│  │        │  │  ├─ _pep440.py
│  │        │  │  ├─ _pep440.pyi
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ __init__.pyi
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ _convertions.cpython-312.pyc
│  │        │  │     ├─ _inspect.cpython-312.pyc
│  │        │  │     ├─ _pep440.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ __config__.py
│  │        │  ├─ __config__.pyi
│  │        │  ├─ __init__.cython-30.pxd
│  │        │  ├─ __init__.pxd
│  │        │  ├─ __init__.py
│  │        │  ├─ __init__.pyi
│  │        │  └─ __pycache__
│  │        │     ├─ conftest.cpython-312.pyc
│  │        │     ├─ ctypeslib.cpython-312.pyc
│  │        │     ├─ dtypes.cpython-312.pyc
│  │        │     ├─ exceptions.cpython-312.pyc
│  │        │     ├─ matlib.cpython-312.pyc
│  │        │     ├─ version.cpython-312.pyc
│  │        │     ├─ _array_api_info.cpython-312.pyc
│  │        │     ├─ _configtool.cpython-312.pyc
│  │        │     ├─ _distributor_init.cpython-312.pyc
│  │        │     ├─ _expired_attrs_2_0.cpython-312.pyc
│  │        │     ├─ _globals.cpython-312.pyc
│  │        │     ├─ _pytesttester.cpython-312.pyc
│  │        │     ├─ __config__.cpython-312.pyc
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ numpy-2.2.6.dist-info
│  │        │  ├─ entry_points.txt
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE.txt
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ REQUESTED
│  │        │  └─ WHEEL
│  │        ├─ orjson
│  │        │  ├─ orjson.cpython-312-darwin.so
│  │        │  ├─ py.typed
│  │        │  ├─ __init__.py
│  │        │  ├─ __init__.pyi
│  │        │  └─ __pycache__
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ orjson-3.10.18.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ licenses
│  │        │  │  ├─ LICENSE-APACHE
│  │        │  │  └─ LICENSE-MIT
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  └─ WHEEL
│  │        ├─ pandas
│  │        │  ├─ api
│  │        │  │  ├─ extensions
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ indexers
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ interchange
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ types
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ typing
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ arrays
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ compat
│  │        │  │  ├─ compressors.py
│  │        │  │  ├─ numpy
│  │        │  │  │  ├─ function.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ function.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ pickle_compat.py
│  │        │  │  ├─ pyarrow.py
│  │        │  │  ├─ _constants.py
│  │        │  │  ├─ _optional.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ compressors.cpython-312.pyc
│  │        │  │     ├─ pickle_compat.cpython-312.pyc
│  │        │  │     ├─ pyarrow.cpython-312.pyc
│  │        │  │     ├─ _constants.cpython-312.pyc
│  │        │  │     ├─ _optional.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ conftest.py
│  │        │  ├─ core
│  │        │  │  ├─ accessor.py
│  │        │  │  ├─ algorithms.py
│  │        │  │  ├─ api.py
│  │        │  │  ├─ apply.py
│  │        │  │  ├─ arraylike.py
│  │        │  │  ├─ arrays
│  │        │  │  │  ├─ arrow
│  │        │  │  │  │  ├─ accessors.py
│  │        │  │  │  │  ├─ array.py
│  │        │  │  │  │  ├─ extension_types.py
│  │        │  │  │  │  ├─ _arrow_utils.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ accessors.cpython-312.pyc
│  │        │  │  │  │     ├─ array.cpython-312.pyc
│  │        │  │  │  │     ├─ extension_types.cpython-312.pyc
│  │        │  │  │  │     ├─ _arrow_utils.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ base.py
│  │        │  │  │  ├─ boolean.py
│  │        │  │  │  ├─ categorical.py
│  │        │  │  │  ├─ datetimelike.py
│  │        │  │  │  ├─ datetimes.py
│  │        │  │  │  ├─ floating.py
│  │        │  │  │  ├─ integer.py
│  │        │  │  │  ├─ interval.py
│  │        │  │  │  ├─ masked.py
│  │        │  │  │  ├─ numeric.py
│  │        │  │  │  ├─ numpy_.py
│  │        │  │  │  ├─ period.py
│  │        │  │  │  ├─ sparse
│  │        │  │  │  │  ├─ accessor.py
│  │        │  │  │  │  ├─ array.py
│  │        │  │  │  │  ├─ scipy_sparse.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ accessor.cpython-312.pyc
│  │        │  │  │  │     ├─ array.cpython-312.pyc
│  │        │  │  │  │     ├─ scipy_sparse.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ string_.py
│  │        │  │  │  ├─ string_arrow.py
│  │        │  │  │  ├─ timedeltas.py
│  │        │  │  │  ├─ _arrow_string_mixins.py
│  │        │  │  │  ├─ _mixins.py
│  │        │  │  │  ├─ _ranges.py
│  │        │  │  │  ├─ _utils.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ base.cpython-312.pyc
│  │        │  │  │     ├─ boolean.cpython-312.pyc
│  │        │  │  │     ├─ categorical.cpython-312.pyc
│  │        │  │  │     ├─ datetimelike.cpython-312.pyc
│  │        │  │  │     ├─ datetimes.cpython-312.pyc
│  │        │  │  │     ├─ floating.cpython-312.pyc
│  │        │  │  │     ├─ integer.cpython-312.pyc
│  │        │  │  │     ├─ interval.cpython-312.pyc
│  │        │  │  │     ├─ masked.cpython-312.pyc
│  │        │  │  │     ├─ numeric.cpython-312.pyc
│  │        │  │  │     ├─ numpy_.cpython-312.pyc
│  │        │  │  │     ├─ period.cpython-312.pyc
│  │        │  │  │     ├─ string_.cpython-312.pyc
│  │        │  │  │     ├─ string_arrow.cpython-312.pyc
│  │        │  │  │     ├─ timedeltas.cpython-312.pyc
│  │        │  │  │     ├─ _arrow_string_mixins.cpython-312.pyc
│  │        │  │  │     ├─ _mixins.cpython-312.pyc
│  │        │  │  │     ├─ _ranges.cpython-312.pyc
│  │        │  │  │     ├─ _utils.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ array_algos
│  │        │  │  │  ├─ datetimelike_accumulations.py
│  │        │  │  │  ├─ masked_accumulations.py
│  │        │  │  │  ├─ masked_reductions.py
│  │        │  │  │  ├─ putmask.py
│  │        │  │  │  ├─ quantile.py
│  │        │  │  │  ├─ replace.py
│  │        │  │  │  ├─ take.py
│  │        │  │  │  ├─ transforms.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ datetimelike_accumulations.cpython-312.pyc
│  │        │  │  │     ├─ masked_accumulations.cpython-312.pyc
│  │        │  │  │     ├─ masked_reductions.cpython-312.pyc
│  │        │  │  │     ├─ putmask.cpython-312.pyc
│  │        │  │  │     ├─ quantile.cpython-312.pyc
│  │        │  │  │     ├─ replace.cpython-312.pyc
│  │        │  │  │     ├─ take.cpython-312.pyc
│  │        │  │  │     ├─ transforms.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ base.py
│  │        │  │  ├─ common.py
│  │        │  │  ├─ computation
│  │        │  │  │  ├─ align.py
│  │        │  │  │  ├─ api.py
│  │        │  │  │  ├─ check.py
│  │        │  │  │  ├─ common.py
│  │        │  │  │  ├─ engines.py
│  │        │  │  │  ├─ eval.py
│  │        │  │  │  ├─ expr.py
│  │        │  │  │  ├─ expressions.py
│  │        │  │  │  ├─ ops.py
│  │        │  │  │  ├─ parsing.py
│  │        │  │  │  ├─ pytables.py
│  │        │  │  │  ├─ scope.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ align.cpython-312.pyc
│  │        │  │  │     ├─ api.cpython-312.pyc
│  │        │  │  │     ├─ check.cpython-312.pyc
│  │        │  │  │     ├─ common.cpython-312.pyc
│  │        │  │  │     ├─ engines.cpython-312.pyc
│  │        │  │  │     ├─ eval.cpython-312.pyc
│  │        │  │  │     ├─ expr.cpython-312.pyc
│  │        │  │  │     ├─ expressions.cpython-312.pyc
│  │        │  │  │     ├─ ops.cpython-312.pyc
│  │        │  │  │     ├─ parsing.cpython-312.pyc
│  │        │  │  │     ├─ pytables.cpython-312.pyc
│  │        │  │  │     ├─ scope.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ config_init.py
│  │        │  │  ├─ construction.py
│  │        │  │  ├─ dtypes
│  │        │  │  │  ├─ api.py
│  │        │  │  │  ├─ astype.py
│  │        │  │  │  ├─ base.py
│  │        │  │  │  ├─ cast.py
│  │        │  │  │  ├─ common.py
│  │        │  │  │  ├─ concat.py
│  │        │  │  │  ├─ dtypes.py
│  │        │  │  │  ├─ generic.py
│  │        │  │  │  ├─ inference.py
│  │        │  │  │  ├─ missing.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ api.cpython-312.pyc
│  │        │  │  │     ├─ astype.cpython-312.pyc
│  │        │  │  │     ├─ base.cpython-312.pyc
│  │        │  │  │     ├─ cast.cpython-312.pyc
│  │        │  │  │     ├─ common.cpython-312.pyc
│  │        │  │  │     ├─ concat.cpython-312.pyc
│  │        │  │  │     ├─ dtypes.cpython-312.pyc
│  │        │  │  │     ├─ generic.cpython-312.pyc
│  │        │  │  │     ├─ inference.cpython-312.pyc
│  │        │  │  │     ├─ missing.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ flags.py
│  │        │  │  ├─ frame.py
│  │        │  │  ├─ generic.py
│  │        │  │  ├─ groupby
│  │        │  │  │  ├─ base.py
│  │        │  │  │  ├─ categorical.py
│  │        │  │  │  ├─ generic.py
│  │        │  │  │  ├─ groupby.py
│  │        │  │  │  ├─ grouper.py
│  │        │  │  │  ├─ indexing.py
│  │        │  │  │  ├─ numba_.py
│  │        │  │  │  ├─ ops.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ base.cpython-312.pyc
│  │        │  │  │     ├─ categorical.cpython-312.pyc
│  │        │  │  │     ├─ generic.cpython-312.pyc
│  │        │  │  │     ├─ groupby.cpython-312.pyc
│  │        │  │  │     ├─ grouper.cpython-312.pyc
│  │        │  │  │     ├─ indexing.cpython-312.pyc
│  │        │  │  │     ├─ numba_.cpython-312.pyc
│  │        │  │  │     ├─ ops.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ indexers
│  │        │  │  │  ├─ objects.py
│  │        │  │  │  ├─ utils.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ objects.cpython-312.pyc
│  │        │  │  │     ├─ utils.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ indexes
│  │        │  │  │  ├─ accessors.py
│  │        │  │  │  ├─ api.py
│  │        │  │  │  ├─ base.py
│  │        │  │  │  ├─ category.py
│  │        │  │  │  ├─ datetimelike.py
│  │        │  │  │  ├─ datetimes.py
│  │        │  │  │  ├─ extension.py
│  │        │  │  │  ├─ frozen.py
│  │        │  │  │  ├─ interval.py
│  │        │  │  │  ├─ multi.py
│  │        │  │  │  ├─ period.py
│  │        │  │  │  ├─ range.py
│  │        │  │  │  ├─ timedeltas.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ accessors.cpython-312.pyc
│  │        │  │  │     ├─ api.cpython-312.pyc
│  │        │  │  │     ├─ base.cpython-312.pyc
│  │        │  │  │     ├─ category.cpython-312.pyc
│  │        │  │  │     ├─ datetimelike.cpython-312.pyc
│  │        │  │  │     ├─ datetimes.cpython-312.pyc
│  │        │  │  │     ├─ extension.cpython-312.pyc
│  │        │  │  │     ├─ frozen.cpython-312.pyc
│  │        │  │  │     ├─ interval.cpython-312.pyc
│  │        │  │  │     ├─ multi.cpython-312.pyc
│  │        │  │  │     ├─ period.cpython-312.pyc
│  │        │  │  │     ├─ range.cpython-312.pyc
│  │        │  │  │     ├─ timedeltas.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ indexing.py
│  │        │  │  ├─ interchange
│  │        │  │  │  ├─ buffer.py
│  │        │  │  │  ├─ column.py
│  │        │  │  │  ├─ dataframe.py
│  │        │  │  │  ├─ dataframe_protocol.py
│  │        │  │  │  ├─ from_dataframe.py
│  │        │  │  │  ├─ utils.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ buffer.cpython-312.pyc
│  │        │  │  │     ├─ column.cpython-312.pyc
│  │        │  │  │     ├─ dataframe.cpython-312.pyc
│  │        │  │  │     ├─ dataframe_protocol.cpython-312.pyc
│  │        │  │  │     ├─ from_dataframe.cpython-312.pyc
│  │        │  │  │     ├─ utils.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ internals
│  │        │  │  │  ├─ api.py
│  │        │  │  │  ├─ array_manager.py
│  │        │  │  │  ├─ base.py
│  │        │  │  │  ├─ blocks.py
│  │        │  │  │  ├─ concat.py
│  │        │  │  │  ├─ construction.py
│  │        │  │  │  ├─ managers.py
│  │        │  │  │  ├─ ops.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ api.cpython-312.pyc
│  │        │  │  │     ├─ array_manager.cpython-312.pyc
│  │        │  │  │     ├─ base.cpython-312.pyc
│  │        │  │  │     ├─ blocks.cpython-312.pyc
│  │        │  │  │     ├─ concat.cpython-312.pyc
│  │        │  │  │     ├─ construction.cpython-312.pyc
│  │        │  │  │     ├─ managers.cpython-312.pyc
│  │        │  │  │     ├─ ops.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ methods
│  │        │  │  │  ├─ describe.py
│  │        │  │  │  ├─ selectn.py
│  │        │  │  │  ├─ to_dict.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ describe.cpython-312.pyc
│  │        │  │  │     ├─ selectn.cpython-312.pyc
│  │        │  │  │     ├─ to_dict.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ missing.py
│  │        │  │  ├─ nanops.py
│  │        │  │  ├─ ops
│  │        │  │  │  ├─ array_ops.py
│  │        │  │  │  ├─ common.py
│  │        │  │  │  ├─ dispatch.py
│  │        │  │  │  ├─ docstrings.py
│  │        │  │  │  ├─ invalid.py
│  │        │  │  │  ├─ mask_ops.py
│  │        │  │  │  ├─ missing.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ array_ops.cpython-312.pyc
│  │        │  │  │     ├─ common.cpython-312.pyc
│  │        │  │  │     ├─ dispatch.cpython-312.pyc
│  │        │  │  │     ├─ docstrings.cpython-312.pyc
│  │        │  │  │     ├─ invalid.cpython-312.pyc
│  │        │  │  │     ├─ mask_ops.cpython-312.pyc
│  │        │  │  │     ├─ missing.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ resample.py
│  │        │  │  ├─ reshape
│  │        │  │  │  ├─ api.py
│  │        │  │  │  ├─ concat.py
│  │        │  │  │  ├─ encoding.py
│  │        │  │  │  ├─ melt.py
│  │        │  │  │  ├─ merge.py
│  │        │  │  │  ├─ pivot.py
│  │        │  │  │  ├─ reshape.py
│  │        │  │  │  ├─ tile.py
│  │        │  │  │  ├─ util.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ api.cpython-312.pyc
│  │        │  │  │     ├─ concat.cpython-312.pyc
│  │        │  │  │     ├─ encoding.cpython-312.pyc
│  │        │  │  │     ├─ melt.cpython-312.pyc
│  │        │  │  │     ├─ merge.cpython-312.pyc
│  │        │  │  │     ├─ pivot.cpython-312.pyc
│  │        │  │  │     ├─ reshape.cpython-312.pyc
│  │        │  │  │     ├─ tile.cpython-312.pyc
│  │        │  │  │     ├─ util.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ roperator.py
│  │        │  │  ├─ sample.py
│  │        │  │  ├─ series.py
│  │        │  │  ├─ shared_docs.py
│  │        │  │  ├─ sorting.py
│  │        │  │  ├─ sparse
│  │        │  │  │  ├─ api.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ api.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ strings
│  │        │  │  │  ├─ accessor.py
│  │        │  │  │  ├─ base.py
│  │        │  │  │  ├─ object_array.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ accessor.cpython-312.pyc
│  │        │  │  │     ├─ base.cpython-312.pyc
│  │        │  │  │     ├─ object_array.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ tools
│  │        │  │  │  ├─ datetimes.py
│  │        │  │  │  ├─ numeric.py
│  │        │  │  │  ├─ timedeltas.py
│  │        │  │  │  ├─ times.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ datetimes.cpython-312.pyc
│  │        │  │  │     ├─ numeric.cpython-312.pyc
│  │        │  │  │     ├─ timedeltas.cpython-312.pyc
│  │        │  │  │     ├─ times.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ util
│  │        │  │  │  ├─ hashing.py
│  │        │  │  │  ├─ numba_.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ hashing.cpython-312.pyc
│  │        │  │  │     ├─ numba_.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ window
│  │        │  │  │  ├─ common.py
│  │        │  │  │  ├─ doc.py
│  │        │  │  │  ├─ ewm.py
│  │        │  │  │  ├─ expanding.py
│  │        │  │  │  ├─ numba_.py
│  │        │  │  │  ├─ online.py
│  │        │  │  │  ├─ rolling.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ common.cpython-312.pyc
│  │        │  │  │     ├─ doc.cpython-312.pyc
│  │        │  │  │     ├─ ewm.cpython-312.pyc
│  │        │  │  │     ├─ expanding.cpython-312.pyc
│  │        │  │  │     ├─ numba_.cpython-312.pyc
│  │        │  │  │     ├─ online.cpython-312.pyc
│  │        │  │  │     ├─ rolling.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _numba
│  │        │  │  │  ├─ executor.py
│  │        │  │  │  ├─ extensions.py
│  │        │  │  │  ├─ kernels
│  │        │  │  │  │  ├─ mean_.py
│  │        │  │  │  │  ├─ min_max_.py
│  │        │  │  │  │  ├─ shared.py
│  │        │  │  │  │  ├─ sum_.py
│  │        │  │  │  │  ├─ var_.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ mean_.cpython-312.pyc
│  │        │  │  │  │     ├─ min_max_.cpython-312.pyc
│  │        │  │  │  │     ├─ shared.cpython-312.pyc
│  │        │  │  │  │     ├─ sum_.cpython-312.pyc
│  │        │  │  │  │     ├─ var_.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ executor.cpython-312.pyc
│  │        │  │  │     ├─ extensions.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ accessor.cpython-312.pyc
│  │        │  │     ├─ algorithms.cpython-312.pyc
│  │        │  │     ├─ api.cpython-312.pyc
│  │        │  │     ├─ apply.cpython-312.pyc
│  │        │  │     ├─ arraylike.cpython-312.pyc
│  │        │  │     ├─ base.cpython-312.pyc
│  │        │  │     ├─ common.cpython-312.pyc
│  │        │  │     ├─ config_init.cpython-312.pyc
│  │        │  │     ├─ construction.cpython-312.pyc
│  │        │  │     ├─ flags.cpython-312.pyc
│  │        │  │     ├─ frame.cpython-312.pyc
│  │        │  │     ├─ generic.cpython-312.pyc
│  │        │  │     ├─ indexing.cpython-312.pyc
│  │        │  │     ├─ missing.cpython-312.pyc
│  │        │  │     ├─ nanops.cpython-312.pyc
│  │        │  │     ├─ resample.cpython-312.pyc
│  │        │  │     ├─ roperator.cpython-312.pyc
│  │        │  │     ├─ sample.cpython-312.pyc
│  │        │  │     ├─ series.cpython-312.pyc
│  │        │  │     ├─ shared_docs.cpython-312.pyc
│  │        │  │     ├─ sorting.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ errors
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ io
│  │        │  │  ├─ api.py
│  │        │  │  ├─ clipboard
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ clipboards.py
│  │        │  │  ├─ common.py
│  │        │  │  ├─ excel
│  │        │  │  │  ├─ _base.py
│  │        │  │  │  ├─ _calamine.py
│  │        │  │  │  ├─ _odfreader.py
│  │        │  │  │  ├─ _odswriter.py
│  │        │  │  │  ├─ _openpyxl.py
│  │        │  │  │  ├─ _pyxlsb.py
│  │        │  │  │  ├─ _util.py
│  │        │  │  │  ├─ _xlrd.py
│  │        │  │  │  ├─ _xlsxwriter.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ _base.cpython-312.pyc
│  │        │  │  │     ├─ _calamine.cpython-312.pyc
│  │        │  │  │     ├─ _odfreader.cpython-312.pyc
│  │        │  │  │     ├─ _odswriter.cpython-312.pyc
│  │        │  │  │     ├─ _openpyxl.cpython-312.pyc
│  │        │  │  │     ├─ _pyxlsb.cpython-312.pyc
│  │        │  │  │     ├─ _util.cpython-312.pyc
│  │        │  │  │     ├─ _xlrd.cpython-312.pyc
│  │        │  │  │     ├─ _xlsxwriter.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ feather_format.py
│  │        │  │  ├─ formats
│  │        │  │  │  ├─ console.py
│  │        │  │  │  ├─ css.py
│  │        │  │  │  ├─ csvs.py
│  │        │  │  │  ├─ excel.py
│  │        │  │  │  ├─ format.py
│  │        │  │  │  ├─ html.py
│  │        │  │  │  ├─ info.py
│  │        │  │  │  ├─ printing.py
│  │        │  │  │  ├─ string.py
│  │        │  │  │  ├─ style.py
│  │        │  │  │  ├─ style_render.py
│  │        │  │  │  ├─ templates
│  │        │  │  │  │  ├─ html.tpl
│  │        │  │  │  │  ├─ html_style.tpl
│  │        │  │  │  │  ├─ html_table.tpl
│  │        │  │  │  │  ├─ latex.tpl
│  │        │  │  │  │  ├─ latex_longtable.tpl
│  │        │  │  │  │  ├─ latex_table.tpl
│  │        │  │  │  │  └─ string.tpl
│  │        │  │  │  ├─ xml.py
│  │        │  │  │  ├─ _color_data.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ console.cpython-312.pyc
│  │        │  │  │     ├─ css.cpython-312.pyc
│  │        │  │  │     ├─ csvs.cpython-312.pyc
│  │        │  │  │     ├─ excel.cpython-312.pyc
│  │        │  │  │     ├─ format.cpython-312.pyc
│  │        │  │  │     ├─ html.cpython-312.pyc
│  │        │  │  │     ├─ info.cpython-312.pyc
│  │        │  │  │     ├─ printing.cpython-312.pyc
│  │        │  │  │     ├─ string.cpython-312.pyc
│  │        │  │  │     ├─ style.cpython-312.pyc
│  │        │  │  │     ├─ style_render.cpython-312.pyc
│  │        │  │  │     ├─ xml.cpython-312.pyc
│  │        │  │  │     ├─ _color_data.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ gbq.py
│  │        │  │  ├─ html.py
│  │        │  │  ├─ json
│  │        │  │  │  ├─ _json.py
│  │        │  │  │  ├─ _normalize.py
│  │        │  │  │  ├─ _table_schema.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ _json.cpython-312.pyc
│  │        │  │  │     ├─ _normalize.cpython-312.pyc
│  │        │  │  │     ├─ _table_schema.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ orc.py
│  │        │  │  ├─ parquet.py
│  │        │  │  ├─ parsers
│  │        │  │  │  ├─ arrow_parser_wrapper.py
│  │        │  │  │  ├─ base_parser.py
│  │        │  │  │  ├─ c_parser_wrapper.py
│  │        │  │  │  ├─ python_parser.py
│  │        │  │  │  ├─ readers.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ arrow_parser_wrapper.cpython-312.pyc
│  │        │  │  │     ├─ base_parser.cpython-312.pyc
│  │        │  │  │     ├─ c_parser_wrapper.cpython-312.pyc
│  │        │  │  │     ├─ python_parser.cpython-312.pyc
│  │        │  │  │     ├─ readers.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ pickle.py
│  │        │  │  ├─ pytables.py
│  │        │  │  ├─ sas
│  │        │  │  │  ├─ sas7bdat.py
│  │        │  │  │  ├─ sasreader.py
│  │        │  │  │  ├─ sas_constants.py
│  │        │  │  │  ├─ sas_xport.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ sas7bdat.cpython-312.pyc
│  │        │  │  │     ├─ sasreader.cpython-312.pyc
│  │        │  │  │     ├─ sas_constants.cpython-312.pyc
│  │        │  │  │     ├─ sas_xport.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ spss.py
│  │        │  │  ├─ sql.py
│  │        │  │  ├─ stata.py
│  │        │  │  ├─ xml.py
│  │        │  │  ├─ _util.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ api.cpython-312.pyc
│  │        │  │     ├─ clipboards.cpython-312.pyc
│  │        │  │     ├─ common.cpython-312.pyc
│  │        │  │     ├─ feather_format.cpython-312.pyc
│  │        │  │     ├─ gbq.cpython-312.pyc
│  │        │  │     ├─ html.cpython-312.pyc
│  │        │  │     ├─ orc.cpython-312.pyc
│  │        │  │     ├─ parquet.cpython-312.pyc
│  │        │  │     ├─ pickle.cpython-312.pyc
│  │        │  │     ├─ pytables.cpython-312.pyc
│  │        │  │     ├─ spss.cpython-312.pyc
│  │        │  │     ├─ sql.cpython-312.pyc
│  │        │  │     ├─ stata.cpython-312.pyc
│  │        │  │     ├─ xml.cpython-312.pyc
│  │        │  │     ├─ _util.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ plotting
│  │        │  │  ├─ _core.py
│  │        │  │  ├─ _matplotlib
│  │        │  │  │  ├─ boxplot.py
│  │        │  │  │  ├─ converter.py
│  │        │  │  │  ├─ core.py
│  │        │  │  │  ├─ groupby.py
│  │        │  │  │  ├─ hist.py
│  │        │  │  │  ├─ misc.py
│  │        │  │  │  ├─ style.py
│  │        │  │  │  ├─ timeseries.py
│  │        │  │  │  ├─ tools.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ boxplot.cpython-312.pyc
│  │        │  │  │     ├─ converter.cpython-312.pyc
│  │        │  │  │     ├─ core.cpython-312.pyc
│  │        │  │  │     ├─ groupby.cpython-312.pyc
│  │        │  │  │     ├─ hist.cpython-312.pyc
│  │        │  │  │     ├─ misc.cpython-312.pyc
│  │        │  │  │     ├─ style.cpython-312.pyc
│  │        │  │  │     ├─ timeseries.cpython-312.pyc
│  │        │  │  │     ├─ tools.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _misc.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ _core.cpython-312.pyc
│  │        │  │     ├─ _misc.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ pyproject.toml
│  │        │  ├─ testing.py
│  │        │  ├─ tests
│  │        │  │  ├─ api
│  │        │  │  │  ├─ test_api.py
│  │        │  │  │  ├─ test_types.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_api.cpython-312.pyc
│  │        │  │  │     ├─ test_types.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ apply
│  │        │  │  │  ├─ common.py
│  │        │  │  │  ├─ test_frame_apply.py
│  │        │  │  │  ├─ test_frame_apply_relabeling.py
│  │        │  │  │  ├─ test_frame_transform.py
│  │        │  │  │  ├─ test_invalid_arg.py
│  │        │  │  │  ├─ test_numba.py
│  │        │  │  │  ├─ test_series_apply.py
│  │        │  │  │  ├─ test_series_apply_relabeling.py
│  │        │  │  │  ├─ test_series_transform.py
│  │        │  │  │  ├─ test_str.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ common.cpython-312.pyc
│  │        │  │  │     ├─ test_frame_apply.cpython-312.pyc
│  │        │  │  │     ├─ test_frame_apply_relabeling.cpython-312.pyc
│  │        │  │  │     ├─ test_frame_transform.cpython-312.pyc
│  │        │  │  │     ├─ test_invalid_arg.cpython-312.pyc
│  │        │  │  │     ├─ test_numba.cpython-312.pyc
│  │        │  │  │     ├─ test_series_apply.cpython-312.pyc
│  │        │  │  │     ├─ test_series_apply_relabeling.cpython-312.pyc
│  │        │  │  │     ├─ test_series_transform.cpython-312.pyc
│  │        │  │  │     ├─ test_str.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ arithmetic
│  │        │  │  │  ├─ common.py
│  │        │  │  │  ├─ conftest.py
│  │        │  │  │  ├─ test_array_ops.py
│  │        │  │  │  ├─ test_categorical.py
│  │        │  │  │  ├─ test_datetime64.py
│  │        │  │  │  ├─ test_interval.py
│  │        │  │  │  ├─ test_numeric.py
│  │        │  │  │  ├─ test_object.py
│  │        │  │  │  ├─ test_period.py
│  │        │  │  │  ├─ test_timedelta64.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ common.cpython-312.pyc
│  │        │  │  │     ├─ conftest.cpython-312.pyc
│  │        │  │  │     ├─ test_array_ops.cpython-312.pyc
│  │        │  │  │     ├─ test_categorical.cpython-312.pyc
│  │        │  │  │     ├─ test_datetime64.cpython-312.pyc
│  │        │  │  │     ├─ test_interval.cpython-312.pyc
│  │        │  │  │     ├─ test_numeric.cpython-312.pyc
│  │        │  │  │     ├─ test_object.cpython-312.pyc
│  │        │  │  │     ├─ test_period.cpython-312.pyc
│  │        │  │  │     ├─ test_timedelta64.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ arrays
│  │        │  │  │  ├─ boolean
│  │        │  │  │  │  ├─ test_arithmetic.py
│  │        │  │  │  │  ├─ test_astype.py
│  │        │  │  │  │  ├─ test_comparison.py
│  │        │  │  │  │  ├─ test_construction.py
│  │        │  │  │  │  ├─ test_function.py
│  │        │  │  │  │  ├─ test_indexing.py
│  │        │  │  │  │  ├─ test_logical.py
│  │        │  │  │  │  ├─ test_ops.py
│  │        │  │  │  │  ├─ test_reduction.py
│  │        │  │  │  │  ├─ test_repr.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_arithmetic.cpython-312.pyc
│  │        │  │  │  │     ├─ test_astype.cpython-312.pyc
│  │        │  │  │  │     ├─ test_comparison.cpython-312.pyc
│  │        │  │  │  │     ├─ test_construction.cpython-312.pyc
│  │        │  │  │  │     ├─ test_function.cpython-312.pyc
│  │        │  │  │  │     ├─ test_indexing.cpython-312.pyc
│  │        │  │  │  │     ├─ test_logical.cpython-312.pyc
│  │        │  │  │  │     ├─ test_ops.cpython-312.pyc
│  │        │  │  │  │     ├─ test_reduction.cpython-312.pyc
│  │        │  │  │  │     ├─ test_repr.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ categorical
│  │        │  │  │  │  ├─ test_algos.py
│  │        │  │  │  │  ├─ test_analytics.py
│  │        │  │  │  │  ├─ test_api.py
│  │        │  │  │  │  ├─ test_astype.py
│  │        │  │  │  │  ├─ test_constructors.py
│  │        │  │  │  │  ├─ test_dtypes.py
│  │        │  │  │  │  ├─ test_indexing.py
│  │        │  │  │  │  ├─ test_map.py
│  │        │  │  │  │  ├─ test_missing.py
│  │        │  │  │  │  ├─ test_operators.py
│  │        │  │  │  │  ├─ test_replace.py
│  │        │  │  │  │  ├─ test_repr.py
│  │        │  │  │  │  ├─ test_sorting.py
│  │        │  │  │  │  ├─ test_subclass.py
│  │        │  │  │  │  ├─ test_take.py
│  │        │  │  │  │  ├─ test_warnings.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_algos.cpython-312.pyc
│  │        │  │  │  │     ├─ test_analytics.cpython-312.pyc
│  │        │  │  │  │     ├─ test_api.cpython-312.pyc
│  │        │  │  │  │     ├─ test_astype.cpython-312.pyc
│  │        │  │  │  │     ├─ test_constructors.cpython-312.pyc
│  │        │  │  │  │     ├─ test_dtypes.cpython-312.pyc
│  │        │  │  │  │     ├─ test_indexing.cpython-312.pyc
│  │        │  │  │  │     ├─ test_map.cpython-312.pyc
│  │        │  │  │  │     ├─ test_missing.cpython-312.pyc
│  │        │  │  │  │     ├─ test_operators.cpython-312.pyc
│  │        │  │  │  │     ├─ test_replace.cpython-312.pyc
│  │        │  │  │  │     ├─ test_repr.cpython-312.pyc
│  │        │  │  │  │     ├─ test_sorting.cpython-312.pyc
│  │        │  │  │  │     ├─ test_subclass.cpython-312.pyc
│  │        │  │  │  │     ├─ test_take.cpython-312.pyc
│  │        │  │  │  │     ├─ test_warnings.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ datetimes
│  │        │  │  │  │  ├─ test_constructors.py
│  │        │  │  │  │  ├─ test_cumulative.py
│  │        │  │  │  │  ├─ test_reductions.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_constructors.cpython-312.pyc
│  │        │  │  │  │     ├─ test_cumulative.cpython-312.pyc
│  │        │  │  │  │     ├─ test_reductions.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ floating
│  │        │  │  │  │  ├─ conftest.py
│  │        │  │  │  │  ├─ test_arithmetic.py
│  │        │  │  │  │  ├─ test_astype.py
│  │        │  │  │  │  ├─ test_comparison.py
│  │        │  │  │  │  ├─ test_concat.py
│  │        │  │  │  │  ├─ test_construction.py
│  │        │  │  │  │  ├─ test_contains.py
│  │        │  │  │  │  ├─ test_function.py
│  │        │  │  │  │  ├─ test_repr.py
│  │        │  │  │  │  ├─ test_to_numpy.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ conftest.cpython-312.pyc
│  │        │  │  │  │     ├─ test_arithmetic.cpython-312.pyc
│  │        │  │  │  │     ├─ test_astype.cpython-312.pyc
│  │        │  │  │  │     ├─ test_comparison.cpython-312.pyc
│  │        │  │  │  │     ├─ test_concat.cpython-312.pyc
│  │        │  │  │  │     ├─ test_construction.cpython-312.pyc
│  │        │  │  │  │     ├─ test_contains.cpython-312.pyc
│  │        │  │  │  │     ├─ test_function.cpython-312.pyc
│  │        │  │  │  │     ├─ test_repr.cpython-312.pyc
│  │        │  │  │  │     ├─ test_to_numpy.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ integer
│  │        │  │  │  │  ├─ conftest.py
│  │        │  │  │  │  ├─ test_arithmetic.py
│  │        │  │  │  │  ├─ test_comparison.py
│  │        │  │  │  │  ├─ test_concat.py
│  │        │  │  │  │  ├─ test_construction.py
│  │        │  │  │  │  ├─ test_dtypes.py
│  │        │  │  │  │  ├─ test_function.py
│  │        │  │  │  │  ├─ test_indexing.py
│  │        │  │  │  │  ├─ test_reduction.py
│  │        │  │  │  │  ├─ test_repr.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ conftest.cpython-312.pyc
│  │        │  │  │  │     ├─ test_arithmetic.cpython-312.pyc
│  │        │  │  │  │     ├─ test_comparison.cpython-312.pyc
│  │        │  │  │  │     ├─ test_concat.cpython-312.pyc
│  │        │  │  │  │     ├─ test_construction.cpython-312.pyc
│  │        │  │  │  │     ├─ test_dtypes.cpython-312.pyc
│  │        │  │  │  │     ├─ test_function.cpython-312.pyc
│  │        │  │  │  │     ├─ test_indexing.cpython-312.pyc
│  │        │  │  │  │     ├─ test_reduction.cpython-312.pyc
│  │        │  │  │  │     ├─ test_repr.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ interval
│  │        │  │  │  │  ├─ test_astype.py
│  │        │  │  │  │  ├─ test_formats.py
│  │        │  │  │  │  ├─ test_interval.py
│  │        │  │  │  │  ├─ test_interval_pyarrow.py
│  │        │  │  │  │  ├─ test_overlaps.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_astype.cpython-312.pyc
│  │        │  │  │  │     ├─ test_formats.cpython-312.pyc
│  │        │  │  │  │     ├─ test_interval.cpython-312.pyc
│  │        │  │  │  │     ├─ test_interval_pyarrow.cpython-312.pyc
│  │        │  │  │  │     ├─ test_overlaps.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ masked
│  │        │  │  │  │  ├─ test_arithmetic.py
│  │        │  │  │  │  ├─ test_arrow_compat.py
│  │        │  │  │  │  ├─ test_function.py
│  │        │  │  │  │  ├─ test_indexing.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_arithmetic.cpython-312.pyc
│  │        │  │  │  │     ├─ test_arrow_compat.cpython-312.pyc
│  │        │  │  │  │     ├─ test_function.cpython-312.pyc
│  │        │  │  │  │     ├─ test_indexing.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ masked_shared.py
│  │        │  │  │  ├─ numpy_
│  │        │  │  │  │  ├─ test_indexing.py
│  │        │  │  │  │  ├─ test_numpy.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_indexing.cpython-312.pyc
│  │        │  │  │  │     ├─ test_numpy.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ period
│  │        │  │  │  │  ├─ test_arrow_compat.py
│  │        │  │  │  │  ├─ test_astype.py
│  │        │  │  │  │  ├─ test_constructors.py
│  │        │  │  │  │  ├─ test_reductions.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_arrow_compat.cpython-312.pyc
│  │        │  │  │  │     ├─ test_astype.cpython-312.pyc
│  │        │  │  │  │     ├─ test_constructors.cpython-312.pyc
│  │        │  │  │  │     ├─ test_reductions.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ sparse
│  │        │  │  │  │  ├─ test_accessor.py
│  │        │  │  │  │  ├─ test_arithmetics.py
│  │        │  │  │  │  ├─ test_array.py
│  │        │  │  │  │  ├─ test_astype.py
│  │        │  │  │  │  ├─ test_combine_concat.py
│  │        │  │  │  │  ├─ test_constructors.py
│  │        │  │  │  │  ├─ test_dtype.py
│  │        │  │  │  │  ├─ test_indexing.py
│  │        │  │  │  │  ├─ test_libsparse.py
│  │        │  │  │  │  ├─ test_reductions.py
│  │        │  │  │  │  ├─ test_unary.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_accessor.cpython-312.pyc
│  │        │  │  │  │     ├─ test_arithmetics.cpython-312.pyc
│  │        │  │  │  │     ├─ test_array.cpython-312.pyc
│  │        │  │  │  │     ├─ test_astype.cpython-312.pyc
│  │        │  │  │  │     ├─ test_combine_concat.cpython-312.pyc
│  │        │  │  │  │     ├─ test_constructors.cpython-312.pyc
│  │        │  │  │  │     ├─ test_dtype.cpython-312.pyc
│  │        │  │  │  │     ├─ test_indexing.cpython-312.pyc
│  │        │  │  │  │     ├─ test_libsparse.cpython-312.pyc
│  │        │  │  │  │     ├─ test_reductions.cpython-312.pyc
│  │        │  │  │  │     ├─ test_unary.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ string_
│  │        │  │  │  │  ├─ test_string.py
│  │        │  │  │  │  ├─ test_string_arrow.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_string.cpython-312.pyc
│  │        │  │  │  │     ├─ test_string_arrow.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ test_array.py
│  │        │  │  │  ├─ test_datetimelike.py
│  │        │  │  │  ├─ test_datetimes.py
│  │        │  │  │  ├─ test_ndarray_backed.py
│  │        │  │  │  ├─ test_period.py
│  │        │  │  │  ├─ test_timedeltas.py
│  │        │  │  │  ├─ timedeltas
│  │        │  │  │  │  ├─ test_constructors.py
│  │        │  │  │  │  ├─ test_cumulative.py
│  │        │  │  │  │  ├─ test_reductions.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_constructors.cpython-312.pyc
│  │        │  │  │  │     ├─ test_cumulative.cpython-312.pyc
│  │        │  │  │  │     ├─ test_reductions.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ masked_shared.cpython-312.pyc
│  │        │  │  │     ├─ test_array.cpython-312.pyc
│  │        │  │  │     ├─ test_datetimelike.cpython-312.pyc
│  │        │  │  │     ├─ test_datetimes.cpython-312.pyc
│  │        │  │  │     ├─ test_ndarray_backed.cpython-312.pyc
│  │        │  │  │     ├─ test_period.cpython-312.pyc
│  │        │  │  │     ├─ test_timedeltas.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ base
│  │        │  │  │  ├─ common.py
│  │        │  │  │  ├─ test_constructors.py
│  │        │  │  │  ├─ test_conversion.py
│  │        │  │  │  ├─ test_fillna.py
│  │        │  │  │  ├─ test_misc.py
│  │        │  │  │  ├─ test_transpose.py
│  │        │  │  │  ├─ test_unique.py
│  │        │  │  │  ├─ test_value_counts.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ common.cpython-312.pyc
│  │        │  │  │     ├─ test_constructors.cpython-312.pyc
│  │        │  │  │     ├─ test_conversion.cpython-312.pyc
│  │        │  │  │     ├─ test_fillna.cpython-312.pyc
│  │        │  │  │     ├─ test_misc.cpython-312.pyc
│  │        │  │  │     ├─ test_transpose.cpython-312.pyc
│  │        │  │  │     ├─ test_unique.cpython-312.pyc
│  │        │  │  │     ├─ test_value_counts.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ computation
│  │        │  │  │  ├─ test_compat.py
│  │        │  │  │  ├─ test_eval.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_compat.cpython-312.pyc
│  │        │  │  │     ├─ test_eval.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ config
│  │        │  │  │  ├─ test_config.py
│  │        │  │  │  ├─ test_localization.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_config.cpython-312.pyc
│  │        │  │  │     ├─ test_localization.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ construction
│  │        │  │  │  ├─ test_extract_array.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_extract_array.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ copy_view
│  │        │  │  │  ├─ index
│  │        │  │  │  │  ├─ test_datetimeindex.py
│  │        │  │  │  │  ├─ test_index.py
│  │        │  │  │  │  ├─ test_periodindex.py
│  │        │  │  │  │  ├─ test_timedeltaindex.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_datetimeindex.cpython-312.pyc
│  │        │  │  │  │     ├─ test_index.cpython-312.pyc
│  │        │  │  │  │     ├─ test_periodindex.cpython-312.pyc
│  │        │  │  │  │     ├─ test_timedeltaindex.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ test_array.py
│  │        │  │  │  ├─ test_astype.py
│  │        │  │  │  ├─ test_chained_assignment_deprecation.py
│  │        │  │  │  ├─ test_clip.py
│  │        │  │  │  ├─ test_constructors.py
│  │        │  │  │  ├─ test_core_functionalities.py
│  │        │  │  │  ├─ test_functions.py
│  │        │  │  │  ├─ test_indexing.py
│  │        │  │  │  ├─ test_internals.py
│  │        │  │  │  ├─ test_interp_fillna.py
│  │        │  │  │  ├─ test_methods.py
│  │        │  │  │  ├─ test_replace.py
│  │        │  │  │  ├─ test_setitem.py
│  │        │  │  │  ├─ test_util.py
│  │        │  │  │  ├─ util.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_array.cpython-312.pyc
│  │        │  │  │     ├─ test_astype.cpython-312.pyc
│  │        │  │  │     ├─ test_chained_assignment_deprecation.cpython-312.pyc
│  │        │  │  │     ├─ test_clip.cpython-312.pyc
│  │        │  │  │     ├─ test_constructors.cpython-312.pyc
│  │        │  │  │     ├─ test_core_functionalities.cpython-312.pyc
│  │        │  │  │     ├─ test_functions.cpython-312.pyc
│  │        │  │  │     ├─ test_indexing.cpython-312.pyc
│  │        │  │  │     ├─ test_internals.cpython-312.pyc
│  │        │  │  │     ├─ test_interp_fillna.cpython-312.pyc
│  │        │  │  │     ├─ test_methods.cpython-312.pyc
│  │        │  │  │     ├─ test_replace.cpython-312.pyc
│  │        │  │  │     ├─ test_setitem.cpython-312.pyc
│  │        │  │  │     ├─ test_util.cpython-312.pyc
│  │        │  │  │     ├─ util.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ dtypes
│  │        │  │  │  ├─ cast
│  │        │  │  │  │  ├─ test_can_hold_element.py
│  │        │  │  │  │  ├─ test_construct_from_scalar.py
│  │        │  │  │  │  ├─ test_construct_ndarray.py
│  │        │  │  │  │  ├─ test_construct_object_arr.py
│  │        │  │  │  │  ├─ test_dict_compat.py
│  │        │  │  │  │  ├─ test_downcast.py
│  │        │  │  │  │  ├─ test_find_common_type.py
│  │        │  │  │  │  ├─ test_infer_datetimelike.py
│  │        │  │  │  │  ├─ test_infer_dtype.py
│  │        │  │  │  │  ├─ test_maybe_box_native.py
│  │        │  │  │  │  ├─ test_promote.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_can_hold_element.cpython-312.pyc
│  │        │  │  │  │     ├─ test_construct_from_scalar.cpython-312.pyc
│  │        │  │  │  │     ├─ test_construct_ndarray.cpython-312.pyc
│  │        │  │  │  │     ├─ test_construct_object_arr.cpython-312.pyc
│  │        │  │  │  │     ├─ test_dict_compat.cpython-312.pyc
│  │        │  │  │  │     ├─ test_downcast.cpython-312.pyc
│  │        │  │  │  │     ├─ test_find_common_type.cpython-312.pyc
│  │        │  │  │  │     ├─ test_infer_datetimelike.cpython-312.pyc
│  │        │  │  │  │     ├─ test_infer_dtype.cpython-312.pyc
│  │        │  │  │  │     ├─ test_maybe_box_native.cpython-312.pyc
│  │        │  │  │  │     ├─ test_promote.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ test_common.py
│  │        │  │  │  ├─ test_concat.py
│  │        │  │  │  ├─ test_dtypes.py
│  │        │  │  │  ├─ test_generic.py
│  │        │  │  │  ├─ test_inference.py
│  │        │  │  │  ├─ test_missing.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_common.cpython-312.pyc
│  │        │  │  │     ├─ test_concat.cpython-312.pyc
│  │        │  │  │     ├─ test_dtypes.cpython-312.pyc
│  │        │  │  │     ├─ test_generic.cpython-312.pyc
│  │        │  │  │     ├─ test_inference.cpython-312.pyc
│  │        │  │  │     ├─ test_missing.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ extension
│  │        │  │  │  ├─ array_with_attr
│  │        │  │  │  │  ├─ array.py
│  │        │  │  │  │  ├─ test_array_with_attr.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ array.cpython-312.pyc
│  │        │  │  │  │     ├─ test_array_with_attr.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ base
│  │        │  │  │  │  ├─ accumulate.py
│  │        │  │  │  │  ├─ base.py
│  │        │  │  │  │  ├─ casting.py
│  │        │  │  │  │  ├─ constructors.py
│  │        │  │  │  │  ├─ dim2.py
│  │        │  │  │  │  ├─ dtype.py
│  │        │  │  │  │  ├─ getitem.py
│  │        │  │  │  │  ├─ groupby.py
│  │        │  │  │  │  ├─ index.py
│  │        │  │  │  │  ├─ interface.py
│  │        │  │  │  │  ├─ io.py
│  │        │  │  │  │  ├─ methods.py
│  │        │  │  │  │  ├─ missing.py
│  │        │  │  │  │  ├─ ops.py
│  │        │  │  │  │  ├─ printing.py
│  │        │  │  │  │  ├─ reduce.py
│  │        │  │  │  │  ├─ reshaping.py
│  │        │  │  │  │  ├─ setitem.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ accumulate.cpython-312.pyc
│  │        │  │  │  │     ├─ base.cpython-312.pyc
│  │        │  │  │  │     ├─ casting.cpython-312.pyc
│  │        │  │  │  │     ├─ constructors.cpython-312.pyc
│  │        │  │  │  │     ├─ dim2.cpython-312.pyc
│  │        │  │  │  │     ├─ dtype.cpython-312.pyc
│  │        │  │  │  │     ├─ getitem.cpython-312.pyc
│  │        │  │  │  │     ├─ groupby.cpython-312.pyc
│  │        │  │  │  │     ├─ index.cpython-312.pyc
│  │        │  │  │  │     ├─ interface.cpython-312.pyc
│  │        │  │  │  │     ├─ io.cpython-312.pyc
│  │        │  │  │  │     ├─ methods.cpython-312.pyc
│  │        │  │  │  │     ├─ missing.cpython-312.pyc
│  │        │  │  │  │     ├─ ops.cpython-312.pyc
│  │        │  │  │  │     ├─ printing.cpython-312.pyc
│  │        │  │  │  │     ├─ reduce.cpython-312.pyc
│  │        │  │  │  │     ├─ reshaping.cpython-312.pyc
│  │        │  │  │  │     ├─ setitem.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ conftest.py
│  │        │  │  │  ├─ date
│  │        │  │  │  │  ├─ array.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ array.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ decimal
│  │        │  │  │  │  ├─ array.py
│  │        │  │  │  │  ├─ test_decimal.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ array.cpython-312.pyc
│  │        │  │  │  │     ├─ test_decimal.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ json
│  │        │  │  │  │  ├─ array.py
│  │        │  │  │  │  ├─ test_json.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ array.cpython-312.pyc
│  │        │  │  │  │     ├─ test_json.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ list
│  │        │  │  │  │  ├─ array.py
│  │        │  │  │  │  ├─ test_list.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ array.cpython-312.pyc
│  │        │  │  │  │     ├─ test_list.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ test_arrow.py
│  │        │  │  │  ├─ test_categorical.py
│  │        │  │  │  ├─ test_common.py
│  │        │  │  │  ├─ test_datetime.py
│  │        │  │  │  ├─ test_extension.py
│  │        │  │  │  ├─ test_interval.py
│  │        │  │  │  ├─ test_masked.py
│  │        │  │  │  ├─ test_numpy.py
│  │        │  │  │  ├─ test_period.py
│  │        │  │  │  ├─ test_sparse.py
│  │        │  │  │  ├─ test_string.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ conftest.cpython-312.pyc
│  │        │  │  │     ├─ test_arrow.cpython-312.pyc
│  │        │  │  │     ├─ test_categorical.cpython-312.pyc
│  │        │  │  │     ├─ test_common.cpython-312.pyc
│  │        │  │  │     ├─ test_datetime.cpython-312.pyc
│  │        │  │  │     ├─ test_extension.cpython-312.pyc
│  │        │  │  │     ├─ test_interval.cpython-312.pyc
│  │        │  │  │     ├─ test_masked.cpython-312.pyc
│  │        │  │  │     ├─ test_numpy.cpython-312.pyc
│  │        │  │  │     ├─ test_period.cpython-312.pyc
│  │        │  │  │     ├─ test_sparse.cpython-312.pyc
│  │        │  │  │     ├─ test_string.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ frame
│  │        │  │  │  ├─ common.py
│  │        │  │  │  ├─ conftest.py
│  │        │  │  │  ├─ constructors
│  │        │  │  │  │  ├─ test_from_dict.py
│  │        │  │  │  │  ├─ test_from_records.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_from_dict.cpython-312.pyc
│  │        │  │  │  │     ├─ test_from_records.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ indexing
│  │        │  │  │  │  ├─ test_coercion.py
│  │        │  │  │  │  ├─ test_delitem.py
│  │        │  │  │  │  ├─ test_get.py
│  │        │  │  │  │  ├─ test_getitem.py
│  │        │  │  │  │  ├─ test_get_value.py
│  │        │  │  │  │  ├─ test_indexing.py
│  │        │  │  │  │  ├─ test_insert.py
│  │        │  │  │  │  ├─ test_mask.py
│  │        │  │  │  │  ├─ test_setitem.py
│  │        │  │  │  │  ├─ test_set_value.py
│  │        │  │  │  │  ├─ test_take.py
│  │        │  │  │  │  ├─ test_where.py
│  │        │  │  │  │  ├─ test_xs.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_coercion.cpython-312.pyc
│  │        │  │  │  │     ├─ test_delitem.cpython-312.pyc
│  │        │  │  │  │     ├─ test_get.cpython-312.pyc
│  │        │  │  │  │     ├─ test_getitem.cpython-312.pyc
│  │        │  │  │  │     ├─ test_get_value.cpython-312.pyc
│  │        │  │  │  │     ├─ test_indexing.cpython-312.pyc
│  │        │  │  │  │     ├─ test_insert.cpython-312.pyc
│  │        │  │  │  │     ├─ test_mask.cpython-312.pyc
│  │        │  │  │  │     ├─ test_setitem.cpython-312.pyc
│  │        │  │  │  │     ├─ test_set_value.cpython-312.pyc
│  │        │  │  │  │     ├─ test_take.cpython-312.pyc
│  │        │  │  │  │     ├─ test_where.cpython-312.pyc
│  │        │  │  │  │     ├─ test_xs.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ methods
│  │        │  │  │  │  ├─ test_add_prefix_suffix.py
│  │        │  │  │  │  ├─ test_align.py
│  │        │  │  │  │  ├─ test_asfreq.py
│  │        │  │  │  │  ├─ test_asof.py
│  │        │  │  │  │  ├─ test_assign.py
│  │        │  │  │  │  ├─ test_astype.py
│  │        │  │  │  │  ├─ test_at_time.py
│  │        │  │  │  │  ├─ test_between_time.py
│  │        │  │  │  │  ├─ test_clip.py
│  │        │  │  │  │  ├─ test_combine.py
│  │        │  │  │  │  ├─ test_combine_first.py
│  │        │  │  │  │  ├─ test_compare.py
│  │        │  │  │  │  ├─ test_convert_dtypes.py
│  │        │  │  │  │  ├─ test_copy.py
│  │        │  │  │  │  ├─ test_count.py
│  │        │  │  │  │  ├─ test_cov_corr.py
│  │        │  │  │  │  ├─ test_describe.py
│  │        │  │  │  │  ├─ test_diff.py
│  │        │  │  │  │  ├─ test_dot.py
│  │        │  │  │  │  ├─ test_drop.py
│  │        │  │  │  │  ├─ test_droplevel.py
│  │        │  │  │  │  ├─ test_dropna.py
│  │        │  │  │  │  ├─ test_drop_duplicates.py
│  │        │  │  │  │  ├─ test_dtypes.py
│  │        │  │  │  │  ├─ test_duplicated.py
│  │        │  │  │  │  ├─ test_equals.py
│  │        │  │  │  │  ├─ test_explode.py
│  │        │  │  │  │  ├─ test_fillna.py
│  │        │  │  │  │  ├─ test_filter.py
│  │        │  │  │  │  ├─ test_first_and_last.py
│  │        │  │  │  │  ├─ test_first_valid_index.py
│  │        │  │  │  │  ├─ test_get_numeric_data.py
│  │        │  │  │  │  ├─ test_head_tail.py
│  │        │  │  │  │  ├─ test_infer_objects.py
│  │        │  │  │  │  ├─ test_info.py
│  │        │  │  │  │  ├─ test_interpolate.py
│  │        │  │  │  │  ├─ test_isetitem.py
│  │        │  │  │  │  ├─ test_isin.py
│  │        │  │  │  │  ├─ test_is_homogeneous_dtype.py
│  │        │  │  │  │  ├─ test_iterrows.py
│  │        │  │  │  │  ├─ test_join.py
│  │        │  │  │  │  ├─ test_map.py
│  │        │  │  │  │  ├─ test_matmul.py
│  │        │  │  │  │  ├─ test_nlargest.py
│  │        │  │  │  │  ├─ test_pct_change.py
│  │        │  │  │  │  ├─ test_pipe.py
│  │        │  │  │  │  ├─ test_pop.py
│  │        │  │  │  │  ├─ test_quantile.py
│  │        │  │  │  │  ├─ test_rank.py
│  │        │  │  │  │  ├─ test_reindex.py
│  │        │  │  │  │  ├─ test_reindex_like.py
│  │        │  │  │  │  ├─ test_rename.py
│  │        │  │  │  │  ├─ test_rename_axis.py
│  │        │  │  │  │  ├─ test_reorder_levels.py
│  │        │  │  │  │  ├─ test_replace.py
│  │        │  │  │  │  ├─ test_reset_index.py
│  │        │  │  │  │  ├─ test_round.py
│  │        │  │  │  │  ├─ test_sample.py
│  │        │  │  │  │  ├─ test_select_dtypes.py
│  │        │  │  │  │  ├─ test_set_axis.py
│  │        │  │  │  │  ├─ test_set_index.py
│  │        │  │  │  │  ├─ test_shift.py
│  │        │  │  │  │  ├─ test_size.py
│  │        │  │  │  │  ├─ test_sort_index.py
│  │        │  │  │  │  ├─ test_sort_values.py
│  │        │  │  │  │  ├─ test_swapaxes.py
│  │        │  │  │  │  ├─ test_swaplevel.py
│  │        │  │  │  │  ├─ test_to_csv.py
│  │        │  │  │  │  ├─ test_to_dict.py
│  │        │  │  │  │  ├─ test_to_dict_of_blocks.py
│  │        │  │  │  │  ├─ test_to_numpy.py
│  │        │  │  │  │  ├─ test_to_period.py
│  │        │  │  │  │  ├─ test_to_records.py
│  │        │  │  │  │  ├─ test_to_timestamp.py
│  │        │  │  │  │  ├─ test_transpose.py
│  │        │  │  │  │  ├─ test_truncate.py
│  │        │  │  │  │  ├─ test_tz_convert.py
│  │        │  │  │  │  ├─ test_tz_localize.py
│  │        │  │  │  │  ├─ test_update.py
│  │        │  │  │  │  ├─ test_values.py
│  │        │  │  │  │  ├─ test_value_counts.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_add_prefix_suffix.cpython-312.pyc
│  │        │  │  │  │     ├─ test_align.cpython-312.pyc
│  │        │  │  │  │     ├─ test_asfreq.cpython-312.pyc
│  │        │  │  │  │     ├─ test_asof.cpython-312.pyc
│  │        │  │  │  │     ├─ test_assign.cpython-312.pyc
│  │        │  │  │  │     ├─ test_astype.cpython-312.pyc
│  │        │  │  │  │     ├─ test_at_time.cpython-312.pyc
│  │        │  │  │  │     ├─ test_between_time.cpython-312.pyc
│  │        │  │  │  │     ├─ test_clip.cpython-312.pyc
│  │        │  │  │  │     ├─ test_combine.cpython-312.pyc
│  │        │  │  │  │     ├─ test_combine_first.cpython-312.pyc
│  │        │  │  │  │     ├─ test_compare.cpython-312.pyc
│  │        │  │  │  │     ├─ test_convert_dtypes.cpython-312.pyc
│  │        │  │  │  │     ├─ test_copy.cpython-312.pyc
│  │        │  │  │  │     ├─ test_count.cpython-312.pyc
│  │        │  │  │  │     ├─ test_cov_corr.cpython-312.pyc
│  │        │  │  │  │     ├─ test_describe.cpython-312.pyc
│  │        │  │  │  │     ├─ test_diff.cpython-312.pyc
│  │        │  │  │  │     ├─ test_dot.cpython-312.pyc
│  │        │  │  │  │     ├─ test_drop.cpython-312.pyc
│  │        │  │  │  │     ├─ test_droplevel.cpython-312.pyc
│  │        │  │  │  │     ├─ test_dropna.cpython-312.pyc
│  │        │  │  │  │     ├─ test_drop_duplicates.cpython-312.pyc
│  │        │  │  │  │     ├─ test_dtypes.cpython-312.pyc
│  │        │  │  │  │     ├─ test_duplicated.cpython-312.pyc
│  │        │  │  │  │     ├─ test_equals.cpython-312.pyc
│  │        │  │  │  │     ├─ test_explode.cpython-312.pyc
│  │        │  │  │  │     ├─ test_fillna.cpython-312.pyc
│  │        │  │  │  │     ├─ test_filter.cpython-312.pyc
│  │        │  │  │  │     ├─ test_first_and_last.cpython-312.pyc
│  │        │  │  │  │     ├─ test_first_valid_index.cpython-312.pyc
│  │        │  │  │  │     ├─ test_get_numeric_data.cpython-312.pyc
│  │        │  │  │  │     ├─ test_head_tail.cpython-312.pyc
│  │        │  │  │  │     ├─ test_infer_objects.cpython-312.pyc
│  │        │  │  │  │     ├─ test_info.cpython-312.pyc
│  │        │  │  │  │     ├─ test_interpolate.cpython-312.pyc
│  │        │  │  │  │     ├─ test_isetitem.cpython-312.pyc
│  │        │  │  │  │     ├─ test_isin.cpython-312.pyc
│  │        │  │  │  │     ├─ test_is_homogeneous_dtype.cpython-312.pyc
│  │        │  │  │  │     ├─ test_iterrows.cpython-312.pyc
│  │        │  │  │  │     ├─ test_join.cpython-312.pyc
│  │        │  │  │  │     ├─ test_map.cpython-312.pyc
│  │        │  │  │  │     ├─ test_matmul.cpython-312.pyc
│  │        │  │  │  │     ├─ test_nlargest.cpython-312.pyc
│  │        │  │  │  │     ├─ test_pct_change.cpython-312.pyc
│  │        │  │  │  │     ├─ test_pipe.cpython-312.pyc
│  │        │  │  │  │     ├─ test_pop.cpython-312.pyc
│  │        │  │  │  │     ├─ test_quantile.cpython-312.pyc
│  │        │  │  │  │     ├─ test_rank.cpython-312.pyc
│  │        │  │  │  │     ├─ test_reindex.cpython-312.pyc
│  │        │  │  │  │     ├─ test_reindex_like.cpython-312.pyc
│  │        │  │  │  │     ├─ test_rename.cpython-312.pyc
│  │        │  │  │  │     ├─ test_rename_axis.cpython-312.pyc
│  │        │  │  │  │     ├─ test_reorder_levels.cpython-312.pyc
│  │        │  │  │  │     ├─ test_replace.cpython-312.pyc
│  │        │  │  │  │     ├─ test_reset_index.cpython-312.pyc
│  │        │  │  │  │     ├─ test_round.cpython-312.pyc
│  │        │  │  │  │     ├─ test_sample.cpython-312.pyc
│  │        │  │  │  │     ├─ test_select_dtypes.cpython-312.pyc
│  │        │  │  │  │     ├─ test_set_axis.cpython-312.pyc
│  │        │  │  │  │     ├─ test_set_index.cpython-312.pyc
│  │        │  │  │  │     ├─ test_shift.cpython-312.pyc
│  │        │  │  │  │     ├─ test_size.cpython-312.pyc
│  │        │  │  │  │     ├─ test_sort_index.cpython-312.pyc
│  │        │  │  │  │     ├─ test_sort_values.cpython-312.pyc
│  │        │  │  │  │     ├─ test_swapaxes.cpython-312.pyc
│  │        │  │  │  │     ├─ test_swaplevel.cpython-312.pyc
│  │        │  │  │  │     ├─ test_to_csv.cpython-312.pyc
│  │        │  │  │  │     ├─ test_to_dict.cpython-312.pyc
│  │        │  │  │  │     ├─ test_to_dict_of_blocks.cpython-312.pyc
│  │        │  │  │  │     ├─ test_to_numpy.cpython-312.pyc
│  │        │  │  │  │     ├─ test_to_period.cpython-312.pyc
│  │        │  │  │  │     ├─ test_to_records.cpython-312.pyc
│  │        │  │  │  │     ├─ test_to_timestamp.cpython-312.pyc
│  │        │  │  │  │     ├─ test_transpose.cpython-312.pyc
│  │        │  │  │  │     ├─ test_truncate.cpython-312.pyc
│  │        │  │  │  │     ├─ test_tz_convert.cpython-312.pyc
│  │        │  │  │  │     ├─ test_tz_localize.cpython-312.pyc
│  │        │  │  │  │     ├─ test_update.cpython-312.pyc
│  │        │  │  │  │     ├─ test_values.cpython-312.pyc
│  │        │  │  │  │     ├─ test_value_counts.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ test_alter_axes.py
│  │        │  │  │  ├─ test_api.py
│  │        │  │  │  ├─ test_arithmetic.py
│  │        │  │  │  ├─ test_arrow_interface.py
│  │        │  │  │  ├─ test_block_internals.py
│  │        │  │  │  ├─ test_constructors.py
│  │        │  │  │  ├─ test_cumulative.py
│  │        │  │  │  ├─ test_iteration.py
│  │        │  │  │  ├─ test_logical_ops.py
│  │        │  │  │  ├─ test_nonunique_indexes.py
│  │        │  │  │  ├─ test_npfuncs.py
│  │        │  │  │  ├─ test_query_eval.py
│  │        │  │  │  ├─ test_reductions.py
│  │        │  │  │  ├─ test_repr.py
│  │        │  │  │  ├─ test_stack_unstack.py
│  │        │  │  │  ├─ test_subclass.py
│  │        │  │  │  ├─ test_ufunc.py
│  │        │  │  │  ├─ test_unary.py
│  │        │  │  │  ├─ test_validate.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ common.cpython-312.pyc
│  │        │  │  │     ├─ conftest.cpython-312.pyc
│  │        │  │  │     ├─ test_alter_axes.cpython-312.pyc
│  │        │  │  │     ├─ test_api.cpython-312.pyc
│  │        │  │  │     ├─ test_arithmetic.cpython-312.pyc
│  │        │  │  │     ├─ test_arrow_interface.cpython-312.pyc
│  │        │  │  │     ├─ test_block_internals.cpython-312.pyc
│  │        │  │  │     ├─ test_constructors.cpython-312.pyc
│  │        │  │  │     ├─ test_cumulative.cpython-312.pyc
│  │        │  │  │     ├─ test_iteration.cpython-312.pyc
│  │        │  │  │     ├─ test_logical_ops.cpython-312.pyc
│  │        │  │  │     ├─ test_nonunique_indexes.cpython-312.pyc
│  │        │  │  │     ├─ test_npfuncs.cpython-312.pyc
│  │        │  │  │     ├─ test_query_eval.cpython-312.pyc
│  │        │  │  │     ├─ test_reductions.cpython-312.pyc
│  │        │  │  │     ├─ test_repr.cpython-312.pyc
│  │        │  │  │     ├─ test_stack_unstack.cpython-312.pyc
│  │        │  │  │     ├─ test_subclass.cpython-312.pyc
│  │        │  │  │     ├─ test_ufunc.cpython-312.pyc
│  │        │  │  │     ├─ test_unary.cpython-312.pyc
│  │        │  │  │     ├─ test_validate.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ generic
│  │        │  │  │  ├─ test_duplicate_labels.py
│  │        │  │  │  ├─ test_finalize.py
│  │        │  │  │  ├─ test_frame.py
│  │        │  │  │  ├─ test_generic.py
│  │        │  │  │  ├─ test_label_or_level_utils.py
│  │        │  │  │  ├─ test_series.py
│  │        │  │  │  ├─ test_to_xarray.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_duplicate_labels.cpython-312.pyc
│  │        │  │  │     ├─ test_finalize.cpython-312.pyc
│  │        │  │  │     ├─ test_frame.cpython-312.pyc
│  │        │  │  │     ├─ test_generic.cpython-312.pyc
│  │        │  │  │     ├─ test_label_or_level_utils.cpython-312.pyc
│  │        │  │  │     ├─ test_series.cpython-312.pyc
│  │        │  │  │     ├─ test_to_xarray.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ groupby
│  │        │  │  │  ├─ aggregate
│  │        │  │  │  │  ├─ test_aggregate.py
│  │        │  │  │  │  ├─ test_cython.py
│  │        │  │  │  │  ├─ test_numba.py
│  │        │  │  │  │  ├─ test_other.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_aggregate.cpython-312.pyc
│  │        │  │  │  │     ├─ test_cython.cpython-312.pyc
│  │        │  │  │  │     ├─ test_numba.cpython-312.pyc
│  │        │  │  │  │     ├─ test_other.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ conftest.py
│  │        │  │  │  ├─ methods
│  │        │  │  │  │  ├─ test_corrwith.py
│  │        │  │  │  │  ├─ test_describe.py
│  │        │  │  │  │  ├─ test_groupby_shift_diff.py
│  │        │  │  │  │  ├─ test_is_monotonic.py
│  │        │  │  │  │  ├─ test_nlargest_nsmallest.py
│  │        │  │  │  │  ├─ test_nth.py
│  │        │  │  │  │  ├─ test_quantile.py
│  │        │  │  │  │  ├─ test_rank.py
│  │        │  │  │  │  ├─ test_sample.py
│  │        │  │  │  │  ├─ test_size.py
│  │        │  │  │  │  ├─ test_skew.py
│  │        │  │  │  │  ├─ test_value_counts.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_corrwith.cpython-312.pyc
│  │        │  │  │  │     ├─ test_describe.cpython-312.pyc
│  │        │  │  │  │     ├─ test_groupby_shift_diff.cpython-312.pyc
│  │        │  │  │  │     ├─ test_is_monotonic.cpython-312.pyc
│  │        │  │  │  │     ├─ test_nlargest_nsmallest.cpython-312.pyc
│  │        │  │  │  │     ├─ test_nth.cpython-312.pyc
│  │        │  │  │  │     ├─ test_quantile.cpython-312.pyc
│  │        │  │  │  │     ├─ test_rank.cpython-312.pyc
│  │        │  │  │  │     ├─ test_sample.cpython-312.pyc
│  │        │  │  │  │     ├─ test_size.cpython-312.pyc
│  │        │  │  │  │     ├─ test_skew.cpython-312.pyc
│  │        │  │  │  │     ├─ test_value_counts.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ test_all_methods.py
│  │        │  │  │  ├─ test_api.py
│  │        │  │  │  ├─ test_apply.py
│  │        │  │  │  ├─ test_apply_mutate.py
│  │        │  │  │  ├─ test_bin_groupby.py
│  │        │  │  │  ├─ test_categorical.py
│  │        │  │  │  ├─ test_counting.py
│  │        │  │  │  ├─ test_cumulative.py
│  │        │  │  │  ├─ test_filters.py
│  │        │  │  │  ├─ test_groupby.py
│  │        │  │  │  ├─ test_groupby_dropna.py
│  │        │  │  │  ├─ test_groupby_subclass.py
│  │        │  │  │  ├─ test_grouping.py
│  │        │  │  │  ├─ test_indexing.py
│  │        │  │  │  ├─ test_index_as_string.py
│  │        │  │  │  ├─ test_libgroupby.py
│  │        │  │  │  ├─ test_missing.py
│  │        │  │  │  ├─ test_numba.py
│  │        │  │  │  ├─ test_numeric_only.py
│  │        │  │  │  ├─ test_pipe.py
│  │        │  │  │  ├─ test_raises.py
│  │        │  │  │  ├─ test_reductions.py
│  │        │  │  │  ├─ test_timegrouper.py
│  │        │  │  │  ├─ transform
│  │        │  │  │  │  ├─ test_numba.py
│  │        │  │  │  │  ├─ test_transform.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_numba.cpython-312.pyc
│  │        │  │  │  │     ├─ test_transform.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ conftest.cpython-312.pyc
│  │        │  │  │     ├─ test_all_methods.cpython-312.pyc
│  │        │  │  │     ├─ test_api.cpython-312.pyc
│  │        │  │  │     ├─ test_apply.cpython-312.pyc
│  │        │  │  │     ├─ test_apply_mutate.cpython-312.pyc
│  │        │  │  │     ├─ test_bin_groupby.cpython-312.pyc
│  │        │  │  │     ├─ test_categorical.cpython-312.pyc
│  │        │  │  │     ├─ test_counting.cpython-312.pyc
│  │        │  │  │     ├─ test_cumulative.cpython-312.pyc
│  │        │  │  │     ├─ test_filters.cpython-312.pyc
│  │        │  │  │     ├─ test_groupby.cpython-312.pyc
│  │        │  │  │     ├─ test_groupby_dropna.cpython-312.pyc
│  │        │  │  │     ├─ test_groupby_subclass.cpython-312.pyc
│  │        │  │  │     ├─ test_grouping.cpython-312.pyc
│  │        │  │  │     ├─ test_indexing.cpython-312.pyc
│  │        │  │  │     ├─ test_index_as_string.cpython-312.pyc
│  │        │  │  │     ├─ test_libgroupby.cpython-312.pyc
│  │        │  │  │     ├─ test_missing.cpython-312.pyc
│  │        │  │  │     ├─ test_numba.cpython-312.pyc
│  │        │  │  │     ├─ test_numeric_only.cpython-312.pyc
│  │        │  │  │     ├─ test_pipe.cpython-312.pyc
│  │        │  │  │     ├─ test_raises.cpython-312.pyc
│  │        │  │  │     ├─ test_reductions.cpython-312.pyc
│  │        │  │  │     ├─ test_timegrouper.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ indexes
│  │        │  │  │  ├─ base_class
│  │        │  │  │  │  ├─ test_constructors.py
│  │        │  │  │  │  ├─ test_formats.py
│  │        │  │  │  │  ├─ test_indexing.py
│  │        │  │  │  │  ├─ test_pickle.py
│  │        │  │  │  │  ├─ test_reshape.py
│  │        │  │  │  │  ├─ test_setops.py
│  │        │  │  │  │  ├─ test_where.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_constructors.cpython-312.pyc
│  │        │  │  │  │     ├─ test_formats.cpython-312.pyc
│  │        │  │  │  │     ├─ test_indexing.cpython-312.pyc
│  │        │  │  │  │     ├─ test_pickle.cpython-312.pyc
│  │        │  │  │  │     ├─ test_reshape.cpython-312.pyc
│  │        │  │  │  │     ├─ test_setops.cpython-312.pyc
│  │        │  │  │  │     ├─ test_where.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ categorical
│  │        │  │  │  │  ├─ test_append.py
│  │        │  │  │  │  ├─ test_astype.py
│  │        │  │  │  │  ├─ test_category.py
│  │        │  │  │  │  ├─ test_constructors.py
│  │        │  │  │  │  ├─ test_equals.py
│  │        │  │  │  │  ├─ test_fillna.py
│  │        │  │  │  │  ├─ test_formats.py
│  │        │  │  │  │  ├─ test_indexing.py
│  │        │  │  │  │  ├─ test_map.py
│  │        │  │  │  │  ├─ test_reindex.py
│  │        │  │  │  │  ├─ test_setops.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_append.cpython-312.pyc
│  │        │  │  │  │     ├─ test_astype.cpython-312.pyc
│  │        │  │  │  │     ├─ test_category.cpython-312.pyc
│  │        │  │  │  │     ├─ test_constructors.cpython-312.pyc
│  │        │  │  │  │     ├─ test_equals.cpython-312.pyc
│  │        │  │  │  │     ├─ test_fillna.cpython-312.pyc
│  │        │  │  │  │     ├─ test_formats.cpython-312.pyc
│  │        │  │  │  │     ├─ test_indexing.cpython-312.pyc
│  │        │  │  │  │     ├─ test_map.cpython-312.pyc
│  │        │  │  │  │     ├─ test_reindex.cpython-312.pyc
│  │        │  │  │  │     ├─ test_setops.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ conftest.py
│  │        │  │  │  ├─ datetimelike_
│  │        │  │  │  │  ├─ test_drop_duplicates.py
│  │        │  │  │  │  ├─ test_equals.py
│  │        │  │  │  │  ├─ test_indexing.py
│  │        │  │  │  │  ├─ test_is_monotonic.py
│  │        │  │  │  │  ├─ test_nat.py
│  │        │  │  │  │  ├─ test_sort_values.py
│  │        │  │  │  │  ├─ test_value_counts.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_drop_duplicates.cpython-312.pyc
│  │        │  │  │  │     ├─ test_equals.cpython-312.pyc
│  │        │  │  │  │     ├─ test_indexing.cpython-312.pyc
│  │        │  │  │  │     ├─ test_is_monotonic.cpython-312.pyc
│  │        │  │  │  │     ├─ test_nat.cpython-312.pyc
│  │        │  │  │  │     ├─ test_sort_values.cpython-312.pyc
│  │        │  │  │  │     ├─ test_value_counts.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ datetimes
│  │        │  │  │  │  ├─ methods
│  │        │  │  │  │  │  ├─ test_asof.py
│  │        │  │  │  │  │  ├─ test_astype.py
│  │        │  │  │  │  │  ├─ test_delete.py
│  │        │  │  │  │  │  ├─ test_factorize.py
│  │        │  │  │  │  │  ├─ test_fillna.py
│  │        │  │  │  │  │  ├─ test_insert.py
│  │        │  │  │  │  │  ├─ test_isocalendar.py
│  │        │  │  │  │  │  ├─ test_map.py
│  │        │  │  │  │  │  ├─ test_normalize.py
│  │        │  │  │  │  │  ├─ test_repeat.py
│  │        │  │  │  │  │  ├─ test_resolution.py
│  │        │  │  │  │  │  ├─ test_round.py
│  │        │  │  │  │  │  ├─ test_shift.py
│  │        │  │  │  │  │  ├─ test_snap.py
│  │        │  │  │  │  │  ├─ test_to_frame.py
│  │        │  │  │  │  │  ├─ test_to_julian_date.py
│  │        │  │  │  │  │  ├─ test_to_period.py
│  │        │  │  │  │  │  ├─ test_to_pydatetime.py
│  │        │  │  │  │  │  ├─ test_to_series.py
│  │        │  │  │  │  │  ├─ test_tz_convert.py
│  │        │  │  │  │  │  ├─ test_tz_localize.py
│  │        │  │  │  │  │  ├─ test_unique.py
│  │        │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │     ├─ test_asof.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_astype.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_delete.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_factorize.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_fillna.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_insert.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_isocalendar.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_map.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_normalize.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_repeat.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_resolution.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_round.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_shift.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_snap.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_to_frame.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_to_julian_date.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_to_period.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_to_pydatetime.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_to_series.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_tz_convert.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_tz_localize.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_unique.cpython-312.pyc
│  │        │  │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  │  ├─ test_arithmetic.py
│  │        │  │  │  │  ├─ test_constructors.py
│  │        │  │  │  │  ├─ test_datetime.py
│  │        │  │  │  │  ├─ test_date_range.py
│  │        │  │  │  │  ├─ test_formats.py
│  │        │  │  │  │  ├─ test_freq_attr.py
│  │        │  │  │  │  ├─ test_indexing.py
│  │        │  │  │  │  ├─ test_iter.py
│  │        │  │  │  │  ├─ test_join.py
│  │        │  │  │  │  ├─ test_npfuncs.py
│  │        │  │  │  │  ├─ test_ops.py
│  │        │  │  │  │  ├─ test_partial_slicing.py
│  │        │  │  │  │  ├─ test_pickle.py
│  │        │  │  │  │  ├─ test_reindex.py
│  │        │  │  │  │  ├─ test_scalar_compat.py
│  │        │  │  │  │  ├─ test_setops.py
│  │        │  │  │  │  ├─ test_timezones.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_arithmetic.cpython-312.pyc
│  │        │  │  │  │     ├─ test_constructors.cpython-312.pyc
│  │        │  │  │  │     ├─ test_datetime.cpython-312.pyc
│  │        │  │  │  │     ├─ test_date_range.cpython-312.pyc
│  │        │  │  │  │     ├─ test_formats.cpython-312.pyc
│  │        │  │  │  │     ├─ test_freq_attr.cpython-312.pyc
│  │        │  │  │  │     ├─ test_indexing.cpython-312.pyc
│  │        │  │  │  │     ├─ test_iter.cpython-312.pyc
│  │        │  │  │  │     ├─ test_join.cpython-312.pyc
│  │        │  │  │  │     ├─ test_npfuncs.cpython-312.pyc
│  │        │  │  │  │     ├─ test_ops.cpython-312.pyc
│  │        │  │  │  │     ├─ test_partial_slicing.cpython-312.pyc
│  │        │  │  │  │     ├─ test_pickle.cpython-312.pyc
│  │        │  │  │  │     ├─ test_reindex.cpython-312.pyc
│  │        │  │  │  │     ├─ test_scalar_compat.cpython-312.pyc
│  │        │  │  │  │     ├─ test_setops.cpython-312.pyc
│  │        │  │  │  │     ├─ test_timezones.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ interval
│  │        │  │  │  │  ├─ test_astype.py
│  │        │  │  │  │  ├─ test_constructors.py
│  │        │  │  │  │  ├─ test_equals.py
│  │        │  │  │  │  ├─ test_formats.py
│  │        │  │  │  │  ├─ test_indexing.py
│  │        │  │  │  │  ├─ test_interval.py
│  │        │  │  │  │  ├─ test_interval_range.py
│  │        │  │  │  │  ├─ test_interval_tree.py
│  │        │  │  │  │  ├─ test_join.py
│  │        │  │  │  │  ├─ test_pickle.py
│  │        │  │  │  │  ├─ test_setops.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_astype.cpython-312.pyc
│  │        │  │  │  │     ├─ test_constructors.cpython-312.pyc
│  │        │  │  │  │     ├─ test_equals.cpython-312.pyc
│  │        │  │  │  │     ├─ test_formats.cpython-312.pyc
│  │        │  │  │  │     ├─ test_indexing.cpython-312.pyc
│  │        │  │  │  │     ├─ test_interval.cpython-312.pyc
│  │        │  │  │  │     ├─ test_interval_range.cpython-312.pyc
│  │        │  │  │  │     ├─ test_interval_tree.cpython-312.pyc
│  │        │  │  │  │     ├─ test_join.cpython-312.pyc
│  │        │  │  │  │     ├─ test_pickle.cpython-312.pyc
│  │        │  │  │  │     ├─ test_setops.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ multi
│  │        │  │  │  │  ├─ conftest.py
│  │        │  │  │  │  ├─ test_analytics.py
│  │        │  │  │  │  ├─ test_astype.py
│  │        │  │  │  │  ├─ test_compat.py
│  │        │  │  │  │  ├─ test_constructors.py
│  │        │  │  │  │  ├─ test_conversion.py
│  │        │  │  │  │  ├─ test_copy.py
│  │        │  │  │  │  ├─ test_drop.py
│  │        │  │  │  │  ├─ test_duplicates.py
│  │        │  │  │  │  ├─ test_equivalence.py
│  │        │  │  │  │  ├─ test_formats.py
│  │        │  │  │  │  ├─ test_get_level_values.py
│  │        │  │  │  │  ├─ test_get_set.py
│  │        │  │  │  │  ├─ test_indexing.py
│  │        │  │  │  │  ├─ test_integrity.py
│  │        │  │  │  │  ├─ test_isin.py
│  │        │  │  │  │  ├─ test_join.py
│  │        │  │  │  │  ├─ test_lexsort.py
│  │        │  │  │  │  ├─ test_missing.py
│  │        │  │  │  │  ├─ test_monotonic.py
│  │        │  │  │  │  ├─ test_names.py
│  │        │  │  │  │  ├─ test_partial_indexing.py
│  │        │  │  │  │  ├─ test_pickle.py
│  │        │  │  │  │  ├─ test_reindex.py
│  │        │  │  │  │  ├─ test_reshape.py
│  │        │  │  │  │  ├─ test_setops.py
│  │        │  │  │  │  ├─ test_sorting.py
│  │        │  │  │  │  ├─ test_take.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ conftest.cpython-312.pyc
│  │        │  │  │  │     ├─ test_analytics.cpython-312.pyc
│  │        │  │  │  │     ├─ test_astype.cpython-312.pyc
│  │        │  │  │  │     ├─ test_compat.cpython-312.pyc
│  │        │  │  │  │     ├─ test_constructors.cpython-312.pyc
│  │        │  │  │  │     ├─ test_conversion.cpython-312.pyc
│  │        │  │  │  │     ├─ test_copy.cpython-312.pyc
│  │        │  │  │  │     ├─ test_drop.cpython-312.pyc
│  │        │  │  │  │     ├─ test_duplicates.cpython-312.pyc
│  │        │  │  │  │     ├─ test_equivalence.cpython-312.pyc
│  │        │  │  │  │     ├─ test_formats.cpython-312.pyc
│  │        │  │  │  │     ├─ test_get_level_values.cpython-312.pyc
│  │        │  │  │  │     ├─ test_get_set.cpython-312.pyc
│  │        │  │  │  │     ├─ test_indexing.cpython-312.pyc
│  │        │  │  │  │     ├─ test_integrity.cpython-312.pyc
│  │        │  │  │  │     ├─ test_isin.cpython-312.pyc
│  │        │  │  │  │     ├─ test_join.cpython-312.pyc
│  │        │  │  │  │     ├─ test_lexsort.cpython-312.pyc
│  │        │  │  │  │     ├─ test_missing.cpython-312.pyc
│  │        │  │  │  │     ├─ test_monotonic.cpython-312.pyc
│  │        │  │  │  │     ├─ test_names.cpython-312.pyc
│  │        │  │  │  │     ├─ test_partial_indexing.cpython-312.pyc
│  │        │  │  │  │     ├─ test_pickle.cpython-312.pyc
│  │        │  │  │  │     ├─ test_reindex.cpython-312.pyc
│  │        │  │  │  │     ├─ test_reshape.cpython-312.pyc
│  │        │  │  │  │     ├─ test_setops.cpython-312.pyc
│  │        │  │  │  │     ├─ test_sorting.cpython-312.pyc
│  │        │  │  │  │     ├─ test_take.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ numeric
│  │        │  │  │  │  ├─ test_astype.py
│  │        │  │  │  │  ├─ test_indexing.py
│  │        │  │  │  │  ├─ test_join.py
│  │        │  │  │  │  ├─ test_numeric.py
│  │        │  │  │  │  ├─ test_setops.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_astype.cpython-312.pyc
│  │        │  │  │  │     ├─ test_indexing.cpython-312.pyc
│  │        │  │  │  │     ├─ test_join.cpython-312.pyc
│  │        │  │  │  │     ├─ test_numeric.cpython-312.pyc
│  │        │  │  │  │     ├─ test_setops.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ object
│  │        │  │  │  │  ├─ test_astype.py
│  │        │  │  │  │  ├─ test_indexing.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_astype.cpython-312.pyc
│  │        │  │  │  │     ├─ test_indexing.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ period
│  │        │  │  │  │  ├─ methods
│  │        │  │  │  │  │  ├─ test_asfreq.py
│  │        │  │  │  │  │  ├─ test_astype.py
│  │        │  │  │  │  │  ├─ test_factorize.py
│  │        │  │  │  │  │  ├─ test_fillna.py
│  │        │  │  │  │  │  ├─ test_insert.py
│  │        │  │  │  │  │  ├─ test_is_full.py
│  │        │  │  │  │  │  ├─ test_repeat.py
│  │        │  │  │  │  │  ├─ test_shift.py
│  │        │  │  │  │  │  ├─ test_to_timestamp.py
│  │        │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │     ├─ test_asfreq.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_astype.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_factorize.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_fillna.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_insert.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_is_full.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_repeat.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_shift.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_to_timestamp.cpython-312.pyc
│  │        │  │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  │  ├─ test_constructors.py
│  │        │  │  │  │  ├─ test_formats.py
│  │        │  │  │  │  ├─ test_freq_attr.py
│  │        │  │  │  │  ├─ test_indexing.py
│  │        │  │  │  │  ├─ test_join.py
│  │        │  │  │  │  ├─ test_monotonic.py
│  │        │  │  │  │  ├─ test_partial_slicing.py
│  │        │  │  │  │  ├─ test_period.py
│  │        │  │  │  │  ├─ test_period_range.py
│  │        │  │  │  │  ├─ test_pickle.py
│  │        │  │  │  │  ├─ test_resolution.py
│  │        │  │  │  │  ├─ test_scalar_compat.py
│  │        │  │  │  │  ├─ test_searchsorted.py
│  │        │  │  │  │  ├─ test_setops.py
│  │        │  │  │  │  ├─ test_tools.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_constructors.cpython-312.pyc
│  │        │  │  │  │     ├─ test_formats.cpython-312.pyc
│  │        │  │  │  │     ├─ test_freq_attr.cpython-312.pyc
│  │        │  │  │  │     ├─ test_indexing.cpython-312.pyc
│  │        │  │  │  │     ├─ test_join.cpython-312.pyc
│  │        │  │  │  │     ├─ test_monotonic.cpython-312.pyc
│  │        │  │  │  │     ├─ test_partial_slicing.cpython-312.pyc
│  │        │  │  │  │     ├─ test_period.cpython-312.pyc
│  │        │  │  │  │     ├─ test_period_range.cpython-312.pyc
│  │        │  │  │  │     ├─ test_pickle.cpython-312.pyc
│  │        │  │  │  │     ├─ test_resolution.cpython-312.pyc
│  │        │  │  │  │     ├─ test_scalar_compat.cpython-312.pyc
│  │        │  │  │  │     ├─ test_searchsorted.cpython-312.pyc
│  │        │  │  │  │     ├─ test_setops.cpython-312.pyc
│  │        │  │  │  │     ├─ test_tools.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ ranges
│  │        │  │  │  │  ├─ test_constructors.py
│  │        │  │  │  │  ├─ test_indexing.py
│  │        │  │  │  │  ├─ test_join.py
│  │        │  │  │  │  ├─ test_range.py
│  │        │  │  │  │  ├─ test_setops.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_constructors.cpython-312.pyc
│  │        │  │  │  │     ├─ test_indexing.cpython-312.pyc
│  │        │  │  │  │     ├─ test_join.cpython-312.pyc
│  │        │  │  │  │     ├─ test_range.cpython-312.pyc
│  │        │  │  │  │     ├─ test_setops.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ test_any_index.py
│  │        │  │  │  ├─ test_base.py
│  │        │  │  │  ├─ test_common.py
│  │        │  │  │  ├─ test_datetimelike.py
│  │        │  │  │  ├─ test_engines.py
│  │        │  │  │  ├─ test_frozen.py
│  │        │  │  │  ├─ test_indexing.py
│  │        │  │  │  ├─ test_index_new.py
│  │        │  │  │  ├─ test_numpy_compat.py
│  │        │  │  │  ├─ test_old_base.py
│  │        │  │  │  ├─ test_setops.py
│  │        │  │  │  ├─ test_subclass.py
│  │        │  │  │  ├─ timedeltas
│  │        │  │  │  │  ├─ methods
│  │        │  │  │  │  │  ├─ test_astype.py
│  │        │  │  │  │  │  ├─ test_factorize.py
│  │        │  │  │  │  │  ├─ test_fillna.py
│  │        │  │  │  │  │  ├─ test_insert.py
│  │        │  │  │  │  │  ├─ test_repeat.py
│  │        │  │  │  │  │  ├─ test_shift.py
│  │        │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │     ├─ test_astype.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_factorize.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_fillna.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_insert.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_repeat.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_shift.cpython-312.pyc
│  │        │  │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  │  ├─ test_arithmetic.py
│  │        │  │  │  │  ├─ test_constructors.py
│  │        │  │  │  │  ├─ test_delete.py
│  │        │  │  │  │  ├─ test_formats.py
│  │        │  │  │  │  ├─ test_freq_attr.py
│  │        │  │  │  │  ├─ test_indexing.py
│  │        │  │  │  │  ├─ test_join.py
│  │        │  │  │  │  ├─ test_ops.py
│  │        │  │  │  │  ├─ test_pickle.py
│  │        │  │  │  │  ├─ test_scalar_compat.py
│  │        │  │  │  │  ├─ test_searchsorted.py
│  │        │  │  │  │  ├─ test_setops.py
│  │        │  │  │  │  ├─ test_timedelta.py
│  │        │  │  │  │  ├─ test_timedelta_range.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_arithmetic.cpython-312.pyc
│  │        │  │  │  │     ├─ test_constructors.cpython-312.pyc
│  │        │  │  │  │     ├─ test_delete.cpython-312.pyc
│  │        │  │  │  │     ├─ test_formats.cpython-312.pyc
│  │        │  │  │  │     ├─ test_freq_attr.cpython-312.pyc
│  │        │  │  │  │     ├─ test_indexing.cpython-312.pyc
│  │        │  │  │  │     ├─ test_join.cpython-312.pyc
│  │        │  │  │  │     ├─ test_ops.cpython-312.pyc
│  │        │  │  │  │     ├─ test_pickle.cpython-312.pyc
│  │        │  │  │  │     ├─ test_scalar_compat.cpython-312.pyc
│  │        │  │  │  │     ├─ test_searchsorted.cpython-312.pyc
│  │        │  │  │  │     ├─ test_setops.cpython-312.pyc
│  │        │  │  │  │     ├─ test_timedelta.cpython-312.pyc
│  │        │  │  │  │     ├─ test_timedelta_range.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ conftest.cpython-312.pyc
│  │        │  │  │     ├─ test_any_index.cpython-312.pyc
│  │        │  │  │     ├─ test_base.cpython-312.pyc
│  │        │  │  │     ├─ test_common.cpython-312.pyc
│  │        │  │  │     ├─ test_datetimelike.cpython-312.pyc
│  │        │  │  │     ├─ test_engines.cpython-312.pyc
│  │        │  │  │     ├─ test_frozen.cpython-312.pyc
│  │        │  │  │     ├─ test_indexing.cpython-312.pyc
│  │        │  │  │     ├─ test_index_new.cpython-312.pyc
│  │        │  │  │     ├─ test_numpy_compat.cpython-312.pyc
│  │        │  │  │     ├─ test_old_base.cpython-312.pyc
│  │        │  │  │     ├─ test_setops.cpython-312.pyc
│  │        │  │  │     ├─ test_subclass.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ indexing
│  │        │  │  │  ├─ common.py
│  │        │  │  │  ├─ conftest.py
│  │        │  │  │  ├─ interval
│  │        │  │  │  │  ├─ test_interval.py
│  │        │  │  │  │  ├─ test_interval_new.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_interval.cpython-312.pyc
│  │        │  │  │  │     ├─ test_interval_new.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ multiindex
│  │        │  │  │  │  ├─ test_chaining_and_caching.py
│  │        │  │  │  │  ├─ test_datetime.py
│  │        │  │  │  │  ├─ test_getitem.py
│  │        │  │  │  │  ├─ test_iloc.py
│  │        │  │  │  │  ├─ test_indexing_slow.py
│  │        │  │  │  │  ├─ test_loc.py
│  │        │  │  │  │  ├─ test_multiindex.py
│  │        │  │  │  │  ├─ test_partial.py
│  │        │  │  │  │  ├─ test_setitem.py
│  │        │  │  │  │  ├─ test_slice.py
│  │        │  │  │  │  ├─ test_sorted.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_chaining_and_caching.cpython-312.pyc
│  │        │  │  │  │     ├─ test_datetime.cpython-312.pyc
│  │        │  │  │  │     ├─ test_getitem.cpython-312.pyc
│  │        │  │  │  │     ├─ test_iloc.cpython-312.pyc
│  │        │  │  │  │     ├─ test_indexing_slow.cpython-312.pyc
│  │        │  │  │  │     ├─ test_loc.cpython-312.pyc
│  │        │  │  │  │     ├─ test_multiindex.cpython-312.pyc
│  │        │  │  │  │     ├─ test_partial.cpython-312.pyc
│  │        │  │  │  │     ├─ test_setitem.cpython-312.pyc
│  │        │  │  │  │     ├─ test_slice.cpython-312.pyc
│  │        │  │  │  │     ├─ test_sorted.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ test_at.py
│  │        │  │  │  ├─ test_categorical.py
│  │        │  │  │  ├─ test_chaining_and_caching.py
│  │        │  │  │  ├─ test_check_indexer.py
│  │        │  │  │  ├─ test_coercion.py
│  │        │  │  │  ├─ test_datetime.py
│  │        │  │  │  ├─ test_floats.py
│  │        │  │  │  ├─ test_iat.py
│  │        │  │  │  ├─ test_iloc.py
│  │        │  │  │  ├─ test_indexers.py
│  │        │  │  │  ├─ test_indexing.py
│  │        │  │  │  ├─ test_loc.py
│  │        │  │  │  ├─ test_na_indexing.py
│  │        │  │  │  ├─ test_partial.py
│  │        │  │  │  ├─ test_scalar.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ common.cpython-312.pyc
│  │        │  │  │     ├─ conftest.cpython-312.pyc
│  │        │  │  │     ├─ test_at.cpython-312.pyc
│  │        │  │  │     ├─ test_categorical.cpython-312.pyc
│  │        │  │  │     ├─ test_chaining_and_caching.cpython-312.pyc
│  │        │  │  │     ├─ test_check_indexer.cpython-312.pyc
│  │        │  │  │     ├─ test_coercion.cpython-312.pyc
│  │        │  │  │     ├─ test_datetime.cpython-312.pyc
│  │        │  │  │     ├─ test_floats.cpython-312.pyc
│  │        │  │  │     ├─ test_iat.cpython-312.pyc
│  │        │  │  │     ├─ test_iloc.cpython-312.pyc
│  │        │  │  │     ├─ test_indexers.cpython-312.pyc
│  │        │  │  │     ├─ test_indexing.cpython-312.pyc
│  │        │  │  │     ├─ test_loc.cpython-312.pyc
│  │        │  │  │     ├─ test_na_indexing.cpython-312.pyc
│  │        │  │  │     ├─ test_partial.cpython-312.pyc
│  │        │  │  │     ├─ test_scalar.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ interchange
│  │        │  │  │  ├─ test_impl.py
│  │        │  │  │  ├─ test_spec_conformance.py
│  │        │  │  │  ├─ test_utils.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_impl.cpython-312.pyc
│  │        │  │  │     ├─ test_spec_conformance.cpython-312.pyc
│  │        │  │  │     ├─ test_utils.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ internals
│  │        │  │  │  ├─ test_api.py
│  │        │  │  │  ├─ test_internals.py
│  │        │  │  │  ├─ test_managers.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_api.cpython-312.pyc
│  │        │  │  │     ├─ test_internals.cpython-312.pyc
│  │        │  │  │     ├─ test_managers.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ io
│  │        │  │  │  ├─ conftest.py
│  │        │  │  │  ├─ excel
│  │        │  │  │  │  ├─ test_odf.py
│  │        │  │  │  │  ├─ test_odswriter.py
│  │        │  │  │  │  ├─ test_openpyxl.py
│  │        │  │  │  │  ├─ test_readers.py
│  │        │  │  │  │  ├─ test_style.py
│  │        │  │  │  │  ├─ test_writers.py
│  │        │  │  │  │  ├─ test_xlrd.py
│  │        │  │  │  │  ├─ test_xlsxwriter.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_odf.cpython-312.pyc
│  │        │  │  │  │     ├─ test_odswriter.cpython-312.pyc
│  │        │  │  │  │     ├─ test_openpyxl.cpython-312.pyc
│  │        │  │  │  │     ├─ test_readers.cpython-312.pyc
│  │        │  │  │  │     ├─ test_style.cpython-312.pyc
│  │        │  │  │  │     ├─ test_writers.cpython-312.pyc
│  │        │  │  │  │     ├─ test_xlrd.cpython-312.pyc
│  │        │  │  │  │     ├─ test_xlsxwriter.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ formats
│  │        │  │  │  │  ├─ style
│  │        │  │  │  │  │  ├─ test_bar.py
│  │        │  │  │  │  │  ├─ test_exceptions.py
│  │        │  │  │  │  │  ├─ test_format.py
│  │        │  │  │  │  │  ├─ test_highlight.py
│  │        │  │  │  │  │  ├─ test_html.py
│  │        │  │  │  │  │  ├─ test_matplotlib.py
│  │        │  │  │  │  │  ├─ test_non_unique.py
│  │        │  │  │  │  │  ├─ test_style.py
│  │        │  │  │  │  │  ├─ test_tooltip.py
│  │        │  │  │  │  │  ├─ test_to_latex.py
│  │        │  │  │  │  │  ├─ test_to_string.py
│  │        │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │     ├─ test_bar.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_exceptions.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_format.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_highlight.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_html.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_matplotlib.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_non_unique.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_style.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_tooltip.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_to_latex.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_to_string.cpython-312.pyc
│  │        │  │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  │  ├─ test_console.py
│  │        │  │  │  │  ├─ test_css.py
│  │        │  │  │  │  ├─ test_eng_formatting.py
│  │        │  │  │  │  ├─ test_format.py
│  │        │  │  │  │  ├─ test_ipython_compat.py
│  │        │  │  │  │  ├─ test_printing.py
│  │        │  │  │  │  ├─ test_to_csv.py
│  │        │  │  │  │  ├─ test_to_excel.py
│  │        │  │  │  │  ├─ test_to_html.py
│  │        │  │  │  │  ├─ test_to_latex.py
│  │        │  │  │  │  ├─ test_to_markdown.py
│  │        │  │  │  │  ├─ test_to_string.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_console.cpython-312.pyc
│  │        │  │  │  │     ├─ test_css.cpython-312.pyc
│  │        │  │  │  │     ├─ test_eng_formatting.cpython-312.pyc
│  │        │  │  │  │     ├─ test_format.cpython-312.pyc
│  │        │  │  │  │     ├─ test_ipython_compat.cpython-312.pyc
│  │        │  │  │  │     ├─ test_printing.cpython-312.pyc
│  │        │  │  │  │     ├─ test_to_csv.cpython-312.pyc
│  │        │  │  │  │     ├─ test_to_excel.cpython-312.pyc
│  │        │  │  │  │     ├─ test_to_html.cpython-312.pyc
│  │        │  │  │  │     ├─ test_to_latex.cpython-312.pyc
│  │        │  │  │  │     ├─ test_to_markdown.cpython-312.pyc
│  │        │  │  │  │     ├─ test_to_string.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ generate_legacy_storage_files.py
│  │        │  │  │  ├─ json
│  │        │  │  │  │  ├─ conftest.py
│  │        │  │  │  │  ├─ test_compression.py
│  │        │  │  │  │  ├─ test_deprecated_kwargs.py
│  │        │  │  │  │  ├─ test_json_table_schema.py
│  │        │  │  │  │  ├─ test_json_table_schema_ext_dtype.py
│  │        │  │  │  │  ├─ test_normalize.py
│  │        │  │  │  │  ├─ test_pandas.py
│  │        │  │  │  │  ├─ test_readlines.py
│  │        │  │  │  │  ├─ test_ujson.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ conftest.cpython-312.pyc
│  │        │  │  │  │     ├─ test_compression.cpython-312.pyc
│  │        │  │  │  │     ├─ test_deprecated_kwargs.cpython-312.pyc
│  │        │  │  │  │     ├─ test_json_table_schema.cpython-312.pyc
│  │        │  │  │  │     ├─ test_json_table_schema_ext_dtype.cpython-312.pyc
│  │        │  │  │  │     ├─ test_normalize.cpython-312.pyc
│  │        │  │  │  │     ├─ test_pandas.cpython-312.pyc
│  │        │  │  │  │     ├─ test_readlines.cpython-312.pyc
│  │        │  │  │  │     ├─ test_ujson.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ parser
│  │        │  │  │  │  ├─ common
│  │        │  │  │  │  │  ├─ test_chunksize.py
│  │        │  │  │  │  │  ├─ test_common_basic.py
│  │        │  │  │  │  │  ├─ test_data_list.py
│  │        │  │  │  │  │  ├─ test_decimal.py
│  │        │  │  │  │  │  ├─ test_file_buffer_url.py
│  │        │  │  │  │  │  ├─ test_float.py
│  │        │  │  │  │  │  ├─ test_index.py
│  │        │  │  │  │  │  ├─ test_inf.py
│  │        │  │  │  │  │  ├─ test_ints.py
│  │        │  │  │  │  │  ├─ test_iterator.py
│  │        │  │  │  │  │  ├─ test_read_errors.py
│  │        │  │  │  │  │  ├─ test_verbose.py
│  │        │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │     ├─ test_chunksize.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_common_basic.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_data_list.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_decimal.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_file_buffer_url.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_float.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_index.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_inf.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_ints.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_iterator.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_read_errors.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_verbose.cpython-312.pyc
│  │        │  │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  │  ├─ conftest.py
│  │        │  │  │  │  ├─ dtypes
│  │        │  │  │  │  │  ├─ test_categorical.py
│  │        │  │  │  │  │  ├─ test_dtypes_basic.py
│  │        │  │  │  │  │  ├─ test_empty.py
│  │        │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │     ├─ test_categorical.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_dtypes_basic.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_empty.cpython-312.pyc
│  │        │  │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  │  ├─ test_comment.py
│  │        │  │  │  │  ├─ test_compression.py
│  │        │  │  │  │  ├─ test_concatenate_chunks.py
│  │        │  │  │  │  ├─ test_converters.py
│  │        │  │  │  │  ├─ test_c_parser_only.py
│  │        │  │  │  │  ├─ test_dialect.py
│  │        │  │  │  │  ├─ test_encoding.py
│  │        │  │  │  │  ├─ test_header.py
│  │        │  │  │  │  ├─ test_index_col.py
│  │        │  │  │  │  ├─ test_mangle_dupes.py
│  │        │  │  │  │  ├─ test_multi_thread.py
│  │        │  │  │  │  ├─ test_na_values.py
│  │        │  │  │  │  ├─ test_network.py
│  │        │  │  │  │  ├─ test_parse_dates.py
│  │        │  │  │  │  ├─ test_python_parser_only.py
│  │        │  │  │  │  ├─ test_quoting.py
│  │        │  │  │  │  ├─ test_read_fwf.py
│  │        │  │  │  │  ├─ test_skiprows.py
│  │        │  │  │  │  ├─ test_textreader.py
│  │        │  │  │  │  ├─ test_unsupported.py
│  │        │  │  │  │  ├─ test_upcast.py
│  │        │  │  │  │  ├─ usecols
│  │        │  │  │  │  │  ├─ test_parse_dates.py
│  │        │  │  │  │  │  ├─ test_strings.py
│  │        │  │  │  │  │  ├─ test_usecols_basic.py
│  │        │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │     ├─ test_parse_dates.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_strings.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_usecols_basic.cpython-312.pyc
│  │        │  │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ conftest.cpython-312.pyc
│  │        │  │  │  │     ├─ test_comment.cpython-312.pyc
│  │        │  │  │  │     ├─ test_compression.cpython-312.pyc
│  │        │  │  │  │     ├─ test_concatenate_chunks.cpython-312.pyc
│  │        │  │  │  │     ├─ test_converters.cpython-312.pyc
│  │        │  │  │  │     ├─ test_c_parser_only.cpython-312.pyc
│  │        │  │  │  │     ├─ test_dialect.cpython-312.pyc
│  │        │  │  │  │     ├─ test_encoding.cpython-312.pyc
│  │        │  │  │  │     ├─ test_header.cpython-312.pyc
│  │        │  │  │  │     ├─ test_index_col.cpython-312.pyc
│  │        │  │  │  │     ├─ test_mangle_dupes.cpython-312.pyc
│  │        │  │  │  │     ├─ test_multi_thread.cpython-312.pyc
│  │        │  │  │  │     ├─ test_na_values.cpython-312.pyc
│  │        │  │  │  │     ├─ test_network.cpython-312.pyc
│  │        │  │  │  │     ├─ test_parse_dates.cpython-312.pyc
│  │        │  │  │  │     ├─ test_python_parser_only.cpython-312.pyc
│  │        │  │  │  │     ├─ test_quoting.cpython-312.pyc
│  │        │  │  │  │     ├─ test_read_fwf.cpython-312.pyc
│  │        │  │  │  │     ├─ test_skiprows.cpython-312.pyc
│  │        │  │  │  │     ├─ test_textreader.cpython-312.pyc
│  │        │  │  │  │     ├─ test_unsupported.cpython-312.pyc
│  │        │  │  │  │     ├─ test_upcast.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ pytables
│  │        │  │  │  │  ├─ common.py
│  │        │  │  │  │  ├─ conftest.py
│  │        │  │  │  │  ├─ test_append.py
│  │        │  │  │  │  ├─ test_categorical.py
│  │        │  │  │  │  ├─ test_compat.py
│  │        │  │  │  │  ├─ test_complex.py
│  │        │  │  │  │  ├─ test_errors.py
│  │        │  │  │  │  ├─ test_file_handling.py
│  │        │  │  │  │  ├─ test_keys.py
│  │        │  │  │  │  ├─ test_put.py
│  │        │  │  │  │  ├─ test_pytables_missing.py
│  │        │  │  │  │  ├─ test_read.py
│  │        │  │  │  │  ├─ test_retain_attributes.py
│  │        │  │  │  │  ├─ test_round_trip.py
│  │        │  │  │  │  ├─ test_select.py
│  │        │  │  │  │  ├─ test_store.py
│  │        │  │  │  │  ├─ test_subclass.py
│  │        │  │  │  │  ├─ test_timezones.py
│  │        │  │  │  │  ├─ test_time_series.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ common.cpython-312.pyc
│  │        │  │  │  │     ├─ conftest.cpython-312.pyc
│  │        │  │  │  │     ├─ test_append.cpython-312.pyc
│  │        │  │  │  │     ├─ test_categorical.cpython-312.pyc
│  │        │  │  │  │     ├─ test_compat.cpython-312.pyc
│  │        │  │  │  │     ├─ test_complex.cpython-312.pyc
│  │        │  │  │  │     ├─ test_errors.cpython-312.pyc
│  │        │  │  │  │     ├─ test_file_handling.cpython-312.pyc
│  │        │  │  │  │     ├─ test_keys.cpython-312.pyc
│  │        │  │  │  │     ├─ test_put.cpython-312.pyc
│  │        │  │  │  │     ├─ test_pytables_missing.cpython-312.pyc
│  │        │  │  │  │     ├─ test_read.cpython-312.pyc
│  │        │  │  │  │     ├─ test_retain_attributes.cpython-312.pyc
│  │        │  │  │  │     ├─ test_round_trip.cpython-312.pyc
│  │        │  │  │  │     ├─ test_select.cpython-312.pyc
│  │        │  │  │  │     ├─ test_store.cpython-312.pyc
│  │        │  │  │  │     ├─ test_subclass.cpython-312.pyc
│  │        │  │  │  │     ├─ test_timezones.cpython-312.pyc
│  │        │  │  │  │     ├─ test_time_series.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ sas
│  │        │  │  │  │  ├─ test_byteswap.py
│  │        │  │  │  │  ├─ test_sas.py
│  │        │  │  │  │  ├─ test_sas7bdat.py
│  │        │  │  │  │  ├─ test_xport.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_byteswap.cpython-312.pyc
│  │        │  │  │  │     ├─ test_sas.cpython-312.pyc
│  │        │  │  │  │     ├─ test_sas7bdat.cpython-312.pyc
│  │        │  │  │  │     ├─ test_xport.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ test_clipboard.py
│  │        │  │  │  ├─ test_common.py
│  │        │  │  │  ├─ test_compression.py
│  │        │  │  │  ├─ test_feather.py
│  │        │  │  │  ├─ test_fsspec.py
│  │        │  │  │  ├─ test_gbq.py
│  │        │  │  │  ├─ test_gcs.py
│  │        │  │  │  ├─ test_html.py
│  │        │  │  │  ├─ test_http_headers.py
│  │        │  │  │  ├─ test_orc.py
│  │        │  │  │  ├─ test_parquet.py
│  │        │  │  │  ├─ test_pickle.py
│  │        │  │  │  ├─ test_s3.py
│  │        │  │  │  ├─ test_spss.py
│  │        │  │  │  ├─ test_sql.py
│  │        │  │  │  ├─ test_stata.py
│  │        │  │  │  ├─ xml
│  │        │  │  │  │  ├─ conftest.py
│  │        │  │  │  │  ├─ test_to_xml.py
│  │        │  │  │  │  ├─ test_xml.py
│  │        │  │  │  │  ├─ test_xml_dtypes.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ conftest.cpython-312.pyc
│  │        │  │  │  │     ├─ test_to_xml.cpython-312.pyc
│  │        │  │  │  │     ├─ test_xml.cpython-312.pyc
│  │        │  │  │  │     ├─ test_xml_dtypes.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ conftest.cpython-312.pyc
│  │        │  │  │     ├─ generate_legacy_storage_files.cpython-312.pyc
│  │        │  │  │     ├─ test_clipboard.cpython-312.pyc
│  │        │  │  │     ├─ test_common.cpython-312.pyc
│  │        │  │  │     ├─ test_compression.cpython-312.pyc
│  │        │  │  │     ├─ test_feather.cpython-312.pyc
│  │        │  │  │     ├─ test_fsspec.cpython-312.pyc
│  │        │  │  │     ├─ test_gbq.cpython-312.pyc
│  │        │  │  │     ├─ test_gcs.cpython-312.pyc
│  │        │  │  │     ├─ test_html.cpython-312.pyc
│  │        │  │  │     ├─ test_http_headers.cpython-312.pyc
│  │        │  │  │     ├─ test_orc.cpython-312.pyc
│  │        │  │  │     ├─ test_parquet.cpython-312.pyc
│  │        │  │  │     ├─ test_pickle.cpython-312.pyc
│  │        │  │  │     ├─ test_s3.cpython-312.pyc
│  │        │  │  │     ├─ test_spss.cpython-312.pyc
│  │        │  │  │     ├─ test_sql.cpython-312.pyc
│  │        │  │  │     ├─ test_stata.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ libs
│  │        │  │  │  ├─ test_hashtable.py
│  │        │  │  │  ├─ test_join.py
│  │        │  │  │  ├─ test_lib.py
│  │        │  │  │  ├─ test_libalgos.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_hashtable.cpython-312.pyc
│  │        │  │  │     ├─ test_join.cpython-312.pyc
│  │        │  │  │     ├─ test_lib.cpython-312.pyc
│  │        │  │  │     ├─ test_libalgos.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ plotting
│  │        │  │  │  ├─ common.py
│  │        │  │  │  ├─ conftest.py
│  │        │  │  │  ├─ frame
│  │        │  │  │  │  ├─ test_frame.py
│  │        │  │  │  │  ├─ test_frame_color.py
│  │        │  │  │  │  ├─ test_frame_groupby.py
│  │        │  │  │  │  ├─ test_frame_legend.py
│  │        │  │  │  │  ├─ test_frame_subplots.py
│  │        │  │  │  │  ├─ test_hist_box_by.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_frame.cpython-312.pyc
│  │        │  │  │  │     ├─ test_frame_color.cpython-312.pyc
│  │        │  │  │  │     ├─ test_frame_groupby.cpython-312.pyc
│  │        │  │  │  │     ├─ test_frame_legend.cpython-312.pyc
│  │        │  │  │  │     ├─ test_frame_subplots.cpython-312.pyc
│  │        │  │  │  │     ├─ test_hist_box_by.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ test_backend.py
│  │        │  │  │  ├─ test_boxplot_method.py
│  │        │  │  │  ├─ test_common.py
│  │        │  │  │  ├─ test_converter.py
│  │        │  │  │  ├─ test_datetimelike.py
│  │        │  │  │  ├─ test_groupby.py
│  │        │  │  │  ├─ test_hist_method.py
│  │        │  │  │  ├─ test_misc.py
│  │        │  │  │  ├─ test_series.py
│  │        │  │  │  ├─ test_style.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ common.cpython-312.pyc
│  │        │  │  │     ├─ conftest.cpython-312.pyc
│  │        │  │  │     ├─ test_backend.cpython-312.pyc
│  │        │  │  │     ├─ test_boxplot_method.cpython-312.pyc
│  │        │  │  │     ├─ test_common.cpython-312.pyc
│  │        │  │  │     ├─ test_converter.cpython-312.pyc
│  │        │  │  │     ├─ test_datetimelike.cpython-312.pyc
│  │        │  │  │     ├─ test_groupby.cpython-312.pyc
│  │        │  │  │     ├─ test_hist_method.cpython-312.pyc
│  │        │  │  │     ├─ test_misc.cpython-312.pyc
│  │        │  │  │     ├─ test_series.cpython-312.pyc
│  │        │  │  │     ├─ test_style.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ reductions
│  │        │  │  │  ├─ test_reductions.py
│  │        │  │  │  ├─ test_stat_reductions.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_reductions.cpython-312.pyc
│  │        │  │  │     ├─ test_stat_reductions.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ resample
│  │        │  │  │  ├─ conftest.py
│  │        │  │  │  ├─ test_base.py
│  │        │  │  │  ├─ test_datetime_index.py
│  │        │  │  │  ├─ test_period_index.py
│  │        │  │  │  ├─ test_resampler_grouper.py
│  │        │  │  │  ├─ test_resample_api.py
│  │        │  │  │  ├─ test_timedelta.py
│  │        │  │  │  ├─ test_time_grouper.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ conftest.cpython-312.pyc
│  │        │  │  │     ├─ test_base.cpython-312.pyc
│  │        │  │  │     ├─ test_datetime_index.cpython-312.pyc
│  │        │  │  │     ├─ test_period_index.cpython-312.pyc
│  │        │  │  │     ├─ test_resampler_grouper.cpython-312.pyc
│  │        │  │  │     ├─ test_resample_api.cpython-312.pyc
│  │        │  │  │     ├─ test_timedelta.cpython-312.pyc
│  │        │  │  │     ├─ test_time_grouper.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ reshape
│  │        │  │  │  ├─ concat
│  │        │  │  │  │  ├─ conftest.py
│  │        │  │  │  │  ├─ test_append.py
│  │        │  │  │  │  ├─ test_append_common.py
│  │        │  │  │  │  ├─ test_categorical.py
│  │        │  │  │  │  ├─ test_concat.py
│  │        │  │  │  │  ├─ test_dataframe.py
│  │        │  │  │  │  ├─ test_datetimes.py
│  │        │  │  │  │  ├─ test_empty.py
│  │        │  │  │  │  ├─ test_index.py
│  │        │  │  │  │  ├─ test_invalid.py
│  │        │  │  │  │  ├─ test_series.py
│  │        │  │  │  │  ├─ test_sort.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ conftest.cpython-312.pyc
│  │        │  │  │  │     ├─ test_append.cpython-312.pyc
│  │        │  │  │  │     ├─ test_append_common.cpython-312.pyc
│  │        │  │  │  │     ├─ test_categorical.cpython-312.pyc
│  │        │  │  │  │     ├─ test_concat.cpython-312.pyc
│  │        │  │  │  │     ├─ test_dataframe.cpython-312.pyc
│  │        │  │  │  │     ├─ test_datetimes.cpython-312.pyc
│  │        │  │  │  │     ├─ test_empty.cpython-312.pyc
│  │        │  │  │  │     ├─ test_index.cpython-312.pyc
│  │        │  │  │  │     ├─ test_invalid.cpython-312.pyc
│  │        │  │  │  │     ├─ test_series.cpython-312.pyc
│  │        │  │  │  │     ├─ test_sort.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ merge
│  │        │  │  │  │  ├─ test_join.py
│  │        │  │  │  │  ├─ test_merge.py
│  │        │  │  │  │  ├─ test_merge_asof.py
│  │        │  │  │  │  ├─ test_merge_cross.py
│  │        │  │  │  │  ├─ test_merge_index_as_string.py
│  │        │  │  │  │  ├─ test_merge_ordered.py
│  │        │  │  │  │  ├─ test_multi.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_join.cpython-312.pyc
│  │        │  │  │  │     ├─ test_merge.cpython-312.pyc
│  │        │  │  │  │     ├─ test_merge_asof.cpython-312.pyc
│  │        │  │  │  │     ├─ test_merge_cross.cpython-312.pyc
│  │        │  │  │  │     ├─ test_merge_index_as_string.cpython-312.pyc
│  │        │  │  │  │     ├─ test_merge_ordered.cpython-312.pyc
│  │        │  │  │  │     ├─ test_multi.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ test_crosstab.py
│  │        │  │  │  ├─ test_cut.py
│  │        │  │  │  ├─ test_from_dummies.py
│  │        │  │  │  ├─ test_get_dummies.py
│  │        │  │  │  ├─ test_melt.py
│  │        │  │  │  ├─ test_pivot.py
│  │        │  │  │  ├─ test_pivot_multilevel.py
│  │        │  │  │  ├─ test_qcut.py
│  │        │  │  │  ├─ test_union_categoricals.py
│  │        │  │  │  ├─ test_util.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_crosstab.cpython-312.pyc
│  │        │  │  │     ├─ test_cut.cpython-312.pyc
│  │        │  │  │     ├─ test_from_dummies.cpython-312.pyc
│  │        │  │  │     ├─ test_get_dummies.cpython-312.pyc
│  │        │  │  │     ├─ test_melt.cpython-312.pyc
│  │        │  │  │     ├─ test_pivot.cpython-312.pyc
│  │        │  │  │     ├─ test_pivot_multilevel.cpython-312.pyc
│  │        │  │  │     ├─ test_qcut.cpython-312.pyc
│  │        │  │  │     ├─ test_union_categoricals.cpython-312.pyc
│  │        │  │  │     ├─ test_util.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ scalar
│  │        │  │  │  ├─ interval
│  │        │  │  │  │  ├─ test_arithmetic.py
│  │        │  │  │  │  ├─ test_constructors.py
│  │        │  │  │  │  ├─ test_contains.py
│  │        │  │  │  │  ├─ test_formats.py
│  │        │  │  │  │  ├─ test_interval.py
│  │        │  │  │  │  ├─ test_overlaps.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_arithmetic.cpython-312.pyc
│  │        │  │  │  │     ├─ test_constructors.cpython-312.pyc
│  │        │  │  │  │     ├─ test_contains.cpython-312.pyc
│  │        │  │  │  │     ├─ test_formats.cpython-312.pyc
│  │        │  │  │  │     ├─ test_interval.cpython-312.pyc
│  │        │  │  │  │     ├─ test_overlaps.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ period
│  │        │  │  │  │  ├─ test_arithmetic.py
│  │        │  │  │  │  ├─ test_asfreq.py
│  │        │  │  │  │  ├─ test_period.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_arithmetic.cpython-312.pyc
│  │        │  │  │  │     ├─ test_asfreq.cpython-312.pyc
│  │        │  │  │  │     ├─ test_period.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ test_nat.py
│  │        │  │  │  ├─ test_na_scalar.py
│  │        │  │  │  ├─ timedelta
│  │        │  │  │  │  ├─ methods
│  │        │  │  │  │  │  ├─ test_as_unit.py
│  │        │  │  │  │  │  ├─ test_round.py
│  │        │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │     ├─ test_as_unit.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_round.cpython-312.pyc
│  │        │  │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  │  ├─ test_arithmetic.py
│  │        │  │  │  │  ├─ test_constructors.py
│  │        │  │  │  │  ├─ test_formats.py
│  │        │  │  │  │  ├─ test_timedelta.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_arithmetic.cpython-312.pyc
│  │        │  │  │  │     ├─ test_constructors.cpython-312.pyc
│  │        │  │  │  │     ├─ test_formats.cpython-312.pyc
│  │        │  │  │  │     ├─ test_timedelta.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ timestamp
│  │        │  │  │  │  ├─ methods
│  │        │  │  │  │  │  ├─ test_as_unit.py
│  │        │  │  │  │  │  ├─ test_normalize.py
│  │        │  │  │  │  │  ├─ test_replace.py
│  │        │  │  │  │  │  ├─ test_round.py
│  │        │  │  │  │  │  ├─ test_timestamp_method.py
│  │        │  │  │  │  │  ├─ test_to_julian_date.py
│  │        │  │  │  │  │  ├─ test_to_pydatetime.py
│  │        │  │  │  │  │  ├─ test_tz_convert.py
│  │        │  │  │  │  │  ├─ test_tz_localize.py
│  │        │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │     ├─ test_as_unit.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_normalize.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_replace.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_round.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_timestamp_method.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_to_julian_date.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_to_pydatetime.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_tz_convert.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_tz_localize.cpython-312.pyc
│  │        │  │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  │  ├─ test_arithmetic.py
│  │        │  │  │  │  ├─ test_comparisons.py
│  │        │  │  │  │  ├─ test_constructors.py
│  │        │  │  │  │  ├─ test_formats.py
│  │        │  │  │  │  ├─ test_timestamp.py
│  │        │  │  │  │  ├─ test_timezones.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_arithmetic.cpython-312.pyc
│  │        │  │  │  │     ├─ test_comparisons.cpython-312.pyc
│  │        │  │  │  │     ├─ test_constructors.cpython-312.pyc
│  │        │  │  │  │     ├─ test_formats.cpython-312.pyc
│  │        │  │  │  │     ├─ test_timestamp.cpython-312.pyc
│  │        │  │  │  │     ├─ test_timezones.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_nat.cpython-312.pyc
│  │        │  │  │     ├─ test_na_scalar.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ series
│  │        │  │  │  ├─ accessors
│  │        │  │  │  │  ├─ test_cat_accessor.py
│  │        │  │  │  │  ├─ test_dt_accessor.py
│  │        │  │  │  │  ├─ test_list_accessor.py
│  │        │  │  │  │  ├─ test_sparse_accessor.py
│  │        │  │  │  │  ├─ test_struct_accessor.py
│  │        │  │  │  │  ├─ test_str_accessor.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_cat_accessor.cpython-312.pyc
│  │        │  │  │  │     ├─ test_dt_accessor.cpython-312.pyc
│  │        │  │  │  │     ├─ test_list_accessor.cpython-312.pyc
│  │        │  │  │  │     ├─ test_sparse_accessor.cpython-312.pyc
│  │        │  │  │  │     ├─ test_struct_accessor.cpython-312.pyc
│  │        │  │  │  │     ├─ test_str_accessor.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ indexing
│  │        │  │  │  │  ├─ test_datetime.py
│  │        │  │  │  │  ├─ test_delitem.py
│  │        │  │  │  │  ├─ test_get.py
│  │        │  │  │  │  ├─ test_getitem.py
│  │        │  │  │  │  ├─ test_indexing.py
│  │        │  │  │  │  ├─ test_mask.py
│  │        │  │  │  │  ├─ test_setitem.py
│  │        │  │  │  │  ├─ test_set_value.py
│  │        │  │  │  │  ├─ test_take.py
│  │        │  │  │  │  ├─ test_where.py
│  │        │  │  │  │  ├─ test_xs.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_datetime.cpython-312.pyc
│  │        │  │  │  │     ├─ test_delitem.cpython-312.pyc
│  │        │  │  │  │     ├─ test_get.cpython-312.pyc
│  │        │  │  │  │     ├─ test_getitem.cpython-312.pyc
│  │        │  │  │  │     ├─ test_indexing.cpython-312.pyc
│  │        │  │  │  │     ├─ test_mask.cpython-312.pyc
│  │        │  │  │  │     ├─ test_setitem.cpython-312.pyc
│  │        │  │  │  │     ├─ test_set_value.cpython-312.pyc
│  │        │  │  │  │     ├─ test_take.cpython-312.pyc
│  │        │  │  │  │     ├─ test_where.cpython-312.pyc
│  │        │  │  │  │     ├─ test_xs.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ methods
│  │        │  │  │  │  ├─ test_add_prefix_suffix.py
│  │        │  │  │  │  ├─ test_align.py
│  │        │  │  │  │  ├─ test_argsort.py
│  │        │  │  │  │  ├─ test_asof.py
│  │        │  │  │  │  ├─ test_astype.py
│  │        │  │  │  │  ├─ test_autocorr.py
│  │        │  │  │  │  ├─ test_between.py
│  │        │  │  │  │  ├─ test_case_when.py
│  │        │  │  │  │  ├─ test_clip.py
│  │        │  │  │  │  ├─ test_combine.py
│  │        │  │  │  │  ├─ test_combine_first.py
│  │        │  │  │  │  ├─ test_compare.py
│  │        │  │  │  │  ├─ test_convert_dtypes.py
│  │        │  │  │  │  ├─ test_copy.py
│  │        │  │  │  │  ├─ test_count.py
│  │        │  │  │  │  ├─ test_cov_corr.py
│  │        │  │  │  │  ├─ test_describe.py
│  │        │  │  │  │  ├─ test_diff.py
│  │        │  │  │  │  ├─ test_drop.py
│  │        │  │  │  │  ├─ test_dropna.py
│  │        │  │  │  │  ├─ test_drop_duplicates.py
│  │        │  │  │  │  ├─ test_dtypes.py
│  │        │  │  │  │  ├─ test_duplicated.py
│  │        │  │  │  │  ├─ test_equals.py
│  │        │  │  │  │  ├─ test_explode.py
│  │        │  │  │  │  ├─ test_fillna.py
│  │        │  │  │  │  ├─ test_get_numeric_data.py
│  │        │  │  │  │  ├─ test_head_tail.py
│  │        │  │  │  │  ├─ test_infer_objects.py
│  │        │  │  │  │  ├─ test_info.py
│  │        │  │  │  │  ├─ test_interpolate.py
│  │        │  │  │  │  ├─ test_isin.py
│  │        │  │  │  │  ├─ test_isna.py
│  │        │  │  │  │  ├─ test_is_monotonic.py
│  │        │  │  │  │  ├─ test_is_unique.py
│  │        │  │  │  │  ├─ test_item.py
│  │        │  │  │  │  ├─ test_map.py
│  │        │  │  │  │  ├─ test_matmul.py
│  │        │  │  │  │  ├─ test_nlargest.py
│  │        │  │  │  │  ├─ test_nunique.py
│  │        │  │  │  │  ├─ test_pct_change.py
│  │        │  │  │  │  ├─ test_pop.py
│  │        │  │  │  │  ├─ test_quantile.py
│  │        │  │  │  │  ├─ test_rank.py
│  │        │  │  │  │  ├─ test_reindex.py
│  │        │  │  │  │  ├─ test_reindex_like.py
│  │        │  │  │  │  ├─ test_rename.py
│  │        │  │  │  │  ├─ test_rename_axis.py
│  │        │  │  │  │  ├─ test_repeat.py
│  │        │  │  │  │  ├─ test_replace.py
│  │        │  │  │  │  ├─ test_reset_index.py
│  │        │  │  │  │  ├─ test_round.py
│  │        │  │  │  │  ├─ test_searchsorted.py
│  │        │  │  │  │  ├─ test_set_name.py
│  │        │  │  │  │  ├─ test_size.py
│  │        │  │  │  │  ├─ test_sort_index.py
│  │        │  │  │  │  ├─ test_sort_values.py
│  │        │  │  │  │  ├─ test_tolist.py
│  │        │  │  │  │  ├─ test_to_csv.py
│  │        │  │  │  │  ├─ test_to_dict.py
│  │        │  │  │  │  ├─ test_to_frame.py
│  │        │  │  │  │  ├─ test_to_numpy.py
│  │        │  │  │  │  ├─ test_truncate.py
│  │        │  │  │  │  ├─ test_tz_localize.py
│  │        │  │  │  │  ├─ test_unique.py
│  │        │  │  │  │  ├─ test_unstack.py
│  │        │  │  │  │  ├─ test_update.py
│  │        │  │  │  │  ├─ test_values.py
│  │        │  │  │  │  ├─ test_value_counts.py
│  │        │  │  │  │  ├─ test_view.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_add_prefix_suffix.cpython-312.pyc
│  │        │  │  │  │     ├─ test_align.cpython-312.pyc
│  │        │  │  │  │     ├─ test_argsort.cpython-312.pyc
│  │        │  │  │  │     ├─ test_asof.cpython-312.pyc
│  │        │  │  │  │     ├─ test_astype.cpython-312.pyc
│  │        │  │  │  │     ├─ test_autocorr.cpython-312.pyc
│  │        │  │  │  │     ├─ test_between.cpython-312.pyc
│  │        │  │  │  │     ├─ test_case_when.cpython-312.pyc
│  │        │  │  │  │     ├─ test_clip.cpython-312.pyc
│  │        │  │  │  │     ├─ test_combine.cpython-312.pyc
│  │        │  │  │  │     ├─ test_combine_first.cpython-312.pyc
│  │        │  │  │  │     ├─ test_compare.cpython-312.pyc
│  │        │  │  │  │     ├─ test_convert_dtypes.cpython-312.pyc
│  │        │  │  │  │     ├─ test_copy.cpython-312.pyc
│  │        │  │  │  │     ├─ test_count.cpython-312.pyc
│  │        │  │  │  │     ├─ test_cov_corr.cpython-312.pyc
│  │        │  │  │  │     ├─ test_describe.cpython-312.pyc
│  │        │  │  │  │     ├─ test_diff.cpython-312.pyc
│  │        │  │  │  │     ├─ test_drop.cpython-312.pyc
│  │        │  │  │  │     ├─ test_dropna.cpython-312.pyc
│  │        │  │  │  │     ├─ test_drop_duplicates.cpython-312.pyc
│  │        │  │  │  │     ├─ test_dtypes.cpython-312.pyc
│  │        │  │  │  │     ├─ test_duplicated.cpython-312.pyc
│  │        │  │  │  │     ├─ test_equals.cpython-312.pyc
│  │        │  │  │  │     ├─ test_explode.cpython-312.pyc
│  │        │  │  │  │     ├─ test_fillna.cpython-312.pyc
│  │        │  │  │  │     ├─ test_get_numeric_data.cpython-312.pyc
│  │        │  │  │  │     ├─ test_head_tail.cpython-312.pyc
│  │        │  │  │  │     ├─ test_infer_objects.cpython-312.pyc
│  │        │  │  │  │     ├─ test_info.cpython-312.pyc
│  │        │  │  │  │     ├─ test_interpolate.cpython-312.pyc
│  │        │  │  │  │     ├─ test_isin.cpython-312.pyc
│  │        │  │  │  │     ├─ test_isna.cpython-312.pyc
│  │        │  │  │  │     ├─ test_is_monotonic.cpython-312.pyc
│  │        │  │  │  │     ├─ test_is_unique.cpython-312.pyc
│  │        │  │  │  │     ├─ test_item.cpython-312.pyc
│  │        │  │  │  │     ├─ test_map.cpython-312.pyc
│  │        │  │  │  │     ├─ test_matmul.cpython-312.pyc
│  │        │  │  │  │     ├─ test_nlargest.cpython-312.pyc
│  │        │  │  │  │     ├─ test_nunique.cpython-312.pyc
│  │        │  │  │  │     ├─ test_pct_change.cpython-312.pyc
│  │        │  │  │  │     ├─ test_pop.cpython-312.pyc
│  │        │  │  │  │     ├─ test_quantile.cpython-312.pyc
│  │        │  │  │  │     ├─ test_rank.cpython-312.pyc
│  │        │  │  │  │     ├─ test_reindex.cpython-312.pyc
│  │        │  │  │  │     ├─ test_reindex_like.cpython-312.pyc
│  │        │  │  │  │     ├─ test_rename.cpython-312.pyc
│  │        │  │  │  │     ├─ test_rename_axis.cpython-312.pyc
│  │        │  │  │  │     ├─ test_repeat.cpython-312.pyc
│  │        │  │  │  │     ├─ test_replace.cpython-312.pyc
│  │        │  │  │  │     ├─ test_reset_index.cpython-312.pyc
│  │        │  │  │  │     ├─ test_round.cpython-312.pyc
│  │        │  │  │  │     ├─ test_searchsorted.cpython-312.pyc
│  │        │  │  │  │     ├─ test_set_name.cpython-312.pyc
│  │        │  │  │  │     ├─ test_size.cpython-312.pyc
│  │        │  │  │  │     ├─ test_sort_index.cpython-312.pyc
│  │        │  │  │  │     ├─ test_sort_values.cpython-312.pyc
│  │        │  │  │  │     ├─ test_tolist.cpython-312.pyc
│  │        │  │  │  │     ├─ test_to_csv.cpython-312.pyc
│  │        │  │  │  │     ├─ test_to_dict.cpython-312.pyc
│  │        │  │  │  │     ├─ test_to_frame.cpython-312.pyc
│  │        │  │  │  │     ├─ test_to_numpy.cpython-312.pyc
│  │        │  │  │  │     ├─ test_truncate.cpython-312.pyc
│  │        │  │  │  │     ├─ test_tz_localize.cpython-312.pyc
│  │        │  │  │  │     ├─ test_unique.cpython-312.pyc
│  │        │  │  │  │     ├─ test_unstack.cpython-312.pyc
│  │        │  │  │  │     ├─ test_update.cpython-312.pyc
│  │        │  │  │  │     ├─ test_values.cpython-312.pyc
│  │        │  │  │  │     ├─ test_value_counts.cpython-312.pyc
│  │        │  │  │  │     ├─ test_view.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ test_api.py
│  │        │  │  │  ├─ test_arithmetic.py
│  │        │  │  │  ├─ test_constructors.py
│  │        │  │  │  ├─ test_cumulative.py
│  │        │  │  │  ├─ test_formats.py
│  │        │  │  │  ├─ test_iteration.py
│  │        │  │  │  ├─ test_logical_ops.py
│  │        │  │  │  ├─ test_missing.py
│  │        │  │  │  ├─ test_npfuncs.py
│  │        │  │  │  ├─ test_reductions.py
│  │        │  │  │  ├─ test_subclass.py
│  │        │  │  │  ├─ test_ufunc.py
│  │        │  │  │  ├─ test_unary.py
│  │        │  │  │  ├─ test_validate.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_api.cpython-312.pyc
│  │        │  │  │     ├─ test_arithmetic.cpython-312.pyc
│  │        │  │  │     ├─ test_constructors.cpython-312.pyc
│  │        │  │  │     ├─ test_cumulative.cpython-312.pyc
│  │        │  │  │     ├─ test_formats.cpython-312.pyc
│  │        │  │  │     ├─ test_iteration.cpython-312.pyc
│  │        │  │  │     ├─ test_logical_ops.cpython-312.pyc
│  │        │  │  │     ├─ test_missing.cpython-312.pyc
│  │        │  │  │     ├─ test_npfuncs.cpython-312.pyc
│  │        │  │  │     ├─ test_reductions.cpython-312.pyc
│  │        │  │  │     ├─ test_subclass.cpython-312.pyc
│  │        │  │  │     ├─ test_ufunc.cpython-312.pyc
│  │        │  │  │     ├─ test_unary.cpython-312.pyc
│  │        │  │  │     ├─ test_validate.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ strings
│  │        │  │  │  ├─ conftest.py
│  │        │  │  │  ├─ test_api.py
│  │        │  │  │  ├─ test_case_justify.py
│  │        │  │  │  ├─ test_cat.py
│  │        │  │  │  ├─ test_extract.py
│  │        │  │  │  ├─ test_find_replace.py
│  │        │  │  │  ├─ test_get_dummies.py
│  │        │  │  │  ├─ test_split_partition.py
│  │        │  │  │  ├─ test_strings.py
│  │        │  │  │  ├─ test_string_array.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ conftest.cpython-312.pyc
│  │        │  │  │     ├─ test_api.cpython-312.pyc
│  │        │  │  │     ├─ test_case_justify.cpython-312.pyc
│  │        │  │  │     ├─ test_cat.cpython-312.pyc
│  │        │  │  │     ├─ test_extract.cpython-312.pyc
│  │        │  │  │     ├─ test_find_replace.cpython-312.pyc
│  │        │  │  │     ├─ test_get_dummies.cpython-312.pyc
│  │        │  │  │     ├─ test_split_partition.cpython-312.pyc
│  │        │  │  │     ├─ test_strings.cpython-312.pyc
│  │        │  │  │     ├─ test_string_array.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ test_aggregation.py
│  │        │  │  ├─ test_algos.py
│  │        │  │  ├─ test_common.py
│  │        │  │  ├─ test_downstream.py
│  │        │  │  ├─ test_errors.py
│  │        │  │  ├─ test_expressions.py
│  │        │  │  ├─ test_flags.py
│  │        │  │  ├─ test_multilevel.py
│  │        │  │  ├─ test_nanops.py
│  │        │  │  ├─ test_optional_dependency.py
│  │        │  │  ├─ test_register_accessor.py
│  │        │  │  ├─ test_sorting.py
│  │        │  │  ├─ test_take.py
│  │        │  │  ├─ tools
│  │        │  │  │  ├─ test_to_datetime.py
│  │        │  │  │  ├─ test_to_numeric.py
│  │        │  │  │  ├─ test_to_time.py
│  │        │  │  │  ├─ test_to_timedelta.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_to_datetime.cpython-312.pyc
│  │        │  │  │     ├─ test_to_numeric.cpython-312.pyc
│  │        │  │  │     ├─ test_to_time.cpython-312.pyc
│  │        │  │  │     ├─ test_to_timedelta.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ tseries
│  │        │  │  │  ├─ frequencies
│  │        │  │  │  │  ├─ test_frequencies.py
│  │        │  │  │  │  ├─ test_freq_code.py
│  │        │  │  │  │  ├─ test_inference.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_frequencies.cpython-312.pyc
│  │        │  │  │  │     ├─ test_freq_code.cpython-312.pyc
│  │        │  │  │  │     ├─ test_inference.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ holiday
│  │        │  │  │  │  ├─ test_calendar.py
│  │        │  │  │  │  ├─ test_federal.py
│  │        │  │  │  │  ├─ test_holiday.py
│  │        │  │  │  │  ├─ test_observance.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_calendar.cpython-312.pyc
│  │        │  │  │  │     ├─ test_federal.cpython-312.pyc
│  │        │  │  │  │     ├─ test_holiday.cpython-312.pyc
│  │        │  │  │  │     ├─ test_observance.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ offsets
│  │        │  │  │  │  ├─ common.py
│  │        │  │  │  │  ├─ test_business_day.py
│  │        │  │  │  │  ├─ test_business_hour.py
│  │        │  │  │  │  ├─ test_business_month.py
│  │        │  │  │  │  ├─ test_business_quarter.py
│  │        │  │  │  │  ├─ test_business_year.py
│  │        │  │  │  │  ├─ test_common.py
│  │        │  │  │  │  ├─ test_custom_business_day.py
│  │        │  │  │  │  ├─ test_custom_business_hour.py
│  │        │  │  │  │  ├─ test_custom_business_month.py
│  │        │  │  │  │  ├─ test_dst.py
│  │        │  │  │  │  ├─ test_easter.py
│  │        │  │  │  │  ├─ test_fiscal.py
│  │        │  │  │  │  ├─ test_index.py
│  │        │  │  │  │  ├─ test_month.py
│  │        │  │  │  │  ├─ test_offsets.py
│  │        │  │  │  │  ├─ test_offsets_properties.py
│  │        │  │  │  │  ├─ test_quarter.py
│  │        │  │  │  │  ├─ test_ticks.py
│  │        │  │  │  │  ├─ test_week.py
│  │        │  │  │  │  ├─ test_year.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ common.cpython-312.pyc
│  │        │  │  │  │     ├─ test_business_day.cpython-312.pyc
│  │        │  │  │  │     ├─ test_business_hour.cpython-312.pyc
│  │        │  │  │  │     ├─ test_business_month.cpython-312.pyc
│  │        │  │  │  │     ├─ test_business_quarter.cpython-312.pyc
│  │        │  │  │  │     ├─ test_business_year.cpython-312.pyc
│  │        │  │  │  │     ├─ test_common.cpython-312.pyc
│  │        │  │  │  │     ├─ test_custom_business_day.cpython-312.pyc
│  │        │  │  │  │     ├─ test_custom_business_hour.cpython-312.pyc
│  │        │  │  │  │     ├─ test_custom_business_month.cpython-312.pyc
│  │        │  │  │  │     ├─ test_dst.cpython-312.pyc
│  │        │  │  │  │     ├─ test_easter.cpython-312.pyc
│  │        │  │  │  │     ├─ test_fiscal.cpython-312.pyc
│  │        │  │  │  │     ├─ test_index.cpython-312.pyc
│  │        │  │  │  │     ├─ test_month.cpython-312.pyc
│  │        │  │  │  │     ├─ test_offsets.cpython-312.pyc
│  │        │  │  │  │     ├─ test_offsets_properties.cpython-312.pyc
│  │        │  │  │  │     ├─ test_quarter.cpython-312.pyc
│  │        │  │  │  │     ├─ test_ticks.cpython-312.pyc
│  │        │  │  │  │     ├─ test_week.cpython-312.pyc
│  │        │  │  │  │     ├─ test_year.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ tslibs
│  │        │  │  │  ├─ test_api.py
│  │        │  │  │  ├─ test_array_to_datetime.py
│  │        │  │  │  ├─ test_ccalendar.py
│  │        │  │  │  ├─ test_conversion.py
│  │        │  │  │  ├─ test_fields.py
│  │        │  │  │  ├─ test_libfrequencies.py
│  │        │  │  │  ├─ test_liboffsets.py
│  │        │  │  │  ├─ test_npy_units.py
│  │        │  │  │  ├─ test_np_datetime.py
│  │        │  │  │  ├─ test_parse_iso8601.py
│  │        │  │  │  ├─ test_parsing.py
│  │        │  │  │  ├─ test_period.py
│  │        │  │  │  ├─ test_resolution.py
│  │        │  │  │  ├─ test_strptime.py
│  │        │  │  │  ├─ test_timedeltas.py
│  │        │  │  │  ├─ test_timezones.py
│  │        │  │  │  ├─ test_to_offset.py
│  │        │  │  │  ├─ test_tzconversion.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_api.cpython-312.pyc
│  │        │  │  │     ├─ test_array_to_datetime.cpython-312.pyc
│  │        │  │  │     ├─ test_ccalendar.cpython-312.pyc
│  │        │  │  │     ├─ test_conversion.cpython-312.pyc
│  │        │  │  │     ├─ test_fields.cpython-312.pyc
│  │        │  │  │     ├─ test_libfrequencies.cpython-312.pyc
│  │        │  │  │     ├─ test_liboffsets.cpython-312.pyc
│  │        │  │  │     ├─ test_npy_units.cpython-312.pyc
│  │        │  │  │     ├─ test_np_datetime.cpython-312.pyc
│  │        │  │  │     ├─ test_parse_iso8601.cpython-312.pyc
│  │        │  │  │     ├─ test_parsing.cpython-312.pyc
│  │        │  │  │     ├─ test_period.cpython-312.pyc
│  │        │  │  │     ├─ test_resolution.cpython-312.pyc
│  │        │  │  │     ├─ test_strptime.cpython-312.pyc
│  │        │  │  │     ├─ test_timedeltas.cpython-312.pyc
│  │        │  │  │     ├─ test_timezones.cpython-312.pyc
│  │        │  │  │     ├─ test_to_offset.cpython-312.pyc
│  │        │  │  │     ├─ test_tzconversion.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ util
│  │        │  │  │  ├─ conftest.py
│  │        │  │  │  ├─ test_assert_almost_equal.py
│  │        │  │  │  ├─ test_assert_attr_equal.py
│  │        │  │  │  ├─ test_assert_categorical_equal.py
│  │        │  │  │  ├─ test_assert_extension_array_equal.py
│  │        │  │  │  ├─ test_assert_frame_equal.py
│  │        │  │  │  ├─ test_assert_index_equal.py
│  │        │  │  │  ├─ test_assert_interval_array_equal.py
│  │        │  │  │  ├─ test_assert_numpy_array_equal.py
│  │        │  │  │  ├─ test_assert_produces_warning.py
│  │        │  │  │  ├─ test_assert_series_equal.py
│  │        │  │  │  ├─ test_deprecate.py
│  │        │  │  │  ├─ test_deprecate_kwarg.py
│  │        │  │  │  ├─ test_deprecate_nonkeyword_arguments.py
│  │        │  │  │  ├─ test_doc.py
│  │        │  │  │  ├─ test_hashing.py
│  │        │  │  │  ├─ test_numba.py
│  │        │  │  │  ├─ test_rewrite_warning.py
│  │        │  │  │  ├─ test_shares_memory.py
│  │        │  │  │  ├─ test_show_versions.py
│  │        │  │  │  ├─ test_util.py
│  │        │  │  │  ├─ test_validate_args.py
│  │        │  │  │  ├─ test_validate_args_and_kwargs.py
│  │        │  │  │  ├─ test_validate_inclusive.py
│  │        │  │  │  ├─ test_validate_kwargs.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ conftest.cpython-312.pyc
│  │        │  │  │     ├─ test_assert_almost_equal.cpython-312.pyc
│  │        │  │  │     ├─ test_assert_attr_equal.cpython-312.pyc
│  │        │  │  │     ├─ test_assert_categorical_equal.cpython-312.pyc
│  │        │  │  │     ├─ test_assert_extension_array_equal.cpython-312.pyc
│  │        │  │  │     ├─ test_assert_frame_equal.cpython-312.pyc
│  │        │  │  │     ├─ test_assert_index_equal.cpython-312.pyc
│  │        │  │  │     ├─ test_assert_interval_array_equal.cpython-312.pyc
│  │        │  │  │     ├─ test_assert_numpy_array_equal.cpython-312.pyc
│  │        │  │  │     ├─ test_assert_produces_warning.cpython-312.pyc
│  │        │  │  │     ├─ test_assert_series_equal.cpython-312.pyc
│  │        │  │  │     ├─ test_deprecate.cpython-312.pyc
│  │        │  │  │     ├─ test_deprecate_kwarg.cpython-312.pyc
│  │        │  │  │     ├─ test_deprecate_nonkeyword_arguments.cpython-312.pyc
│  │        │  │  │     ├─ test_doc.cpython-312.pyc
│  │        │  │  │     ├─ test_hashing.cpython-312.pyc
│  │        │  │  │     ├─ test_numba.cpython-312.pyc
│  │        │  │  │     ├─ test_rewrite_warning.cpython-312.pyc
│  │        │  │  │     ├─ test_shares_memory.cpython-312.pyc
│  │        │  │  │     ├─ test_show_versions.cpython-312.pyc
│  │        │  │  │     ├─ test_util.cpython-312.pyc
│  │        │  │  │     ├─ test_validate_args.cpython-312.pyc
│  │        │  │  │     ├─ test_validate_args_and_kwargs.cpython-312.pyc
│  │        │  │  │     ├─ test_validate_inclusive.cpython-312.pyc
│  │        │  │  │     ├─ test_validate_kwargs.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ window
│  │        │  │  │  ├─ conftest.py
│  │        │  │  │  ├─ moments
│  │        │  │  │  │  ├─ conftest.py
│  │        │  │  │  │  ├─ test_moments_consistency_ewm.py
│  │        │  │  │  │  ├─ test_moments_consistency_expanding.py
│  │        │  │  │  │  ├─ test_moments_consistency_rolling.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ conftest.cpython-312.pyc
│  │        │  │  │  │     ├─ test_moments_consistency_ewm.cpython-312.pyc
│  │        │  │  │  │     ├─ test_moments_consistency_expanding.cpython-312.pyc
│  │        │  │  │  │     ├─ test_moments_consistency_rolling.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ test_api.py
│  │        │  │  │  ├─ test_apply.py
│  │        │  │  │  ├─ test_base_indexer.py
│  │        │  │  │  ├─ test_cython_aggregations.py
│  │        │  │  │  ├─ test_dtypes.py
│  │        │  │  │  ├─ test_ewm.py
│  │        │  │  │  ├─ test_expanding.py
│  │        │  │  │  ├─ test_groupby.py
│  │        │  │  │  ├─ test_numba.py
│  │        │  │  │  ├─ test_online.py
│  │        │  │  │  ├─ test_pairwise.py
│  │        │  │  │  ├─ test_rolling.py
│  │        │  │  │  ├─ test_rolling_functions.py
│  │        │  │  │  ├─ test_rolling_quantile.py
│  │        │  │  │  ├─ test_rolling_skew_kurt.py
│  │        │  │  │  ├─ test_timeseries_window.py
│  │        │  │  │  ├─ test_win_type.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ conftest.cpython-312.pyc
│  │        │  │  │     ├─ test_api.cpython-312.pyc
│  │        │  │  │     ├─ test_apply.cpython-312.pyc
│  │        │  │  │     ├─ test_base_indexer.cpython-312.pyc
│  │        │  │  │     ├─ test_cython_aggregations.cpython-312.pyc
│  │        │  │  │     ├─ test_dtypes.cpython-312.pyc
│  │        │  │  │     ├─ test_ewm.cpython-312.pyc
│  │        │  │  │     ├─ test_expanding.cpython-312.pyc
│  │        │  │  │     ├─ test_groupby.cpython-312.pyc
│  │        │  │  │     ├─ test_numba.cpython-312.pyc
│  │        │  │  │     ├─ test_online.cpython-312.pyc
│  │        │  │  │     ├─ test_pairwise.cpython-312.pyc
│  │        │  │  │     ├─ test_rolling.cpython-312.pyc
│  │        │  │  │     ├─ test_rolling_functions.cpython-312.pyc
│  │        │  │  │     ├─ test_rolling_quantile.cpython-312.pyc
│  │        │  │  │     ├─ test_rolling_skew_kurt.cpython-312.pyc
│  │        │  │  │     ├─ test_timeseries_window.cpython-312.pyc
│  │        │  │  │     ├─ test_win_type.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ test_aggregation.cpython-312.pyc
│  │        │  │     ├─ test_algos.cpython-312.pyc
│  │        │  │     ├─ test_common.cpython-312.pyc
│  │        │  │     ├─ test_downstream.cpython-312.pyc
│  │        │  │     ├─ test_errors.cpython-312.pyc
│  │        │  │     ├─ test_expressions.cpython-312.pyc
│  │        │  │     ├─ test_flags.cpython-312.pyc
│  │        │  │     ├─ test_multilevel.cpython-312.pyc
│  │        │  │     ├─ test_nanops.cpython-312.pyc
│  │        │  │     ├─ test_optional_dependency.cpython-312.pyc
│  │        │  │     ├─ test_register_accessor.cpython-312.pyc
│  │        │  │     ├─ test_sorting.cpython-312.pyc
│  │        │  │     ├─ test_take.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ tseries
│  │        │  │  ├─ api.py
│  │        │  │  ├─ frequencies.py
│  │        │  │  ├─ holiday.py
│  │        │  │  ├─ offsets.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ api.cpython-312.pyc
│  │        │  │     ├─ frequencies.cpython-312.pyc
│  │        │  │     ├─ holiday.cpython-312.pyc
│  │        │  │     ├─ offsets.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ util
│  │        │  │  ├─ version
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _decorators.py
│  │        │  │  ├─ _doctools.py
│  │        │  │  ├─ _exceptions.py
│  │        │  │  ├─ _print_versions.py
│  │        │  │  ├─ _tester.py
│  │        │  │  ├─ _test_decorators.py
│  │        │  │  ├─ _validators.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ _decorators.cpython-312.pyc
│  │        │  │     ├─ _doctools.cpython-312.pyc
│  │        │  │     ├─ _exceptions.cpython-312.pyc
│  │        │  │     ├─ _print_versions.cpython-312.pyc
│  │        │  │     ├─ _tester.cpython-312.pyc
│  │        │  │     ├─ _test_decorators.cpython-312.pyc
│  │        │  │     ├─ _validators.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ _config
│  │        │  │  ├─ config.py
│  │        │  │  ├─ dates.py
│  │        │  │  ├─ display.py
│  │        │  │  ├─ localization.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ config.cpython-312.pyc
│  │        │  │     ├─ dates.cpython-312.pyc
│  │        │  │     ├─ display.cpython-312.pyc
│  │        │  │     ├─ localization.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ _libs
│  │        │  │  ├─ algos.cpython-312-darwin.so
│  │        │  │  ├─ algos.pyi
│  │        │  │  ├─ arrays.cpython-312-darwin.so
│  │        │  │  ├─ arrays.pyi
│  │        │  │  ├─ byteswap.cpython-312-darwin.so
│  │        │  │  ├─ byteswap.pyi
│  │        │  │  ├─ groupby.cpython-312-darwin.so
│  │        │  │  ├─ groupby.pyi
│  │        │  │  ├─ hashing.cpython-312-darwin.so
│  │        │  │  ├─ hashing.pyi
│  │        │  │  ├─ hashtable.cpython-312-darwin.so
│  │        │  │  ├─ hashtable.pyi
│  │        │  │  ├─ index.cpython-312-darwin.so
│  │        │  │  ├─ index.pyi
│  │        │  │  ├─ indexing.cpython-312-darwin.so
│  │        │  │  ├─ indexing.pyi
│  │        │  │  ├─ internals.cpython-312-darwin.so
│  │        │  │  ├─ internals.pyi
│  │        │  │  ├─ interval.cpython-312-darwin.so
│  │        │  │  ├─ interval.pyi
│  │        │  │  ├─ join.cpython-312-darwin.so
│  │        │  │  ├─ join.pyi
│  │        │  │  ├─ json.cpython-312-darwin.so
│  │        │  │  ├─ json.pyi
│  │        │  │  ├─ lib.cpython-312-darwin.so
│  │        │  │  ├─ lib.pyi
│  │        │  │  ├─ missing.cpython-312-darwin.so
│  │        │  │  ├─ missing.pyi
│  │        │  │  ├─ ops.cpython-312-darwin.so
│  │        │  │  ├─ ops.pyi
│  │        │  │  ├─ ops_dispatch.cpython-312-darwin.so
│  │        │  │  ├─ ops_dispatch.pyi
│  │        │  │  ├─ pandas_datetime.cpython-312-darwin.so
│  │        │  │  ├─ pandas_parser.cpython-312-darwin.so
│  │        │  │  ├─ parsers.cpython-312-darwin.so
│  │        │  │  ├─ parsers.pyi
│  │        │  │  ├─ properties.cpython-312-darwin.so
│  │        │  │  ├─ properties.pyi
│  │        │  │  ├─ reshape.cpython-312-darwin.so
│  │        │  │  ├─ reshape.pyi
│  │        │  │  ├─ sas.cpython-312-darwin.so
│  │        │  │  ├─ sas.pyi
│  │        │  │  ├─ sparse.cpython-312-darwin.so
│  │        │  │  ├─ sparse.pyi
│  │        │  │  ├─ testing.cpython-312-darwin.so
│  │        │  │  ├─ testing.pyi
│  │        │  │  ├─ tslib.cpython-312-darwin.so
│  │        │  │  ├─ tslib.pyi
│  │        │  │  ├─ tslibs
│  │        │  │  │  ├─ base.cpython-312-darwin.so
│  │        │  │  │  ├─ ccalendar.cpython-312-darwin.so
│  │        │  │  │  ├─ ccalendar.pyi
│  │        │  │  │  ├─ conversion.cpython-312-darwin.so
│  │        │  │  │  ├─ conversion.pyi
│  │        │  │  │  ├─ dtypes.cpython-312-darwin.so
│  │        │  │  │  ├─ dtypes.pyi
│  │        │  │  │  ├─ fields.cpython-312-darwin.so
│  │        │  │  │  ├─ fields.pyi
│  │        │  │  │  ├─ nattype.cpython-312-darwin.so
│  │        │  │  │  ├─ nattype.pyi
│  │        │  │  │  ├─ np_datetime.cpython-312-darwin.so
│  │        │  │  │  ├─ np_datetime.pyi
│  │        │  │  │  ├─ offsets.cpython-312-darwin.so
│  │        │  │  │  ├─ offsets.pyi
│  │        │  │  │  ├─ parsing.cpython-312-darwin.so
│  │        │  │  │  ├─ parsing.pyi
│  │        │  │  │  ├─ period.cpython-312-darwin.so
│  │        │  │  │  ├─ period.pyi
│  │        │  │  │  ├─ strptime.cpython-312-darwin.so
│  │        │  │  │  ├─ strptime.pyi
│  │        │  │  │  ├─ timedeltas.cpython-312-darwin.so
│  │        │  │  │  ├─ timedeltas.pyi
│  │        │  │  │  ├─ timestamps.cpython-312-darwin.so
│  │        │  │  │  ├─ timestamps.pyi
│  │        │  │  │  ├─ timezones.cpython-312-darwin.so
│  │        │  │  │  ├─ timezones.pyi
│  │        │  │  │  ├─ tzconversion.cpython-312-darwin.so
│  │        │  │  │  ├─ tzconversion.pyi
│  │        │  │  │  ├─ vectorized.cpython-312-darwin.so
│  │        │  │  │  ├─ vectorized.pyi
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ window
│  │        │  │  │  ├─ aggregations.cpython-312-darwin.so
│  │        │  │  │  ├─ aggregations.pyi
│  │        │  │  │  ├─ indexers.cpython-312-darwin.so
│  │        │  │  │  ├─ indexers.pyi
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ writers.cpython-312-darwin.so
│  │        │  │  ├─ writers.pyi
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ _testing
│  │        │  │  ├─ asserters.py
│  │        │  │  ├─ compat.py
│  │        │  │  ├─ contexts.py
│  │        │  │  ├─ _hypothesis.py
│  │        │  │  ├─ _io.py
│  │        │  │  ├─ _warnings.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ asserters.cpython-312.pyc
│  │        │  │     ├─ compat.cpython-312.pyc
│  │        │  │     ├─ contexts.cpython-312.pyc
│  │        │  │     ├─ _hypothesis.cpython-312.pyc
│  │        │  │     ├─ _io.cpython-312.pyc
│  │        │  │     ├─ _warnings.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ _typing.py
│  │        │  ├─ _version.py
│  │        │  ├─ _version_meson.py
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     ├─ conftest.cpython-312.pyc
│  │        │     ├─ testing.cpython-312.pyc
│  │        │     ├─ _typing.cpython-312.pyc
│  │        │     ├─ _version.cpython-312.pyc
│  │        │     ├─ _version_meson.cpython-312.pyc
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ pandas-2.2.3.dist-info
│  │        │  ├─ entry_points.txt
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ REQUESTED
│  │        │  └─ WHEEL
│  │        ├─ pip
│  │        │  ├─ py.typed
│  │        │  ├─ _internal
│  │        │  │  ├─ build_env.py
│  │        │  │  ├─ cache.py
│  │        │  │  ├─ cli
│  │        │  │  │  ├─ autocompletion.py
│  │        │  │  │  ├─ base_command.py
│  │        │  │  │  ├─ cmdoptions.py
│  │        │  │  │  ├─ command_context.py
│  │        │  │  │  ├─ index_command.py
│  │        │  │  │  ├─ main.py
│  │        │  │  │  ├─ main_parser.py
│  │        │  │  │  ├─ parser.py
│  │        │  │  │  ├─ progress_bars.py
│  │        │  │  │  ├─ req_command.py
│  │        │  │  │  ├─ spinners.py
│  │        │  │  │  ├─ status_codes.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ autocompletion.cpython-312.pyc
│  │        │  │  │     ├─ base_command.cpython-312.pyc
│  │        │  │  │     ├─ cmdoptions.cpython-312.pyc
│  │        │  │  │     ├─ command_context.cpython-312.pyc
│  │        │  │  │     ├─ index_command.cpython-312.pyc
│  │        │  │  │     ├─ main.cpython-312.pyc
│  │        │  │  │     ├─ main_parser.cpython-312.pyc
│  │        │  │  │     ├─ parser.cpython-312.pyc
│  │        │  │  │     ├─ progress_bars.cpython-312.pyc
│  │        │  │  │     ├─ req_command.cpython-312.pyc
│  │        │  │  │     ├─ spinners.cpython-312.pyc
│  │        │  │  │     ├─ status_codes.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ commands
│  │        │  │  │  ├─ cache.py
│  │        │  │  │  ├─ check.py
│  │        │  │  │  ├─ completion.py
│  │        │  │  │  ├─ configuration.py
│  │        │  │  │  ├─ debug.py
│  │        │  │  │  ├─ download.py
│  │        │  │  │  ├─ freeze.py
│  │        │  │  │  ├─ hash.py
│  │        │  │  │  ├─ help.py
│  │        │  │  │  ├─ index.py
│  │        │  │  │  ├─ inspect.py
│  │        │  │  │  ├─ install.py
│  │        │  │  │  ├─ list.py
│  │        │  │  │  ├─ lock.py
│  │        │  │  │  ├─ search.py
│  │        │  │  │  ├─ show.py
│  │        │  │  │  ├─ uninstall.py
│  │        │  │  │  ├─ wheel.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ cache.cpython-312.pyc
│  │        │  │  │     ├─ check.cpython-312.pyc
│  │        │  │  │     ├─ completion.cpython-312.pyc
│  │        │  │  │     ├─ configuration.cpython-312.pyc
│  │        │  │  │     ├─ debug.cpython-312.pyc
│  │        │  │  │     ├─ download.cpython-312.pyc
│  │        │  │  │     ├─ freeze.cpython-312.pyc
│  │        │  │  │     ├─ hash.cpython-312.pyc
│  │        │  │  │     ├─ help.cpython-312.pyc
│  │        │  │  │     ├─ index.cpython-312.pyc
│  │        │  │  │     ├─ inspect.cpython-312.pyc
│  │        │  │  │     ├─ install.cpython-312.pyc
│  │        │  │  │     ├─ list.cpython-312.pyc
│  │        │  │  │     ├─ lock.cpython-312.pyc
│  │        │  │  │     ├─ search.cpython-312.pyc
│  │        │  │  │     ├─ show.cpython-312.pyc
│  │        │  │  │     ├─ uninstall.cpython-312.pyc
│  │        │  │  │     ├─ wheel.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ configuration.py
│  │        │  │  ├─ distributions
│  │        │  │  │  ├─ base.py
│  │        │  │  │  ├─ installed.py
│  │        │  │  │  ├─ sdist.py
│  │        │  │  │  ├─ wheel.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ base.cpython-312.pyc
│  │        │  │  │     ├─ installed.cpython-312.pyc
│  │        │  │  │     ├─ sdist.cpython-312.pyc
│  │        │  │  │     ├─ wheel.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ exceptions.py
│  │        │  │  ├─ index
│  │        │  │  │  ├─ collector.py
│  │        │  │  │  ├─ package_finder.py
│  │        │  │  │  ├─ sources.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ collector.cpython-312.pyc
│  │        │  │  │     ├─ package_finder.cpython-312.pyc
│  │        │  │  │     ├─ sources.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ locations
│  │        │  │  │  ├─ base.py
│  │        │  │  │  ├─ _distutils.py
│  │        │  │  │  ├─ _sysconfig.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ base.cpython-312.pyc
│  │        │  │  │     ├─ _distutils.cpython-312.pyc
│  │        │  │  │     ├─ _sysconfig.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ main.py
│  │        │  │  ├─ metadata
│  │        │  │  │  ├─ base.py
│  │        │  │  │  ├─ importlib
│  │        │  │  │  │  ├─ _compat.py
│  │        │  │  │  │  ├─ _dists.py
│  │        │  │  │  │  ├─ _envs.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ _compat.cpython-312.pyc
│  │        │  │  │  │     ├─ _dists.cpython-312.pyc
│  │        │  │  │  │     ├─ _envs.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ pkg_resources.py
│  │        │  │  │  ├─ _json.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ base.cpython-312.pyc
│  │        │  │  │     ├─ pkg_resources.cpython-312.pyc
│  │        │  │  │     ├─ _json.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ models
│  │        │  │  │  ├─ candidate.py
│  │        │  │  │  ├─ direct_url.py
│  │        │  │  │  ├─ format_control.py
│  │        │  │  │  ├─ index.py
│  │        │  │  │  ├─ installation_report.py
│  │        │  │  │  ├─ link.py
│  │        │  │  │  ├─ pylock.py
│  │        │  │  │  ├─ scheme.py
│  │        │  │  │  ├─ search_scope.py
│  │        │  │  │  ├─ selection_prefs.py
│  │        │  │  │  ├─ target_python.py
│  │        │  │  │  ├─ wheel.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ candidate.cpython-312.pyc
│  │        │  │  │     ├─ direct_url.cpython-312.pyc
│  │        │  │  │     ├─ format_control.cpython-312.pyc
│  │        │  │  │     ├─ index.cpython-312.pyc
│  │        │  │  │     ├─ installation_report.cpython-312.pyc
│  │        │  │  │     ├─ link.cpython-312.pyc
│  │        │  │  │     ├─ pylock.cpython-312.pyc
│  │        │  │  │     ├─ scheme.cpython-312.pyc
│  │        │  │  │     ├─ search_scope.cpython-312.pyc
│  │        │  │  │     ├─ selection_prefs.cpython-312.pyc
│  │        │  │  │     ├─ target_python.cpython-312.pyc
│  │        │  │  │     ├─ wheel.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ network
│  │        │  │  │  ├─ auth.py
│  │        │  │  │  ├─ cache.py
│  │        │  │  │  ├─ download.py
│  │        │  │  │  ├─ lazy_wheel.py
│  │        │  │  │  ├─ session.py
│  │        │  │  │  ├─ utils.py
│  │        │  │  │  ├─ xmlrpc.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ auth.cpython-312.pyc
│  │        │  │  │     ├─ cache.cpython-312.pyc
│  │        │  │  │     ├─ download.cpython-312.pyc
│  │        │  │  │     ├─ lazy_wheel.cpython-312.pyc
│  │        │  │  │     ├─ session.cpython-312.pyc
│  │        │  │  │     ├─ utils.cpython-312.pyc
│  │        │  │  │     ├─ xmlrpc.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ operations
│  │        │  │  │  ├─ build
│  │        │  │  │  │  ├─ build_tracker.py
│  │        │  │  │  │  ├─ metadata.py
│  │        │  │  │  │  ├─ metadata_editable.py
│  │        │  │  │  │  ├─ metadata_legacy.py
│  │        │  │  │  │  ├─ wheel.py
│  │        │  │  │  │  ├─ wheel_editable.py
│  │        │  │  │  │  ├─ wheel_legacy.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ build_tracker.cpython-312.pyc
│  │        │  │  │  │     ├─ metadata.cpython-312.pyc
│  │        │  │  │  │     ├─ metadata_editable.cpython-312.pyc
│  │        │  │  │  │     ├─ metadata_legacy.cpython-312.pyc
│  │        │  │  │  │     ├─ wheel.cpython-312.pyc
│  │        │  │  │  │     ├─ wheel_editable.cpython-312.pyc
│  │        │  │  │  │     ├─ wheel_legacy.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ check.py
│  │        │  │  │  ├─ freeze.py
│  │        │  │  │  ├─ install
│  │        │  │  │  │  ├─ editable_legacy.py
│  │        │  │  │  │  ├─ wheel.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ editable_legacy.cpython-312.pyc
│  │        │  │  │  │     ├─ wheel.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ prepare.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ check.cpython-312.pyc
│  │        │  │  │     ├─ freeze.cpython-312.pyc
│  │        │  │  │     ├─ prepare.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ pyproject.py
│  │        │  │  ├─ req
│  │        │  │  │  ├─ constructors.py
│  │        │  │  │  ├─ req_dependency_group.py
│  │        │  │  │  ├─ req_file.py
│  │        │  │  │  ├─ req_install.py
│  │        │  │  │  ├─ req_set.py
│  │        │  │  │  ├─ req_uninstall.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ constructors.cpython-312.pyc
│  │        │  │  │     ├─ req_dependency_group.cpython-312.pyc
│  │        │  │  │     ├─ req_file.cpython-312.pyc
│  │        │  │  │     ├─ req_install.cpython-312.pyc
│  │        │  │  │     ├─ req_set.cpython-312.pyc
│  │        │  │  │     ├─ req_uninstall.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ resolution
│  │        │  │  │  ├─ base.py
│  │        │  │  │  ├─ legacy
│  │        │  │  │  │  ├─ resolver.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ resolver.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ resolvelib
│  │        │  │  │  │  ├─ base.py
│  │        │  │  │  │  ├─ candidates.py
│  │        │  │  │  │  ├─ factory.py
│  │        │  │  │  │  ├─ found_candidates.py
│  │        │  │  │  │  ├─ provider.py
│  │        │  │  │  │  ├─ reporter.py
│  │        │  │  │  │  ├─ requirements.py
│  │        │  │  │  │  ├─ resolver.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ base.cpython-312.pyc
│  │        │  │  │  │     ├─ candidates.cpython-312.pyc
│  │        │  │  │  │     ├─ factory.cpython-312.pyc
│  │        │  │  │  │     ├─ found_candidates.cpython-312.pyc
│  │        │  │  │  │     ├─ provider.cpython-312.pyc
│  │        │  │  │  │     ├─ reporter.cpython-312.pyc
│  │        │  │  │  │     ├─ requirements.cpython-312.pyc
│  │        │  │  │  │     ├─ resolver.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ base.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ self_outdated_check.py
│  │        │  │  ├─ utils
│  │        │  │  │  ├─ appdirs.py
│  │        │  │  │  ├─ compat.py
│  │        │  │  │  ├─ compatibility_tags.py
│  │        │  │  │  ├─ datetime.py
│  │        │  │  │  ├─ deprecation.py
│  │        │  │  │  ├─ direct_url_helpers.py
│  │        │  │  │  ├─ egg_link.py
│  │        │  │  │  ├─ entrypoints.py
│  │        │  │  │  ├─ filesystem.py
│  │        │  │  │  ├─ filetypes.py
│  │        │  │  │  ├─ glibc.py
│  │        │  │  │  ├─ hashes.py
│  │        │  │  │  ├─ logging.py
│  │        │  │  │  ├─ misc.py
│  │        │  │  │  ├─ packaging.py
│  │        │  │  │  ├─ retry.py
│  │        │  │  │  ├─ setuptools_build.py
│  │        │  │  │  ├─ subprocess.py
│  │        │  │  │  ├─ temp_dir.py
│  │        │  │  │  ├─ unpacking.py
│  │        │  │  │  ├─ urls.py
│  │        │  │  │  ├─ virtualenv.py
│  │        │  │  │  ├─ wheel.py
│  │        │  │  │  ├─ _jaraco_text.py
│  │        │  │  │  ├─ _log.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ appdirs.cpython-312.pyc
│  │        │  │  │     ├─ compat.cpython-312.pyc
│  │        │  │  │     ├─ compatibility_tags.cpython-312.pyc
│  │        │  │  │     ├─ datetime.cpython-312.pyc
│  │        │  │  │     ├─ deprecation.cpython-312.pyc
│  │        │  │  │     ├─ direct_url_helpers.cpython-312.pyc
│  │        │  │  │     ├─ egg_link.cpython-312.pyc
│  │        │  │  │     ├─ entrypoints.cpython-312.pyc
│  │        │  │  │     ├─ filesystem.cpython-312.pyc
│  │        │  │  │     ├─ filetypes.cpython-312.pyc
│  │        │  │  │     ├─ glibc.cpython-312.pyc
│  │        │  │  │     ├─ hashes.cpython-312.pyc
│  │        │  │  │     ├─ logging.cpython-312.pyc
│  │        │  │  │     ├─ misc.cpython-312.pyc
│  │        │  │  │     ├─ packaging.cpython-312.pyc
│  │        │  │  │     ├─ retry.cpython-312.pyc
│  │        │  │  │     ├─ setuptools_build.cpython-312.pyc
│  │        │  │  │     ├─ subprocess.cpython-312.pyc
│  │        │  │  │     ├─ temp_dir.cpython-312.pyc
│  │        │  │  │     ├─ unpacking.cpython-312.pyc
│  │        │  │  │     ├─ urls.cpython-312.pyc
│  │        │  │  │     ├─ virtualenv.cpython-312.pyc
│  │        │  │  │     ├─ wheel.cpython-312.pyc
│  │        │  │  │     ├─ _jaraco_text.cpython-312.pyc
│  │        │  │  │     ├─ _log.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ vcs
│  │        │  │  │  ├─ bazaar.py
│  │        │  │  │  ├─ git.py
│  │        │  │  │  ├─ mercurial.py
│  │        │  │  │  ├─ subversion.py
│  │        │  │  │  ├─ versioncontrol.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ bazaar.cpython-312.pyc
│  │        │  │  │     ├─ git.cpython-312.pyc
│  │        │  │  │     ├─ mercurial.cpython-312.pyc
│  │        │  │  │     ├─ subversion.cpython-312.pyc
│  │        │  │  │     ├─ versioncontrol.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ wheel_builder.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ build_env.cpython-312.pyc
│  │        │  │     ├─ cache.cpython-312.pyc
│  │        │  │     ├─ configuration.cpython-312.pyc
│  │        │  │     ├─ exceptions.cpython-312.pyc
│  │        │  │     ├─ main.cpython-312.pyc
│  │        │  │     ├─ pyproject.cpython-312.pyc
│  │        │  │     ├─ self_outdated_check.cpython-312.pyc
│  │        │  │     ├─ wheel_builder.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ _vendor
│  │        │  │  ├─ cachecontrol
│  │        │  │  │  ├─ adapter.py
│  │        │  │  │  ├─ cache.py
│  │        │  │  │  ├─ caches
│  │        │  │  │  │  ├─ file_cache.py
│  │        │  │  │  │  ├─ redis_cache.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ file_cache.cpython-312.pyc
│  │        │  │  │  │     ├─ redis_cache.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ controller.py
│  │        │  │  │  ├─ filewrapper.py
│  │        │  │  │  ├─ heuristics.py
│  │        │  │  │  ├─ py.typed
│  │        │  │  │  ├─ serialize.py
│  │        │  │  │  ├─ wrapper.py
│  │        │  │  │  ├─ _cmd.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ adapter.cpython-312.pyc
│  │        │  │  │     ├─ cache.cpython-312.pyc
│  │        │  │  │     ├─ controller.cpython-312.pyc
│  │        │  │  │     ├─ filewrapper.cpython-312.pyc
│  │        │  │  │     ├─ heuristics.cpython-312.pyc
│  │        │  │  │     ├─ serialize.cpython-312.pyc
│  │        │  │  │     ├─ wrapper.cpython-312.pyc
│  │        │  │  │     ├─ _cmd.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ certifi
│  │        │  │  │  ├─ cacert.pem
│  │        │  │  │  ├─ core.py
│  │        │  │  │  ├─ py.typed
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ __main__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ core.cpython-312.pyc
│  │        │  │  │     ├─ __init__.cpython-312.pyc
│  │        │  │  │     └─ __main__.cpython-312.pyc
│  │        │  │  ├─ dependency_groups
│  │        │  │  │  ├─ py.typed
│  │        │  │  │  ├─ _implementation.py
│  │        │  │  │  ├─ _lint_dependency_groups.py
│  │        │  │  │  ├─ _pip_wrapper.py
│  │        │  │  │  ├─ _toml_compat.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ __main__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ _implementation.cpython-312.pyc
│  │        │  │  │     ├─ _lint_dependency_groups.cpython-312.pyc
│  │        │  │  │     ├─ _pip_wrapper.cpython-312.pyc
│  │        │  │  │     ├─ _toml_compat.cpython-312.pyc
│  │        │  │  │     ├─ __init__.cpython-312.pyc
│  │        │  │  │     └─ __main__.cpython-312.pyc
│  │        │  │  ├─ distlib
│  │        │  │  │  ├─ compat.py
│  │        │  │  │  ├─ database.py
│  │        │  │  │  ├─ index.py
│  │        │  │  │  ├─ locators.py
│  │        │  │  │  ├─ manifest.py
│  │        │  │  │  ├─ markers.py
│  │        │  │  │  ├─ metadata.py
│  │        │  │  │  ├─ resources.py
│  │        │  │  │  ├─ scripts.py
│  │        │  │  │  ├─ t32.exe
│  │        │  │  │  ├─ t64-arm.exe
│  │        │  │  │  ├─ t64.exe
│  │        │  │  │  ├─ util.py
│  │        │  │  │  ├─ version.py
│  │        │  │  │  ├─ w32.exe
│  │        │  │  │  ├─ w64-arm.exe
│  │        │  │  │  ├─ w64.exe
│  │        │  │  │  ├─ wheel.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ compat.cpython-312.pyc
│  │        │  │  │     ├─ database.cpython-312.pyc
│  │        │  │  │     ├─ index.cpython-312.pyc
│  │        │  │  │     ├─ locators.cpython-312.pyc
│  │        │  │  │     ├─ manifest.cpython-312.pyc
│  │        │  │  │     ├─ markers.cpython-312.pyc
│  │        │  │  │     ├─ metadata.cpython-312.pyc
│  │        │  │  │     ├─ resources.cpython-312.pyc
│  │        │  │  │     ├─ scripts.cpython-312.pyc
│  │        │  │  │     ├─ util.cpython-312.pyc
│  │        │  │  │     ├─ version.cpython-312.pyc
│  │        │  │  │     ├─ wheel.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ distro
│  │        │  │  │  ├─ distro.py
│  │        │  │  │  ├─ py.typed
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ __main__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ distro.cpython-312.pyc
│  │        │  │  │     ├─ __init__.cpython-312.pyc
│  │        │  │  │     └─ __main__.cpython-312.pyc
│  │        │  │  ├─ idna
│  │        │  │  │  ├─ codec.py
│  │        │  │  │  ├─ compat.py
│  │        │  │  │  ├─ core.py
│  │        │  │  │  ├─ idnadata.py
│  │        │  │  │  ├─ intranges.py
│  │        │  │  │  ├─ package_data.py
│  │        │  │  │  ├─ py.typed
│  │        │  │  │  ├─ uts46data.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ codec.cpython-312.pyc
│  │        │  │  │     ├─ compat.cpython-312.pyc
│  │        │  │  │     ├─ core.cpython-312.pyc
│  │        │  │  │     ├─ idnadata.cpython-312.pyc
│  │        │  │  │     ├─ intranges.cpython-312.pyc
│  │        │  │  │     ├─ package_data.cpython-312.pyc
│  │        │  │  │     ├─ uts46data.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ msgpack
│  │        │  │  │  ├─ exceptions.py
│  │        │  │  │  ├─ ext.py
│  │        │  │  │  ├─ fallback.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ exceptions.cpython-312.pyc
│  │        │  │  │     ├─ ext.cpython-312.pyc
│  │        │  │  │     ├─ fallback.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ packaging
│  │        │  │  │  ├─ licenses
│  │        │  │  │  │  ├─ _spdx.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ _spdx.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ markers.py
│  │        │  │  │  ├─ metadata.py
│  │        │  │  │  ├─ py.typed
│  │        │  │  │  ├─ requirements.py
│  │        │  │  │  ├─ specifiers.py
│  │        │  │  │  ├─ tags.py
│  │        │  │  │  ├─ utils.py
│  │        │  │  │  ├─ version.py
│  │        │  │  │  ├─ _elffile.py
│  │        │  │  │  ├─ _manylinux.py
│  │        │  │  │  ├─ _musllinux.py
│  │        │  │  │  ├─ _parser.py
│  │        │  │  │  ├─ _structures.py
│  │        │  │  │  ├─ _tokenizer.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ markers.cpython-312.pyc
│  │        │  │  │     ├─ metadata.cpython-312.pyc
│  │        │  │  │     ├─ requirements.cpython-312.pyc
│  │        │  │  │     ├─ specifiers.cpython-312.pyc
│  │        │  │  │     ├─ tags.cpython-312.pyc
│  │        │  │  │     ├─ utils.cpython-312.pyc
│  │        │  │  │     ├─ version.cpython-312.pyc
│  │        │  │  │     ├─ _elffile.cpython-312.pyc
│  │        │  │  │     ├─ _manylinux.cpython-312.pyc
│  │        │  │  │     ├─ _musllinux.cpython-312.pyc
│  │        │  │  │     ├─ _parser.cpython-312.pyc
│  │        │  │  │     ├─ _structures.cpython-312.pyc
│  │        │  │  │     ├─ _tokenizer.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ pkg_resources
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ platformdirs
│  │        │  │  │  ├─ android.py
│  │        │  │  │  ├─ api.py
│  │        │  │  │  ├─ macos.py
│  │        │  │  │  ├─ py.typed
│  │        │  │  │  ├─ unix.py
│  │        │  │  │  ├─ version.py
│  │        │  │  │  ├─ windows.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ __main__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ android.cpython-312.pyc
│  │        │  │  │     ├─ api.cpython-312.pyc
│  │        │  │  │     ├─ macos.cpython-312.pyc
│  │        │  │  │     ├─ unix.cpython-312.pyc
│  │        │  │  │     ├─ version.cpython-312.pyc
│  │        │  │  │     ├─ windows.cpython-312.pyc
│  │        │  │  │     ├─ __init__.cpython-312.pyc
│  │        │  │  │     └─ __main__.cpython-312.pyc
│  │        │  │  ├─ pygments
│  │        │  │  │  ├─ console.py
│  │        │  │  │  ├─ filter.py
│  │        │  │  │  ├─ filters
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ formatter.py
│  │        │  │  │  ├─ formatters
│  │        │  │  │  │  ├─ _mapping.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ _mapping.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ lexer.py
│  │        │  │  │  ├─ lexers
│  │        │  │  │  │  ├─ python.py
│  │        │  │  │  │  ├─ _mapping.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ python.cpython-312.pyc
│  │        │  │  │  │     ├─ _mapping.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ modeline.py
│  │        │  │  │  ├─ plugin.py
│  │        │  │  │  ├─ regexopt.py
│  │        │  │  │  ├─ scanner.py
│  │        │  │  │  ├─ sphinxext.py
│  │        │  │  │  ├─ style.py
│  │        │  │  │  ├─ styles
│  │        │  │  │  │  ├─ _mapping.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ _mapping.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ token.py
│  │        │  │  │  ├─ unistring.py
│  │        │  │  │  ├─ util.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ __main__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ console.cpython-312.pyc
│  │        │  │  │     ├─ filter.cpython-312.pyc
│  │        │  │  │     ├─ formatter.cpython-312.pyc
│  │        │  │  │     ├─ lexer.cpython-312.pyc
│  │        │  │  │     ├─ modeline.cpython-312.pyc
│  │        │  │  │     ├─ plugin.cpython-312.pyc
│  │        │  │  │     ├─ regexopt.cpython-312.pyc
│  │        │  │  │     ├─ scanner.cpython-312.pyc
│  │        │  │  │     ├─ sphinxext.cpython-312.pyc
│  │        │  │  │     ├─ style.cpython-312.pyc
│  │        │  │  │     ├─ token.cpython-312.pyc
│  │        │  │  │     ├─ unistring.cpython-312.pyc
│  │        │  │  │     ├─ util.cpython-312.pyc
│  │        │  │  │     ├─ __init__.cpython-312.pyc
│  │        │  │  │     └─ __main__.cpython-312.pyc
│  │        │  │  ├─ pyproject_hooks
│  │        │  │  │  ├─ py.typed
│  │        │  │  │  ├─ _impl.py
│  │        │  │  │  ├─ _in_process
│  │        │  │  │  │  ├─ _in_process.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ _in_process.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ _impl.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ requests
│  │        │  │  │  ├─ adapters.py
│  │        │  │  │  ├─ api.py
│  │        │  │  │  ├─ auth.py
│  │        │  │  │  ├─ certs.py
│  │        │  │  │  ├─ compat.py
│  │        │  │  │  ├─ cookies.py
│  │        │  │  │  ├─ exceptions.py
│  │        │  │  │  ├─ help.py
│  │        │  │  │  ├─ hooks.py
│  │        │  │  │  ├─ models.py
│  │        │  │  │  ├─ packages.py
│  │        │  │  │  ├─ sessions.py
│  │        │  │  │  ├─ status_codes.py
│  │        │  │  │  ├─ structures.py
│  │        │  │  │  ├─ utils.py
│  │        │  │  │  ├─ _internal_utils.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ __pycache__
│  │        │  │  │  │  ├─ adapters.cpython-312.pyc
│  │        │  │  │  │  ├─ api.cpython-312.pyc
│  │        │  │  │  │  ├─ auth.cpython-312.pyc
│  │        │  │  │  │  ├─ certs.cpython-312.pyc
│  │        │  │  │  │  ├─ compat.cpython-312.pyc
│  │        │  │  │  │  ├─ cookies.cpython-312.pyc
│  │        │  │  │  │  ├─ exceptions.cpython-312.pyc
│  │        │  │  │  │  ├─ help.cpython-312.pyc
│  │        │  │  │  │  ├─ hooks.cpython-312.pyc
│  │        │  │  │  │  ├─ models.cpython-312.pyc
│  │        │  │  │  │  ├─ packages.cpython-312.pyc
│  │        │  │  │  │  ├─ sessions.cpython-312.pyc
│  │        │  │  │  │  ├─ status_codes.cpython-312.pyc
│  │        │  │  │  │  ├─ structures.cpython-312.pyc
│  │        │  │  │  │  ├─ utils.cpython-312.pyc
│  │        │  │  │  │  ├─ _internal_utils.cpython-312.pyc
│  │        │  │  │  │  ├─ __init__.cpython-312.pyc
│  │        │  │  │  │  └─ __version__.cpython-312.pyc
│  │        │  │  │  └─ __version__.py
│  │        │  │  ├─ resolvelib
│  │        │  │  │  ├─ providers.py
│  │        │  │  │  ├─ py.typed
│  │        │  │  │  ├─ reporters.py
│  │        │  │  │  ├─ resolvers
│  │        │  │  │  │  ├─ abstract.py
│  │        │  │  │  │  ├─ criterion.py
│  │        │  │  │  │  ├─ exceptions.py
│  │        │  │  │  │  ├─ resolution.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ abstract.cpython-312.pyc
│  │        │  │  │  │     ├─ criterion.cpython-312.pyc
│  │        │  │  │  │     ├─ exceptions.cpython-312.pyc
│  │        │  │  │  │     ├─ resolution.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ structs.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ providers.cpython-312.pyc
│  │        │  │  │     ├─ reporters.cpython-312.pyc
│  │        │  │  │     ├─ structs.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ rich
│  │        │  │  │  ├─ abc.py
│  │        │  │  │  ├─ align.py
│  │        │  │  │  ├─ ansi.py
│  │        │  │  │  ├─ bar.py
│  │        │  │  │  ├─ box.py
│  │        │  │  │  ├─ cells.py
│  │        │  │  │  ├─ color.py
│  │        │  │  │  ├─ color_triplet.py
│  │        │  │  │  ├─ columns.py
│  │        │  │  │  ├─ console.py
│  │        │  │  │  ├─ constrain.py
│  │        │  │  │  ├─ containers.py
│  │        │  │  │  ├─ control.py
│  │        │  │  │  ├─ default_styles.py
│  │        │  │  │  ├─ diagnose.py
│  │        │  │  │  ├─ emoji.py
│  │        │  │  │  ├─ errors.py
│  │        │  │  │  ├─ filesize.py
│  │        │  │  │  ├─ file_proxy.py
│  │        │  │  │  ├─ highlighter.py
│  │        │  │  │  ├─ json.py
│  │        │  │  │  ├─ jupyter.py
│  │        │  │  │  ├─ layout.py
│  │        │  │  │  ├─ live.py
│  │        │  │  │  ├─ live_render.py
│  │        │  │  │  ├─ logging.py
│  │        │  │  │  ├─ markup.py
│  │        │  │  │  ├─ measure.py
│  │        │  │  │  ├─ padding.py
│  │        │  │  │  ├─ pager.py
│  │        │  │  │  ├─ palette.py
│  │        │  │  │  ├─ panel.py
│  │        │  │  │  ├─ pretty.py
│  │        │  │  │  ├─ progress.py
│  │        │  │  │  ├─ progress_bar.py
│  │        │  │  │  ├─ prompt.py
│  │        │  │  │  ├─ protocol.py
│  │        │  │  │  ├─ py.typed
│  │        │  │  │  ├─ region.py
│  │        │  │  │  ├─ repr.py
│  │        │  │  │  ├─ rule.py
│  │        │  │  │  ├─ scope.py
│  │        │  │  │  ├─ screen.py
│  │        │  │  │  ├─ segment.py
│  │        │  │  │  ├─ spinner.py
│  │        │  │  │  ├─ status.py
│  │        │  │  │  ├─ style.py
│  │        │  │  │  ├─ styled.py
│  │        │  │  │  ├─ syntax.py
│  │        │  │  │  ├─ table.py
│  │        │  │  │  ├─ terminal_theme.py
│  │        │  │  │  ├─ text.py
│  │        │  │  │  ├─ theme.py
│  │        │  │  │  ├─ themes.py
│  │        │  │  │  ├─ traceback.py
│  │        │  │  │  ├─ tree.py
│  │        │  │  │  ├─ _cell_widths.py
│  │        │  │  │  ├─ _emoji_codes.py
│  │        │  │  │  ├─ _emoji_replace.py
│  │        │  │  │  ├─ _export_format.py
│  │        │  │  │  ├─ _extension.py
│  │        │  │  │  ├─ _fileno.py
│  │        │  │  │  ├─ _inspect.py
│  │        │  │  │  ├─ _log_render.py
│  │        │  │  │  ├─ _loop.py
│  │        │  │  │  ├─ _null_file.py
│  │        │  │  │  ├─ _palettes.py
│  │        │  │  │  ├─ _pick.py
│  │        │  │  │  ├─ _ratio.py
│  │        │  │  │  ├─ _spinners.py
│  │        │  │  │  ├─ _stack.py
│  │        │  │  │  ├─ _timer.py
│  │        │  │  │  ├─ _win32_console.py
│  │        │  │  │  ├─ _windows.py
│  │        │  │  │  ├─ _windows_renderer.py
│  │        │  │  │  ├─ _wrap.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ __main__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ abc.cpython-312.pyc
│  │        │  │  │     ├─ align.cpython-312.pyc
│  │        │  │  │     ├─ ansi.cpython-312.pyc
│  │        │  │  │     ├─ bar.cpython-312.pyc
│  │        │  │  │     ├─ box.cpython-312.pyc
│  │        │  │  │     ├─ cells.cpython-312.pyc
│  │        │  │  │     ├─ color.cpython-312.pyc
│  │        │  │  │     ├─ color_triplet.cpython-312.pyc
│  │        │  │  │     ├─ columns.cpython-312.pyc
│  │        │  │  │     ├─ console.cpython-312.pyc
│  │        │  │  │     ├─ constrain.cpython-312.pyc
│  │        │  │  │     ├─ containers.cpython-312.pyc
│  │        │  │  │     ├─ control.cpython-312.pyc
│  │        │  │  │     ├─ default_styles.cpython-312.pyc
│  │        │  │  │     ├─ diagnose.cpython-312.pyc
│  │        │  │  │     ├─ emoji.cpython-312.pyc
│  │        │  │  │     ├─ errors.cpython-312.pyc
│  │        │  │  │     ├─ filesize.cpython-312.pyc
│  │        │  │  │     ├─ file_proxy.cpython-312.pyc
│  │        │  │  │     ├─ highlighter.cpython-312.pyc
│  │        │  │  │     ├─ json.cpython-312.pyc
│  │        │  │  │     ├─ jupyter.cpython-312.pyc
│  │        │  │  │     ├─ layout.cpython-312.pyc
│  │        │  │  │     ├─ live.cpython-312.pyc
│  │        │  │  │     ├─ live_render.cpython-312.pyc
│  │        │  │  │     ├─ logging.cpython-312.pyc
│  │        │  │  │     ├─ markup.cpython-312.pyc
│  │        │  │  │     ├─ measure.cpython-312.pyc
│  │        │  │  │     ├─ padding.cpython-312.pyc
│  │        │  │  │     ├─ pager.cpython-312.pyc
│  │        │  │  │     ├─ palette.cpython-312.pyc
│  │        │  │  │     ├─ panel.cpython-312.pyc
│  │        │  │  │     ├─ pretty.cpython-312.pyc
│  │        │  │  │     ├─ progress.cpython-312.pyc
│  │        │  │  │     ├─ progress_bar.cpython-312.pyc
│  │        │  │  │     ├─ prompt.cpython-312.pyc
│  │        │  │  │     ├─ protocol.cpython-312.pyc
│  │        │  │  │     ├─ region.cpython-312.pyc
│  │        │  │  │     ├─ repr.cpython-312.pyc
│  │        │  │  │     ├─ rule.cpython-312.pyc
│  │        │  │  │     ├─ scope.cpython-312.pyc
│  │        │  │  │     ├─ screen.cpython-312.pyc
│  │        │  │  │     ├─ segment.cpython-312.pyc
│  │        │  │  │     ├─ spinner.cpython-312.pyc
│  │        │  │  │     ├─ status.cpython-312.pyc
│  │        │  │  │     ├─ style.cpython-312.pyc
│  │        │  │  │     ├─ styled.cpython-312.pyc
│  │        │  │  │     ├─ syntax.cpython-312.pyc
│  │        │  │  │     ├─ table.cpython-312.pyc
│  │        │  │  │     ├─ terminal_theme.cpython-312.pyc
│  │        │  │  │     ├─ text.cpython-312.pyc
│  │        │  │  │     ├─ theme.cpython-312.pyc
│  │        │  │  │     ├─ themes.cpython-312.pyc
│  │        │  │  │     ├─ traceback.cpython-312.pyc
│  │        │  │  │     ├─ tree.cpython-312.pyc
│  │        │  │  │     ├─ _cell_widths.cpython-312.pyc
│  │        │  │  │     ├─ _emoji_codes.cpython-312.pyc
│  │        │  │  │     ├─ _emoji_replace.cpython-312.pyc
│  │        │  │  │     ├─ _export_format.cpython-312.pyc
│  │        │  │  │     ├─ _extension.cpython-312.pyc
│  │        │  │  │     ├─ _fileno.cpython-312.pyc
│  │        │  │  │     ├─ _inspect.cpython-312.pyc
│  │        │  │  │     ├─ _log_render.cpython-312.pyc
│  │        │  │  │     ├─ _loop.cpython-312.pyc
│  │        │  │  │     ├─ _null_file.cpython-312.pyc
│  │        │  │  │     ├─ _palettes.cpython-312.pyc
│  │        │  │  │     ├─ _pick.cpython-312.pyc
│  │        │  │  │     ├─ _ratio.cpython-312.pyc
│  │        │  │  │     ├─ _spinners.cpython-312.pyc
│  │        │  │  │     ├─ _stack.cpython-312.pyc
│  │        │  │  │     ├─ _timer.cpython-312.pyc
│  │        │  │  │     ├─ _win32_console.cpython-312.pyc
│  │        │  │  │     ├─ _windows.cpython-312.pyc
│  │        │  │  │     ├─ _windows_renderer.cpython-312.pyc
│  │        │  │  │     ├─ _wrap.cpython-312.pyc
│  │        │  │  │     ├─ __init__.cpython-312.pyc
│  │        │  │  │     └─ __main__.cpython-312.pyc
│  │        │  │  ├─ tomli
│  │        │  │  │  ├─ py.typed
│  │        │  │  │  ├─ _parser.py
│  │        │  │  │  ├─ _re.py
│  │        │  │  │  ├─ _types.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ _parser.cpython-312.pyc
│  │        │  │  │     ├─ _re.cpython-312.pyc
│  │        │  │  │     ├─ _types.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ tomli_w
│  │        │  │  │  ├─ py.typed
│  │        │  │  │  ├─ _writer.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ _writer.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ truststore
│  │        │  │  │  ├─ py.typed
│  │        │  │  │  ├─ _api.py
│  │        │  │  │  ├─ _macos.py
│  │        │  │  │  ├─ _openssl.py
│  │        │  │  │  ├─ _ssl_constants.py
│  │        │  │  │  ├─ _windows.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ _api.cpython-312.pyc
│  │        │  │  │     ├─ _macos.cpython-312.pyc
│  │        │  │  │     ├─ _openssl.cpython-312.pyc
│  │        │  │  │     ├─ _ssl_constants.cpython-312.pyc
│  │        │  │  │     ├─ _windows.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ typing_extensions.py
│  │        │  │  ├─ urllib3
│  │        │  │  │  ├─ connection.py
│  │        │  │  │  ├─ connectionpool.py
│  │        │  │  │  ├─ contrib
│  │        │  │  │  │  ├─ appengine.py
│  │        │  │  │  │  ├─ ntlmpool.py
│  │        │  │  │  │  ├─ pyopenssl.py
│  │        │  │  │  │  ├─ securetransport.py
│  │        │  │  │  │  ├─ socks.py
│  │        │  │  │  │  ├─ _appengine_environ.py
│  │        │  │  │  │  ├─ _securetransport
│  │        │  │  │  │  │  ├─ bindings.py
│  │        │  │  │  │  │  ├─ low_level.py
│  │        │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │     ├─ bindings.cpython-312.pyc
│  │        │  │  │  │  │     ├─ low_level.cpython-312.pyc
│  │        │  │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ appengine.cpython-312.pyc
│  │        │  │  │  │     ├─ ntlmpool.cpython-312.pyc
│  │        │  │  │  │     ├─ pyopenssl.cpython-312.pyc
│  │        │  │  │  │     ├─ securetransport.cpython-312.pyc
│  │        │  │  │  │     ├─ socks.cpython-312.pyc
│  │        │  │  │  │     ├─ _appengine_environ.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ exceptions.py
│  │        │  │  │  ├─ fields.py
│  │        │  │  │  ├─ filepost.py
│  │        │  │  │  ├─ packages
│  │        │  │  │  │  ├─ backports
│  │        │  │  │  │  │  ├─ makefile.py
│  │        │  │  │  │  │  ├─ weakref_finalize.py
│  │        │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │     ├─ makefile.cpython-312.pyc
│  │        │  │  │  │  │     ├─ weakref_finalize.cpython-312.pyc
│  │        │  │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  │  ├─ six.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ six.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ poolmanager.py
│  │        │  │  │  ├─ request.py
│  │        │  │  │  ├─ response.py
│  │        │  │  │  ├─ util
│  │        │  │  │  │  ├─ connection.py
│  │        │  │  │  │  ├─ proxy.py
│  │        │  │  │  │  ├─ queue.py
│  │        │  │  │  │  ├─ request.py
│  │        │  │  │  │  ├─ response.py
│  │        │  │  │  │  ├─ retry.py
│  │        │  │  │  │  ├─ ssltransport.py
│  │        │  │  │  │  ├─ ssl_.py
│  │        │  │  │  │  ├─ ssl_match_hostname.py
│  │        │  │  │  │  ├─ timeout.py
│  │        │  │  │  │  ├─ url.py
│  │        │  │  │  │  ├─ wait.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ connection.cpython-312.pyc
│  │        │  │  │  │     ├─ proxy.cpython-312.pyc
│  │        │  │  │  │     ├─ queue.cpython-312.pyc
│  │        │  │  │  │     ├─ request.cpython-312.pyc
│  │        │  │  │  │     ├─ response.cpython-312.pyc
│  │        │  │  │  │     ├─ retry.cpython-312.pyc
│  │        │  │  │  │     ├─ ssltransport.cpython-312.pyc
│  │        │  │  │  │     ├─ ssl_.cpython-312.pyc
│  │        │  │  │  │     ├─ ssl_match_hostname.cpython-312.pyc
│  │        │  │  │  │     ├─ timeout.cpython-312.pyc
│  │        │  │  │  │     ├─ url.cpython-312.pyc
│  │        │  │  │  │     ├─ wait.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ _collections.py
│  │        │  │  │  ├─ _version.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ connection.cpython-312.pyc
│  │        │  │  │     ├─ connectionpool.cpython-312.pyc
│  │        │  │  │     ├─ exceptions.cpython-312.pyc
│  │        │  │  │     ├─ fields.cpython-312.pyc
│  │        │  │  │     ├─ filepost.cpython-312.pyc
│  │        │  │  │     ├─ poolmanager.cpython-312.pyc
│  │        │  │  │     ├─ request.cpython-312.pyc
│  │        │  │  │     ├─ response.cpython-312.pyc
│  │        │  │  │     ├─ _collections.cpython-312.pyc
│  │        │  │  │     ├─ _version.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ vendor.txt
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ typing_extensions.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ __init__.py
│  │        │  ├─ __main__.py
│  │        │  ├─ __pip-runner__.py
│  │        │  └─ __pycache__
│  │        │     ├─ __init__.cpython-312.pyc
│  │        │     ├─ __main__.cpython-312.pyc
│  │        │     └─ __pip-runner__.cpython-312.pyc
│  │        ├─ pip-25.1.1.dist-info
│  │        │  ├─ entry_points.txt
│  │        │  ├─ INSTALLER
│  │        │  ├─ licenses
│  │        │  │  ├─ AUTHORS.txt
│  │        │  │  └─ LICENSE.txt
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ REQUESTED
│  │        │  ├─ top_level.txt
│  │        │  └─ WHEEL
│  │        ├─ pydantic
│  │        │  ├─ aliases.py
│  │        │  ├─ alias_generators.py
│  │        │  ├─ annotated_handlers.py
│  │        │  ├─ class_validators.py
│  │        │  ├─ color.py
│  │        │  ├─ config.py
│  │        │  ├─ dataclasses.py
│  │        │  ├─ datetime_parse.py
│  │        │  ├─ decorator.py
│  │        │  ├─ deprecated
│  │        │  │  ├─ class_validators.py
│  │        │  │  ├─ config.py
│  │        │  │  ├─ copy_internals.py
│  │        │  │  ├─ decorator.py
│  │        │  │  ├─ json.py
│  │        │  │  ├─ parse.py
│  │        │  │  ├─ tools.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ class_validators.cpython-312.pyc
│  │        │  │     ├─ config.cpython-312.pyc
│  │        │  │     ├─ copy_internals.cpython-312.pyc
│  │        │  │     ├─ decorator.cpython-312.pyc
│  │        │  │     ├─ json.cpython-312.pyc
│  │        │  │     ├─ parse.cpython-312.pyc
│  │        │  │     ├─ tools.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ env_settings.py
│  │        │  ├─ errors.py
│  │        │  ├─ error_wrappers.py
│  │        │  ├─ experimental
│  │        │  │  ├─ arguments_schema.py
│  │        │  │  ├─ pipeline.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ arguments_schema.cpython-312.pyc
│  │        │  │     ├─ pipeline.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ fields.py
│  │        │  ├─ functional_serializers.py
│  │        │  ├─ functional_validators.py
│  │        │  ├─ generics.py
│  │        │  ├─ json.py
│  │        │  ├─ json_schema.py
│  │        │  ├─ main.py
│  │        │  ├─ mypy.py
│  │        │  ├─ networks.py
│  │        │  ├─ parse.py
│  │        │  ├─ plugin
│  │        │  │  ├─ _loader.py
│  │        │  │  ├─ _schema_validator.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ _loader.cpython-312.pyc
│  │        │  │     ├─ _schema_validator.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ py.typed
│  │        │  ├─ root_model.py
│  │        │  ├─ schema.py
│  │        │  ├─ tools.py
│  │        │  ├─ types.py
│  │        │  ├─ type_adapter.py
│  │        │  ├─ typing.py
│  │        │  ├─ utils.py
│  │        │  ├─ v1
│  │        │  │  ├─ annotated_types.py
│  │        │  │  ├─ class_validators.py
│  │        │  │  ├─ color.py
│  │        │  │  ├─ config.py
│  │        │  │  ├─ dataclasses.py
│  │        │  │  ├─ datetime_parse.py
│  │        │  │  ├─ decorator.py
│  │        │  │  ├─ env_settings.py
│  │        │  │  ├─ errors.py
│  │        │  │  ├─ error_wrappers.py
│  │        │  │  ├─ fields.py
│  │        │  │  ├─ generics.py
│  │        │  │  ├─ json.py
│  │        │  │  ├─ main.py
│  │        │  │  ├─ mypy.py
│  │        │  │  ├─ networks.py
│  │        │  │  ├─ parse.py
│  │        │  │  ├─ py.typed
│  │        │  │  ├─ schema.py
│  │        │  │  ├─ tools.py
│  │        │  │  ├─ types.py
│  │        │  │  ├─ typing.py
│  │        │  │  ├─ utils.py
│  │        │  │  ├─ validators.py
│  │        │  │  ├─ version.py
│  │        │  │  ├─ _hypothesis_plugin.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ annotated_types.cpython-312.pyc
│  │        │  │     ├─ class_validators.cpython-312.pyc
│  │        │  │     ├─ color.cpython-312.pyc
│  │        │  │     ├─ config.cpython-312.pyc
│  │        │  │     ├─ dataclasses.cpython-312.pyc
│  │        │  │     ├─ datetime_parse.cpython-312.pyc
│  │        │  │     ├─ decorator.cpython-312.pyc
│  │        │  │     ├─ env_settings.cpython-312.pyc
│  │        │  │     ├─ errors.cpython-312.pyc
│  │        │  │     ├─ error_wrappers.cpython-312.pyc
│  │        │  │     ├─ fields.cpython-312.pyc
│  │        │  │     ├─ generics.cpython-312.pyc
│  │        │  │     ├─ json.cpython-312.pyc
│  │        │  │     ├─ main.cpython-312.pyc
│  │        │  │     ├─ mypy.cpython-312.pyc
│  │        │  │     ├─ networks.cpython-312.pyc
│  │        │  │     ├─ parse.cpython-312.pyc
│  │        │  │     ├─ schema.cpython-312.pyc
│  │        │  │     ├─ tools.cpython-312.pyc
│  │        │  │     ├─ types.cpython-312.pyc
│  │        │  │     ├─ typing.cpython-312.pyc
│  │        │  │     ├─ utils.cpython-312.pyc
│  │        │  │     ├─ validators.cpython-312.pyc
│  │        │  │     ├─ version.cpython-312.pyc
│  │        │  │     ├─ _hypothesis_plugin.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ validate_call_decorator.py
│  │        │  ├─ validators.py
│  │        │  ├─ version.py
│  │        │  ├─ warnings.py
│  │        │  ├─ _internal
│  │        │  │  ├─ _config.py
│  │        │  │  ├─ _core_metadata.py
│  │        │  │  ├─ _core_utils.py
│  │        │  │  ├─ _dataclasses.py
│  │        │  │  ├─ _decorators.py
│  │        │  │  ├─ _decorators_v1.py
│  │        │  │  ├─ _discriminated_union.py
│  │        │  │  ├─ _docs_extraction.py
│  │        │  │  ├─ _fields.py
│  │        │  │  ├─ _forward_ref.py
│  │        │  │  ├─ _generate_schema.py
│  │        │  │  ├─ _generics.py
│  │        │  │  ├─ _git.py
│  │        │  │  ├─ _import_utils.py
│  │        │  │  ├─ _internal_dataclass.py
│  │        │  │  ├─ _known_annotated_metadata.py
│  │        │  │  ├─ _mock_val_ser.py
│  │        │  │  ├─ _model_construction.py
│  │        │  │  ├─ _namespace_utils.py
│  │        │  │  ├─ _repr.py
│  │        │  │  ├─ _schema_gather.py
│  │        │  │  ├─ _schema_generation_shared.py
│  │        │  │  ├─ _serializers.py
│  │        │  │  ├─ _signature.py
│  │        │  │  ├─ _typing_extra.py
│  │        │  │  ├─ _utils.py
│  │        │  │  ├─ _validate_call.py
│  │        │  │  ├─ _validators.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ _config.cpython-312.pyc
│  │        │  │     ├─ _core_metadata.cpython-312.pyc
│  │        │  │     ├─ _core_utils.cpython-312.pyc
│  │        │  │     ├─ _dataclasses.cpython-312.pyc
│  │        │  │     ├─ _decorators.cpython-312.pyc
│  │        │  │     ├─ _decorators_v1.cpython-312.pyc
│  │        │  │     ├─ _discriminated_union.cpython-312.pyc
│  │        │  │     ├─ _docs_extraction.cpython-312.pyc
│  │        │  │     ├─ _fields.cpython-312.pyc
│  │        │  │     ├─ _forward_ref.cpython-312.pyc
│  │        │  │     ├─ _generate_schema.cpython-312.pyc
│  │        │  │     ├─ _generics.cpython-312.pyc
│  │        │  │     ├─ _git.cpython-312.pyc
│  │        │  │     ├─ _import_utils.cpython-312.pyc
│  │        │  │     ├─ _internal_dataclass.cpython-312.pyc
│  │        │  │     ├─ _known_annotated_metadata.cpython-312.pyc
│  │        │  │     ├─ _mock_val_ser.cpython-312.pyc
│  │        │  │     ├─ _model_construction.cpython-312.pyc
│  │        │  │     ├─ _namespace_utils.cpython-312.pyc
│  │        │  │     ├─ _repr.cpython-312.pyc
│  │        │  │     ├─ _schema_gather.cpython-312.pyc
│  │        │  │     ├─ _schema_generation_shared.cpython-312.pyc
│  │        │  │     ├─ _serializers.cpython-312.pyc
│  │        │  │     ├─ _signature.cpython-312.pyc
│  │        │  │     ├─ _typing_extra.cpython-312.pyc
│  │        │  │     ├─ _utils.cpython-312.pyc
│  │        │  │     ├─ _validate_call.cpython-312.pyc
│  │        │  │     ├─ _validators.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ _migration.py
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     ├─ aliases.cpython-312.pyc
│  │        │     ├─ alias_generators.cpython-312.pyc
│  │        │     ├─ annotated_handlers.cpython-312.pyc
│  │        │     ├─ class_validators.cpython-312.pyc
│  │        │     ├─ color.cpython-312.pyc
│  │        │     ├─ config.cpython-312.pyc
│  │        │     ├─ dataclasses.cpython-312.pyc
│  │        │     ├─ datetime_parse.cpython-312.pyc
│  │        │     ├─ decorator.cpython-312.pyc
│  │        │     ├─ env_settings.cpython-312.pyc
│  │        │     ├─ errors.cpython-312.pyc
│  │        │     ├─ error_wrappers.cpython-312.pyc
│  │        │     ├─ fields.cpython-312.pyc
│  │        │     ├─ functional_serializers.cpython-312.pyc
│  │        │     ├─ functional_validators.cpython-312.pyc
│  │        │     ├─ generics.cpython-312.pyc
│  │        │     ├─ json.cpython-312.pyc
│  │        │     ├─ json_schema.cpython-312.pyc
│  │        │     ├─ main.cpython-312.pyc
│  │        │     ├─ mypy.cpython-312.pyc
│  │        │     ├─ networks.cpython-312.pyc
│  │        │     ├─ parse.cpython-312.pyc
│  │        │     ├─ root_model.cpython-312.pyc
│  │        │     ├─ schema.cpython-312.pyc
│  │        │     ├─ tools.cpython-312.pyc
│  │        │     ├─ types.cpython-312.pyc
│  │        │     ├─ type_adapter.cpython-312.pyc
│  │        │     ├─ typing.cpython-312.pyc
│  │        │     ├─ utils.cpython-312.pyc
│  │        │     ├─ validate_call_decorator.cpython-312.pyc
│  │        │     ├─ validators.cpython-312.pyc
│  │        │     ├─ version.cpython-312.pyc
│  │        │     ├─ warnings.cpython-312.pyc
│  │        │     ├─ _migration.cpython-312.pyc
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ pydantic-2.11.5.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ licenses
│  │        │  │  └─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  └─ WHEEL
│  │        ├─ pydantic_core
│  │        │  ├─ core_schema.py
│  │        │  ├─ py.typed
│  │        │  ├─ _pydantic_core.cpython-312-darwin.so
│  │        │  ├─ _pydantic_core.pyi
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     ├─ core_schema.cpython-312.pyc
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ pydantic_core-2.33.2.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ licenses
│  │        │  │  └─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  └─ WHEEL
│  │        ├─ pydantic_extra_types
│  │        │  ├─ color.py
│  │        │  ├─ coordinate.py
│  │        │  ├─ country.py
│  │        │  ├─ currency_code.py
│  │        │  ├─ domain.py
│  │        │  ├─ epoch.py
│  │        │  ├─ isbn.py
│  │        │  ├─ language_code.py
│  │        │  ├─ mac_address.py
│  │        │  ├─ mongo_object_id.py
│  │        │  ├─ path.py
│  │        │  ├─ payment.py
│  │        │  ├─ pendulum_dt.py
│  │        │  ├─ phone_numbers.py
│  │        │  ├─ py.typed
│  │        │  ├─ routing_number.py
│  │        │  ├─ s3.py
│  │        │  ├─ script_code.py
│  │        │  ├─ semantic_version.py
│  │        │  ├─ semver.py
│  │        │  ├─ timezone_name.py
│  │        │  ├─ ulid.py
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     ├─ color.cpython-312.pyc
│  │        │     ├─ coordinate.cpython-312.pyc
│  │        │     ├─ country.cpython-312.pyc
│  │        │     ├─ currency_code.cpython-312.pyc
│  │        │     ├─ domain.cpython-312.pyc
│  │        │     ├─ epoch.cpython-312.pyc
│  │        │     ├─ isbn.cpython-312.pyc
│  │        │     ├─ language_code.cpython-312.pyc
│  │        │     ├─ mac_address.cpython-312.pyc
│  │        │     ├─ mongo_object_id.cpython-312.pyc
│  │        │     ├─ path.cpython-312.pyc
│  │        │     ├─ payment.cpython-312.pyc
│  │        │     ├─ pendulum_dt.cpython-312.pyc
│  │        │     ├─ phone_numbers.cpython-312.pyc
│  │        │     ├─ routing_number.cpython-312.pyc
│  │        │     ├─ s3.cpython-312.pyc
│  │        │     ├─ script_code.cpython-312.pyc
│  │        │     ├─ semantic_version.cpython-312.pyc
│  │        │     ├─ semver.cpython-312.pyc
│  │        │     ├─ timezone_name.cpython-312.pyc
│  │        │     ├─ ulid.cpython-312.pyc
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ pydantic_extra_types-2.10.5.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ licenses
│  │        │  │  └─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  └─ WHEEL
│  │        ├─ pydantic_settings
│  │        │  ├─ exceptions.py
│  │        │  ├─ main.py
│  │        │  ├─ py.typed
│  │        │  ├─ sources
│  │        │  │  ├─ base.py
│  │        │  │  ├─ providers
│  │        │  │  │  ├─ aws.py
│  │        │  │  │  ├─ azure.py
│  │        │  │  │  ├─ cli.py
│  │        │  │  │  ├─ dotenv.py
│  │        │  │  │  ├─ env.py
│  │        │  │  │  ├─ gcp.py
│  │        │  │  │  ├─ json.py
│  │        │  │  │  ├─ pyproject.py
│  │        │  │  │  ├─ secrets.py
│  │        │  │  │  ├─ toml.py
│  │        │  │  │  ├─ yaml.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ aws.cpython-312.pyc
│  │        │  │  │     ├─ azure.cpython-312.pyc
│  │        │  │  │     ├─ cli.cpython-312.pyc
│  │        │  │  │     ├─ dotenv.cpython-312.pyc
│  │        │  │  │     ├─ env.cpython-312.pyc
│  │        │  │  │     ├─ gcp.cpython-312.pyc
│  │        │  │  │     ├─ json.cpython-312.pyc
│  │        │  │  │     ├─ pyproject.cpython-312.pyc
│  │        │  │  │     ├─ secrets.cpython-312.pyc
│  │        │  │  │     ├─ toml.cpython-312.pyc
│  │        │  │  │     ├─ yaml.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ types.py
│  │        │  │  ├─ utils.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ base.cpython-312.pyc
│  │        │  │     ├─ types.cpython-312.pyc
│  │        │  │     ├─ utils.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ utils.py
│  │        │  ├─ version.py
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     ├─ exceptions.cpython-312.pyc
│  │        │     ├─ main.cpython-312.pyc
│  │        │     ├─ utils.cpython-312.pyc
│  │        │     ├─ version.cpython-312.pyc
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ pydantic_settings-2.9.1.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ licenses
│  │        │  │  └─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  └─ WHEEL
│  │        ├─ pygments
│  │        │  ├─ cmdline.py
│  │        │  ├─ console.py
│  │        │  ├─ filter.py
│  │        │  ├─ filters
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ formatter.py
│  │        │  ├─ formatters
│  │        │  │  ├─ bbcode.py
│  │        │  │  ├─ groff.py
│  │        │  │  ├─ html.py
│  │        │  │  ├─ img.py
│  │        │  │  ├─ irc.py
│  │        │  │  ├─ latex.py
│  │        │  │  ├─ other.py
│  │        │  │  ├─ pangomarkup.py
│  │        │  │  ├─ rtf.py
│  │        │  │  ├─ svg.py
│  │        │  │  ├─ terminal.py
│  │        │  │  ├─ terminal256.py
│  │        │  │  ├─ _mapping.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ bbcode.cpython-312.pyc
│  │        │  │     ├─ groff.cpython-312.pyc
│  │        │  │     ├─ html.cpython-312.pyc
│  │        │  │     ├─ img.cpython-312.pyc
│  │        │  │     ├─ irc.cpython-312.pyc
│  │        │  │     ├─ latex.cpython-312.pyc
│  │        │  │     ├─ other.cpython-312.pyc
│  │        │  │     ├─ pangomarkup.cpython-312.pyc
│  │        │  │     ├─ rtf.cpython-312.pyc
│  │        │  │     ├─ svg.cpython-312.pyc
│  │        │  │     ├─ terminal.cpython-312.pyc
│  │        │  │     ├─ terminal256.cpython-312.pyc
│  │        │  │     ├─ _mapping.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ lexer.py
│  │        │  ├─ lexers
│  │        │  │  ├─ actionscript.py
│  │        │  │  ├─ ada.py
│  │        │  │  ├─ agile.py
│  │        │  │  ├─ algebra.py
│  │        │  │  ├─ ambient.py
│  │        │  │  ├─ amdgpu.py
│  │        │  │  ├─ ampl.py
│  │        │  │  ├─ apdlexer.py
│  │        │  │  ├─ apl.py
│  │        │  │  ├─ archetype.py
│  │        │  │  ├─ arrow.py
│  │        │  │  ├─ arturo.py
│  │        │  │  ├─ asc.py
│  │        │  │  ├─ asm.py
│  │        │  │  ├─ asn1.py
│  │        │  │  ├─ automation.py
│  │        │  │  ├─ bare.py
│  │        │  │  ├─ basic.py
│  │        │  │  ├─ bdd.py
│  │        │  │  ├─ berry.py
│  │        │  │  ├─ bibtex.py
│  │        │  │  ├─ blueprint.py
│  │        │  │  ├─ boa.py
│  │        │  │  ├─ bqn.py
│  │        │  │  ├─ business.py
│  │        │  │  ├─ capnproto.py
│  │        │  │  ├─ carbon.py
│  │        │  │  ├─ cddl.py
│  │        │  │  ├─ chapel.py
│  │        │  │  ├─ clean.py
│  │        │  │  ├─ codeql.py
│  │        │  │  ├─ comal.py
│  │        │  │  ├─ compiled.py
│  │        │  │  ├─ configs.py
│  │        │  │  ├─ console.py
│  │        │  │  ├─ cplint.py
│  │        │  │  ├─ crystal.py
│  │        │  │  ├─ csound.py
│  │        │  │  ├─ css.py
│  │        │  │  ├─ c_cpp.py
│  │        │  │  ├─ c_like.py
│  │        │  │  ├─ d.py
│  │        │  │  ├─ dalvik.py
│  │        │  │  ├─ data.py
│  │        │  │  ├─ dax.py
│  │        │  │  ├─ devicetree.py
│  │        │  │  ├─ diff.py
│  │        │  │  ├─ dns.py
│  │        │  │  ├─ dotnet.py
│  │        │  │  ├─ dsls.py
│  │        │  │  ├─ dylan.py
│  │        │  │  ├─ ecl.py
│  │        │  │  ├─ eiffel.py
│  │        │  │  ├─ elm.py
│  │        │  │  ├─ elpi.py
│  │        │  │  ├─ email.py
│  │        │  │  ├─ erlang.py
│  │        │  │  ├─ esoteric.py
│  │        │  │  ├─ ezhil.py
│  │        │  │  ├─ factor.py
│  │        │  │  ├─ fantom.py
│  │        │  │  ├─ felix.py
│  │        │  │  ├─ fift.py
│  │        │  │  ├─ floscript.py
│  │        │  │  ├─ forth.py
│  │        │  │  ├─ fortran.py
│  │        │  │  ├─ foxpro.py
│  │        │  │  ├─ freefem.py
│  │        │  │  ├─ func.py
│  │        │  │  ├─ functional.py
│  │        │  │  ├─ futhark.py
│  │        │  │  ├─ gcodelexer.py
│  │        │  │  ├─ gdscript.py
│  │        │  │  ├─ gleam.py
│  │        │  │  ├─ go.py
│  │        │  │  ├─ grammar_notation.py
│  │        │  │  ├─ graph.py
│  │        │  │  ├─ graphics.py
│  │        │  │  ├─ graphql.py
│  │        │  │  ├─ graphviz.py
│  │        │  │  ├─ gsql.py
│  │        │  │  ├─ hare.py
│  │        │  │  ├─ haskell.py
│  │        │  │  ├─ haxe.py
│  │        │  │  ├─ hdl.py
│  │        │  │  ├─ hexdump.py
│  │        │  │  ├─ html.py
│  │        │  │  ├─ idl.py
│  │        │  │  ├─ igor.py
│  │        │  │  ├─ inferno.py
│  │        │  │  ├─ installers.py
│  │        │  │  ├─ int_fiction.py
│  │        │  │  ├─ iolang.py
│  │        │  │  ├─ j.py
│  │        │  │  ├─ javascript.py
│  │        │  │  ├─ jmespath.py
│  │        │  │  ├─ jslt.py
│  │        │  │  ├─ json5.py
│  │        │  │  ├─ jsonnet.py
│  │        │  │  ├─ jsx.py
│  │        │  │  ├─ julia.py
│  │        │  │  ├─ jvm.py
│  │        │  │  ├─ kuin.py
│  │        │  │  ├─ kusto.py
│  │        │  │  ├─ ldap.py
│  │        │  │  ├─ lean.py
│  │        │  │  ├─ lilypond.py
│  │        │  │  ├─ lisp.py
│  │        │  │  ├─ macaulay2.py
│  │        │  │  ├─ make.py
│  │        │  │  ├─ maple.py
│  │        │  │  ├─ markup.py
│  │        │  │  ├─ math.py
│  │        │  │  ├─ matlab.py
│  │        │  │  ├─ maxima.py
│  │        │  │  ├─ meson.py
│  │        │  │  ├─ mime.py
│  │        │  │  ├─ minecraft.py
│  │        │  │  ├─ mips.py
│  │        │  │  ├─ ml.py
│  │        │  │  ├─ modeling.py
│  │        │  │  ├─ modula2.py
│  │        │  │  ├─ mojo.py
│  │        │  │  ├─ monte.py
│  │        │  │  ├─ mosel.py
│  │        │  │  ├─ ncl.py
│  │        │  │  ├─ nimrod.py
│  │        │  │  ├─ nit.py
│  │        │  │  ├─ nix.py
│  │        │  │  ├─ numbair.py
│  │        │  │  ├─ oberon.py
│  │        │  │  ├─ objective.py
│  │        │  │  ├─ ooc.py
│  │        │  │  ├─ openscad.py
│  │        │  │  ├─ other.py
│  │        │  │  ├─ parasail.py
│  │        │  │  ├─ parsers.py
│  │        │  │  ├─ pascal.py
│  │        │  │  ├─ pawn.py
│  │        │  │  ├─ pddl.py
│  │        │  │  ├─ perl.py
│  │        │  │  ├─ phix.py
│  │        │  │  ├─ php.py
│  │        │  │  ├─ pointless.py
│  │        │  │  ├─ pony.py
│  │        │  │  ├─ praat.py
│  │        │  │  ├─ procfile.py
│  │        │  │  ├─ prolog.py
│  │        │  │  ├─ promql.py
│  │        │  │  ├─ prql.py
│  │        │  │  ├─ ptx.py
│  │        │  │  ├─ python.py
│  │        │  │  ├─ q.py
│  │        │  │  ├─ qlik.py
│  │        │  │  ├─ qvt.py
│  │        │  │  ├─ r.py
│  │        │  │  ├─ rdf.py
│  │        │  │  ├─ rebol.py
│  │        │  │  ├─ rego.py
│  │        │  │  ├─ resource.py
│  │        │  │  ├─ ride.py
│  │        │  │  ├─ rita.py
│  │        │  │  ├─ rnc.py
│  │        │  │  ├─ roboconf.py
│  │        │  │  ├─ robotframework.py
│  │        │  │  ├─ ruby.py
│  │        │  │  ├─ rust.py
│  │        │  │  ├─ sas.py
│  │        │  │  ├─ savi.py
│  │        │  │  ├─ scdoc.py
│  │        │  │  ├─ scripting.py
│  │        │  │  ├─ sgf.py
│  │        │  │  ├─ shell.py
│  │        │  │  ├─ sieve.py
│  │        │  │  ├─ slash.py
│  │        │  │  ├─ smalltalk.py
│  │        │  │  ├─ smithy.py
│  │        │  │  ├─ smv.py
│  │        │  │  ├─ snobol.py
│  │        │  │  ├─ solidity.py
│  │        │  │  ├─ soong.py
│  │        │  │  ├─ sophia.py
│  │        │  │  ├─ special.py
│  │        │  │  ├─ spice.py
│  │        │  │  ├─ sql.py
│  │        │  │  ├─ srcinfo.py
│  │        │  │  ├─ stata.py
│  │        │  │  ├─ supercollider.py
│  │        │  │  ├─ tablegen.py
│  │        │  │  ├─ tact.py
│  │        │  │  ├─ tal.py
│  │        │  │  ├─ tcl.py
│  │        │  │  ├─ teal.py
│  │        │  │  ├─ templates.py
│  │        │  │  ├─ teraterm.py
│  │        │  │  ├─ testing.py
│  │        │  │  ├─ text.py
│  │        │  │  ├─ textedit.py
│  │        │  │  ├─ textfmts.py
│  │        │  │  ├─ theorem.py
│  │        │  │  ├─ thingsdb.py
│  │        │  │  ├─ tlb.py
│  │        │  │  ├─ tls.py
│  │        │  │  ├─ tnt.py
│  │        │  │  ├─ trafficscript.py
│  │        │  │  ├─ typoscript.py
│  │        │  │  ├─ typst.py
│  │        │  │  ├─ ul4.py
│  │        │  │  ├─ unicon.py
│  │        │  │  ├─ urbi.py
│  │        │  │  ├─ usd.py
│  │        │  │  ├─ varnish.py
│  │        │  │  ├─ verification.py
│  │        │  │  ├─ verifpal.py
│  │        │  │  ├─ vip.py
│  │        │  │  ├─ vyper.py
│  │        │  │  ├─ web.py
│  │        │  │  ├─ webassembly.py
│  │        │  │  ├─ webidl.py
│  │        │  │  ├─ webmisc.py
│  │        │  │  ├─ wgsl.py
│  │        │  │  ├─ whiley.py
│  │        │  │  ├─ wowtoc.py
│  │        │  │  ├─ wren.py
│  │        │  │  ├─ x10.py
│  │        │  │  ├─ xorg.py
│  │        │  │  ├─ yang.py
│  │        │  │  ├─ yara.py
│  │        │  │  ├─ zig.py
│  │        │  │  ├─ _ada_builtins.py
│  │        │  │  ├─ _asy_builtins.py
│  │        │  │  ├─ _cl_builtins.py
│  │        │  │  ├─ _cocoa_builtins.py
│  │        │  │  ├─ _csound_builtins.py
│  │        │  │  ├─ _css_builtins.py
│  │        │  │  ├─ _googlesql_builtins.py
│  │        │  │  ├─ _julia_builtins.py
│  │        │  │  ├─ _lasso_builtins.py
│  │        │  │  ├─ _lilypond_builtins.py
│  │        │  │  ├─ _luau_builtins.py
│  │        │  │  ├─ _lua_builtins.py
│  │        │  │  ├─ _mapping.py
│  │        │  │  ├─ _mql_builtins.py
│  │        │  │  ├─ _mysql_builtins.py
│  │        │  │  ├─ _openedge_builtins.py
│  │        │  │  ├─ _php_builtins.py
│  │        │  │  ├─ _postgres_builtins.py
│  │        │  │  ├─ _qlik_builtins.py
│  │        │  │  ├─ _scheme_builtins.py
│  │        │  │  ├─ _scilab_builtins.py
│  │        │  │  ├─ _sourcemod_builtins.py
│  │        │  │  ├─ _stan_builtins.py
│  │        │  │  ├─ _stata_builtins.py
│  │        │  │  ├─ _tsql_builtins.py
│  │        │  │  ├─ _usd_builtins.py
│  │        │  │  ├─ _vbscript_builtins.py
│  │        │  │  ├─ _vim_builtins.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ actionscript.cpython-312.pyc
│  │        │  │     ├─ ada.cpython-312.pyc
│  │        │  │     ├─ agile.cpython-312.pyc
│  │        │  │     ├─ algebra.cpython-312.pyc
│  │        │  │     ├─ ambient.cpython-312.pyc
│  │        │  │     ├─ amdgpu.cpython-312.pyc
│  │        │  │     ├─ ampl.cpython-312.pyc
│  │        │  │     ├─ apdlexer.cpython-312.pyc
│  │        │  │     ├─ apl.cpython-312.pyc
│  │        │  │     ├─ archetype.cpython-312.pyc
│  │        │  │     ├─ arrow.cpython-312.pyc
│  │        │  │     ├─ arturo.cpython-312.pyc
│  │        │  │     ├─ asc.cpython-312.pyc
│  │        │  │     ├─ asm.cpython-312.pyc
│  │        │  │     ├─ asn1.cpython-312.pyc
│  │        │  │     ├─ automation.cpython-312.pyc
│  │        │  │     ├─ bare.cpython-312.pyc
│  │        │  │     ├─ basic.cpython-312.pyc
│  │        │  │     ├─ bdd.cpython-312.pyc
│  │        │  │     ├─ berry.cpython-312.pyc
│  │        │  │     ├─ bibtex.cpython-312.pyc
│  │        │  │     ├─ blueprint.cpython-312.pyc
│  │        │  │     ├─ boa.cpython-312.pyc
│  │        │  │     ├─ bqn.cpython-312.pyc
│  │        │  │     ├─ business.cpython-312.pyc
│  │        │  │     ├─ capnproto.cpython-312.pyc
│  │        │  │     ├─ carbon.cpython-312.pyc
│  │        │  │     ├─ cddl.cpython-312.pyc
│  │        │  │     ├─ chapel.cpython-312.pyc
│  │        │  │     ├─ clean.cpython-312.pyc
│  │        │  │     ├─ codeql.cpython-312.pyc
│  │        │  │     ├─ comal.cpython-312.pyc
│  │        │  │     ├─ compiled.cpython-312.pyc
│  │        │  │     ├─ configs.cpython-312.pyc
│  │        │  │     ├─ console.cpython-312.pyc
│  │        │  │     ├─ cplint.cpython-312.pyc
│  │        │  │     ├─ crystal.cpython-312.pyc
│  │        │  │     ├─ csound.cpython-312.pyc
│  │        │  │     ├─ css.cpython-312.pyc
│  │        │  │     ├─ c_cpp.cpython-312.pyc
│  │        │  │     ├─ c_like.cpython-312.pyc
│  │        │  │     ├─ d.cpython-312.pyc
│  │        │  │     ├─ dalvik.cpython-312.pyc
│  │        │  │     ├─ data.cpython-312.pyc
│  │        │  │     ├─ dax.cpython-312.pyc
│  │        │  │     ├─ devicetree.cpython-312.pyc
│  │        │  │     ├─ diff.cpython-312.pyc
│  │        │  │     ├─ dns.cpython-312.pyc
│  │        │  │     ├─ dotnet.cpython-312.pyc
│  │        │  │     ├─ dsls.cpython-312.pyc
│  │        │  │     ├─ dylan.cpython-312.pyc
│  │        │  │     ├─ ecl.cpython-312.pyc
│  │        │  │     ├─ eiffel.cpython-312.pyc
│  │        │  │     ├─ elm.cpython-312.pyc
│  │        │  │     ├─ elpi.cpython-312.pyc
│  │        │  │     ├─ email.cpython-312.pyc
│  │        │  │     ├─ erlang.cpython-312.pyc
│  │        │  │     ├─ esoteric.cpython-312.pyc
│  │        │  │     ├─ ezhil.cpython-312.pyc
│  │        │  │     ├─ factor.cpython-312.pyc
│  │        │  │     ├─ fantom.cpython-312.pyc
│  │        │  │     ├─ felix.cpython-312.pyc
│  │        │  │     ├─ fift.cpython-312.pyc
│  │        │  │     ├─ floscript.cpython-312.pyc
│  │        │  │     ├─ forth.cpython-312.pyc
│  │        │  │     ├─ fortran.cpython-312.pyc
│  │        │  │     ├─ foxpro.cpython-312.pyc
│  │        │  │     ├─ freefem.cpython-312.pyc
│  │        │  │     ├─ func.cpython-312.pyc
│  │        │  │     ├─ functional.cpython-312.pyc
│  │        │  │     ├─ futhark.cpython-312.pyc
│  │        │  │     ├─ gcodelexer.cpython-312.pyc
│  │        │  │     ├─ gdscript.cpython-312.pyc
│  │        │  │     ├─ gleam.cpython-312.pyc
│  │        │  │     ├─ go.cpython-312.pyc
│  │        │  │     ├─ grammar_notation.cpython-312.pyc
│  │        │  │     ├─ graph.cpython-312.pyc
│  │        │  │     ├─ graphics.cpython-312.pyc
│  │        │  │     ├─ graphql.cpython-312.pyc
│  │        │  │     ├─ graphviz.cpython-312.pyc
│  │        │  │     ├─ gsql.cpython-312.pyc
│  │        │  │     ├─ hare.cpython-312.pyc
│  │        │  │     ├─ haskell.cpython-312.pyc
│  │        │  │     ├─ haxe.cpython-312.pyc
│  │        │  │     ├─ hdl.cpython-312.pyc
│  │        │  │     ├─ hexdump.cpython-312.pyc
│  │        │  │     ├─ html.cpython-312.pyc
│  │        │  │     ├─ idl.cpython-312.pyc
│  │        │  │     ├─ igor.cpython-312.pyc
│  │        │  │     ├─ inferno.cpython-312.pyc
│  │        │  │     ├─ installers.cpython-312.pyc
│  │        │  │     ├─ int_fiction.cpython-312.pyc
│  │        │  │     ├─ iolang.cpython-312.pyc
│  │        │  │     ├─ j.cpython-312.pyc
│  │        │  │     ├─ javascript.cpython-312.pyc
│  │        │  │     ├─ jmespath.cpython-312.pyc
│  │        │  │     ├─ jslt.cpython-312.pyc
│  │        │  │     ├─ json5.cpython-312.pyc
│  │        │  │     ├─ jsonnet.cpython-312.pyc
│  │        │  │     ├─ jsx.cpython-312.pyc
│  │        │  │     ├─ julia.cpython-312.pyc
│  │        │  │     ├─ jvm.cpython-312.pyc
│  │        │  │     ├─ kuin.cpython-312.pyc
│  │        │  │     ├─ kusto.cpython-312.pyc
│  │        │  │     ├─ ldap.cpython-312.pyc
│  │        │  │     ├─ lean.cpython-312.pyc
│  │        │  │     ├─ lilypond.cpython-312.pyc
│  │        │  │     ├─ lisp.cpython-312.pyc
│  │        │  │     ├─ macaulay2.cpython-312.pyc
│  │        │  │     ├─ make.cpython-312.pyc
│  │        │  │     ├─ maple.cpython-312.pyc
│  │        │  │     ├─ markup.cpython-312.pyc
│  │        │  │     ├─ math.cpython-312.pyc
│  │        │  │     ├─ matlab.cpython-312.pyc
│  │        │  │     ├─ maxima.cpython-312.pyc
│  │        │  │     ├─ meson.cpython-312.pyc
│  │        │  │     ├─ mime.cpython-312.pyc
│  │        │  │     ├─ minecraft.cpython-312.pyc
│  │        │  │     ├─ mips.cpython-312.pyc
│  │        │  │     ├─ ml.cpython-312.pyc
│  │        │  │     ├─ modeling.cpython-312.pyc
│  │        │  │     ├─ modula2.cpython-312.pyc
│  │        │  │     ├─ mojo.cpython-312.pyc
│  │        │  │     ├─ monte.cpython-312.pyc
│  │        │  │     ├─ mosel.cpython-312.pyc
│  │        │  │     ├─ ncl.cpython-312.pyc
│  │        │  │     ├─ nimrod.cpython-312.pyc
│  │        │  │     ├─ nit.cpython-312.pyc
│  │        │  │     ├─ nix.cpython-312.pyc
│  │        │  │     ├─ numbair.cpython-312.pyc
│  │        │  │     ├─ oberon.cpython-312.pyc
│  │        │  │     ├─ objective.cpython-312.pyc
│  │        │  │     ├─ ooc.cpython-312.pyc
│  │        │  │     ├─ openscad.cpython-312.pyc
│  │        │  │     ├─ other.cpython-312.pyc
│  │        │  │     ├─ parasail.cpython-312.pyc
│  │        │  │     ├─ parsers.cpython-312.pyc
│  │        │  │     ├─ pascal.cpython-312.pyc
│  │        │  │     ├─ pawn.cpython-312.pyc
│  │        │  │     ├─ pddl.cpython-312.pyc
│  │        │  │     ├─ perl.cpython-312.pyc
│  │        │  │     ├─ phix.cpython-312.pyc
│  │        │  │     ├─ php.cpython-312.pyc
│  │        │  │     ├─ pointless.cpython-312.pyc
│  │        │  │     ├─ pony.cpython-312.pyc
│  │        │  │     ├─ praat.cpython-312.pyc
│  │        │  │     ├─ procfile.cpython-312.pyc
│  │        │  │     ├─ prolog.cpython-312.pyc
│  │        │  │     ├─ promql.cpython-312.pyc
│  │        │  │     ├─ prql.cpython-312.pyc
│  │        │  │     ├─ ptx.cpython-312.pyc
│  │        │  │     ├─ python.cpython-312.pyc
│  │        │  │     ├─ q.cpython-312.pyc
│  │        │  │     ├─ qlik.cpython-312.pyc
│  │        │  │     ├─ qvt.cpython-312.pyc
│  │        │  │     ├─ r.cpython-312.pyc
│  │        │  │     ├─ rdf.cpython-312.pyc
│  │        │  │     ├─ rebol.cpython-312.pyc
│  │        │  │     ├─ rego.cpython-312.pyc
│  │        │  │     ├─ resource.cpython-312.pyc
│  │        │  │     ├─ ride.cpython-312.pyc
│  │        │  │     ├─ rita.cpython-312.pyc
│  │        │  │     ├─ rnc.cpython-312.pyc
│  │        │  │     ├─ roboconf.cpython-312.pyc
│  │        │  │     ├─ robotframework.cpython-312.pyc
│  │        │  │     ├─ ruby.cpython-312.pyc
│  │        │  │     ├─ rust.cpython-312.pyc
│  │        │  │     ├─ sas.cpython-312.pyc
│  │        │  │     ├─ savi.cpython-312.pyc
│  │        │  │     ├─ scdoc.cpython-312.pyc
│  │        │  │     ├─ scripting.cpython-312.pyc
│  │        │  │     ├─ sgf.cpython-312.pyc
│  │        │  │     ├─ shell.cpython-312.pyc
│  │        │  │     ├─ sieve.cpython-312.pyc
│  │        │  │     ├─ slash.cpython-312.pyc
│  │        │  │     ├─ smalltalk.cpython-312.pyc
│  │        │  │     ├─ smithy.cpython-312.pyc
│  │        │  │     ├─ smv.cpython-312.pyc
│  │        │  │     ├─ snobol.cpython-312.pyc
│  │        │  │     ├─ solidity.cpython-312.pyc
│  │        │  │     ├─ soong.cpython-312.pyc
│  │        │  │     ├─ sophia.cpython-312.pyc
│  │        │  │     ├─ special.cpython-312.pyc
│  │        │  │     ├─ spice.cpython-312.pyc
│  │        │  │     ├─ sql.cpython-312.pyc
│  │        │  │     ├─ srcinfo.cpython-312.pyc
│  │        │  │     ├─ stata.cpython-312.pyc
│  │        │  │     ├─ supercollider.cpython-312.pyc
│  │        │  │     ├─ tablegen.cpython-312.pyc
│  │        │  │     ├─ tact.cpython-312.pyc
│  │        │  │     ├─ tal.cpython-312.pyc
│  │        │  │     ├─ tcl.cpython-312.pyc
│  │        │  │     ├─ teal.cpython-312.pyc
│  │        │  │     ├─ templates.cpython-312.pyc
│  │        │  │     ├─ teraterm.cpython-312.pyc
│  │        │  │     ├─ testing.cpython-312.pyc
│  │        │  │     ├─ text.cpython-312.pyc
│  │        │  │     ├─ textedit.cpython-312.pyc
│  │        │  │     ├─ textfmts.cpython-312.pyc
│  │        │  │     ├─ theorem.cpython-312.pyc
│  │        │  │     ├─ thingsdb.cpython-312.pyc
│  │        │  │     ├─ tlb.cpython-312.pyc
│  │        │  │     ├─ tls.cpython-312.pyc
│  │        │  │     ├─ tnt.cpython-312.pyc
│  │        │  │     ├─ trafficscript.cpython-312.pyc
│  │        │  │     ├─ typoscript.cpython-312.pyc
│  │        │  │     ├─ typst.cpython-312.pyc
│  │        │  │     ├─ ul4.cpython-312.pyc
│  │        │  │     ├─ unicon.cpython-312.pyc
│  │        │  │     ├─ urbi.cpython-312.pyc
│  │        │  │     ├─ usd.cpython-312.pyc
│  │        │  │     ├─ varnish.cpython-312.pyc
│  │        │  │     ├─ verification.cpython-312.pyc
│  │        │  │     ├─ verifpal.cpython-312.pyc
│  │        │  │     ├─ vip.cpython-312.pyc
│  │        │  │     ├─ vyper.cpython-312.pyc
│  │        │  │     ├─ web.cpython-312.pyc
│  │        │  │     ├─ webassembly.cpython-312.pyc
│  │        │  │     ├─ webidl.cpython-312.pyc
│  │        │  │     ├─ webmisc.cpython-312.pyc
│  │        │  │     ├─ wgsl.cpython-312.pyc
│  │        │  │     ├─ whiley.cpython-312.pyc
│  │        │  │     ├─ wowtoc.cpython-312.pyc
│  │        │  │     ├─ wren.cpython-312.pyc
│  │        │  │     ├─ x10.cpython-312.pyc
│  │        │  │     ├─ xorg.cpython-312.pyc
│  │        │  │     ├─ yang.cpython-312.pyc
│  │        │  │     ├─ yara.cpython-312.pyc
│  │        │  │     ├─ zig.cpython-312.pyc
│  │        │  │     ├─ _ada_builtins.cpython-312.pyc
│  │        │  │     ├─ _asy_builtins.cpython-312.pyc
│  │        │  │     ├─ _cl_builtins.cpython-312.pyc
│  │        │  │     ├─ _cocoa_builtins.cpython-312.pyc
│  │        │  │     ├─ _csound_builtins.cpython-312.pyc
│  │        │  │     ├─ _css_builtins.cpython-312.pyc
│  │        │  │     ├─ _googlesql_builtins.cpython-312.pyc
│  │        │  │     ├─ _julia_builtins.cpython-312.pyc
│  │        │  │     ├─ _lasso_builtins.cpython-312.pyc
│  │        │  │     ├─ _lilypond_builtins.cpython-312.pyc
│  │        │  │     ├─ _luau_builtins.cpython-312.pyc
│  │        │  │     ├─ _lua_builtins.cpython-312.pyc
│  │        │  │     ├─ _mapping.cpython-312.pyc
│  │        │  │     ├─ _mql_builtins.cpython-312.pyc
│  │        │  │     ├─ _mysql_builtins.cpython-312.pyc
│  │        │  │     ├─ _openedge_builtins.cpython-312.pyc
│  │        │  │     ├─ _php_builtins.cpython-312.pyc
│  │        │  │     ├─ _postgres_builtins.cpython-312.pyc
│  │        │  │     ├─ _qlik_builtins.cpython-312.pyc
│  │        │  │     ├─ _scheme_builtins.cpython-312.pyc
│  │        │  │     ├─ _scilab_builtins.cpython-312.pyc
│  │        │  │     ├─ _sourcemod_builtins.cpython-312.pyc
│  │        │  │     ├─ _stan_builtins.cpython-312.pyc
│  │        │  │     ├─ _stata_builtins.cpython-312.pyc
│  │        │  │     ├─ _tsql_builtins.cpython-312.pyc
│  │        │  │     ├─ _usd_builtins.cpython-312.pyc
│  │        │  │     ├─ _vbscript_builtins.cpython-312.pyc
│  │        │  │     ├─ _vim_builtins.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ modeline.py
│  │        │  ├─ plugin.py
│  │        │  ├─ regexopt.py
│  │        │  ├─ scanner.py
│  │        │  ├─ sphinxext.py
│  │        │  ├─ style.py
│  │        │  ├─ styles
│  │        │  │  ├─ abap.py
│  │        │  │  ├─ algol.py
│  │        │  │  ├─ algol_nu.py
│  │        │  │  ├─ arduino.py
│  │        │  │  ├─ autumn.py
│  │        │  │  ├─ borland.py
│  │        │  │  ├─ bw.py
│  │        │  │  ├─ coffee.py
│  │        │  │  ├─ colorful.py
│  │        │  │  ├─ default.py
│  │        │  │  ├─ dracula.py
│  │        │  │  ├─ emacs.py
│  │        │  │  ├─ friendly.py
│  │        │  │  ├─ friendly_grayscale.py
│  │        │  │  ├─ fruity.py
│  │        │  │  ├─ gh_dark.py
│  │        │  │  ├─ gruvbox.py
│  │        │  │  ├─ igor.py
│  │        │  │  ├─ inkpot.py
│  │        │  │  ├─ lightbulb.py
│  │        │  │  ├─ lilypond.py
│  │        │  │  ├─ lovelace.py
│  │        │  │  ├─ manni.py
│  │        │  │  ├─ material.py
│  │        │  │  ├─ monokai.py
│  │        │  │  ├─ murphy.py
│  │        │  │  ├─ native.py
│  │        │  │  ├─ nord.py
│  │        │  │  ├─ onedark.py
│  │        │  │  ├─ paraiso_dark.py
│  │        │  │  ├─ paraiso_light.py
│  │        │  │  ├─ pastie.py
│  │        │  │  ├─ perldoc.py
│  │        │  │  ├─ rainbow_dash.py
│  │        │  │  ├─ rrt.py
│  │        │  │  ├─ sas.py
│  │        │  │  ├─ solarized.py
│  │        │  │  ├─ staroffice.py
│  │        │  │  ├─ stata_dark.py
│  │        │  │  ├─ stata_light.py
│  │        │  │  ├─ tango.py
│  │        │  │  ├─ trac.py
│  │        │  │  ├─ vim.py
│  │        │  │  ├─ vs.py
│  │        │  │  ├─ xcode.py
│  │        │  │  ├─ zenburn.py
│  │        │  │  ├─ _mapping.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ abap.cpython-312.pyc
│  │        │  │     ├─ algol.cpython-312.pyc
│  │        │  │     ├─ algol_nu.cpython-312.pyc
│  │        │  │     ├─ arduino.cpython-312.pyc
│  │        │  │     ├─ autumn.cpython-312.pyc
│  │        │  │     ├─ borland.cpython-312.pyc
│  │        │  │     ├─ bw.cpython-312.pyc
│  │        │  │     ├─ coffee.cpython-312.pyc
│  │        │  │     ├─ colorful.cpython-312.pyc
│  │        │  │     ├─ default.cpython-312.pyc
│  │        │  │     ├─ dracula.cpython-312.pyc
│  │        │  │     ├─ emacs.cpython-312.pyc
│  │        │  │     ├─ friendly.cpython-312.pyc
│  │        │  │     ├─ friendly_grayscale.cpython-312.pyc
│  │        │  │     ├─ fruity.cpython-312.pyc
│  │        │  │     ├─ gh_dark.cpython-312.pyc
│  │        │  │     ├─ gruvbox.cpython-312.pyc
│  │        │  │     ├─ igor.cpython-312.pyc
│  │        │  │     ├─ inkpot.cpython-312.pyc
│  │        │  │     ├─ lightbulb.cpython-312.pyc
│  │        │  │     ├─ lilypond.cpython-312.pyc
│  │        │  │     ├─ lovelace.cpython-312.pyc
│  │        │  │     ├─ manni.cpython-312.pyc
│  │        │  │     ├─ material.cpython-312.pyc
│  │        │  │     ├─ monokai.cpython-312.pyc
│  │        │  │     ├─ murphy.cpython-312.pyc
│  │        │  │     ├─ native.cpython-312.pyc
│  │        │  │     ├─ nord.cpython-312.pyc
│  │        │  │     ├─ onedark.cpython-312.pyc
│  │        │  │     ├─ paraiso_dark.cpython-312.pyc
│  │        │  │     ├─ paraiso_light.cpython-312.pyc
│  │        │  │     ├─ pastie.cpython-312.pyc
│  │        │  │     ├─ perldoc.cpython-312.pyc
│  │        │  │     ├─ rainbow_dash.cpython-312.pyc
│  │        │  │     ├─ rrt.cpython-312.pyc
│  │        │  │     ├─ sas.cpython-312.pyc
│  │        │  │     ├─ solarized.cpython-312.pyc
│  │        │  │     ├─ staroffice.cpython-312.pyc
│  │        │  │     ├─ stata_dark.cpython-312.pyc
│  │        │  │     ├─ stata_light.cpython-312.pyc
│  │        │  │     ├─ tango.cpython-312.pyc
│  │        │  │     ├─ trac.cpython-312.pyc
│  │        │  │     ├─ vim.cpython-312.pyc
│  │        │  │     ├─ vs.cpython-312.pyc
│  │        │  │     ├─ xcode.cpython-312.pyc
│  │        │  │     ├─ zenburn.cpython-312.pyc
│  │        │  │     ├─ _mapping.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ token.py
│  │        │  ├─ unistring.py
│  │        │  ├─ util.py
│  │        │  ├─ __init__.py
│  │        │  ├─ __main__.py
│  │        │  └─ __pycache__
│  │        │     ├─ cmdline.cpython-312.pyc
│  │        │     ├─ console.cpython-312.pyc
│  │        │     ├─ filter.cpython-312.pyc
│  │        │     ├─ formatter.cpython-312.pyc
│  │        │     ├─ lexer.cpython-312.pyc
│  │        │     ├─ modeline.cpython-312.pyc
│  │        │     ├─ plugin.cpython-312.pyc
│  │        │     ├─ regexopt.cpython-312.pyc
│  │        │     ├─ scanner.cpython-312.pyc
│  │        │     ├─ sphinxext.cpython-312.pyc
│  │        │     ├─ style.cpython-312.pyc
│  │        │     ├─ token.cpython-312.pyc
│  │        │     ├─ unistring.cpython-312.pyc
│  │        │     ├─ util.cpython-312.pyc
│  │        │     ├─ __init__.cpython-312.pyc
│  │        │     └─ __main__.cpython-312.pyc
│  │        ├─ pygments-2.19.1.dist-info
│  │        │  ├─ entry_points.txt
│  │        │  ├─ INSTALLER
│  │        │  ├─ licenses
│  │        │  │  ├─ AUTHORS
│  │        │  │  └─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  └─ WHEEL
│  │        ├─ pymongo
│  │        │  ├─ asynchronous
│  │        │  │  ├─ aggregation.py
│  │        │  │  ├─ auth.py
│  │        │  │  ├─ auth_aws.py
│  │        │  │  ├─ auth_oidc.py
│  │        │  │  ├─ bulk.py
│  │        │  │  ├─ change_stream.py
│  │        │  │  ├─ client_bulk.py
│  │        │  │  ├─ client_session.py
│  │        │  │  ├─ collection.py
│  │        │  │  ├─ command_cursor.py
│  │        │  │  ├─ cursor.py
│  │        │  │  ├─ database.py
│  │        │  │  ├─ encryption.py
│  │        │  │  ├─ helpers.py
│  │        │  │  ├─ mongo_client.py
│  │        │  │  ├─ monitor.py
│  │        │  │  ├─ network.py
│  │        │  │  ├─ pool.py
│  │        │  │  ├─ server.py
│  │        │  │  ├─ settings.py
│  │        │  │  ├─ srv_resolver.py
│  │        │  │  ├─ topology.py
│  │        │  │  ├─ uri_parser.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ aggregation.cpython-312.pyc
│  │        │  │     ├─ auth.cpython-312.pyc
│  │        │  │     ├─ auth_aws.cpython-312.pyc
│  │        │  │     ├─ auth_oidc.cpython-312.pyc
│  │        │  │     ├─ bulk.cpython-312.pyc
│  │        │  │     ├─ change_stream.cpython-312.pyc
│  │        │  │     ├─ client_bulk.cpython-312.pyc
│  │        │  │     ├─ client_session.cpython-312.pyc
│  │        │  │     ├─ collection.cpython-312.pyc
│  │        │  │     ├─ command_cursor.cpython-312.pyc
│  │        │  │     ├─ cursor.cpython-312.pyc
│  │        │  │     ├─ database.cpython-312.pyc
│  │        │  │     ├─ encryption.cpython-312.pyc
│  │        │  │     ├─ helpers.cpython-312.pyc
│  │        │  │     ├─ mongo_client.cpython-312.pyc
│  │        │  │     ├─ monitor.cpython-312.pyc
│  │        │  │     ├─ network.cpython-312.pyc
│  │        │  │     ├─ pool.cpython-312.pyc
│  │        │  │     ├─ server.cpython-312.pyc
│  │        │  │     ├─ settings.cpython-312.pyc
│  │        │  │     ├─ srv_resolver.cpython-312.pyc
│  │        │  │     ├─ topology.cpython-312.pyc
│  │        │  │     ├─ uri_parser.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ auth.py
│  │        │  ├─ auth_oidc.py
│  │        │  ├─ auth_oidc_shared.py
│  │        │  ├─ auth_shared.py
│  │        │  ├─ bulk_shared.py
│  │        │  ├─ change_stream.py
│  │        │  ├─ client_options.py
│  │        │  ├─ client_session.py
│  │        │  ├─ collation.py
│  │        │  ├─ collection.py
│  │        │  ├─ command_cursor.py
│  │        │  ├─ common.py
│  │        │  ├─ compression_support.py
│  │        │  ├─ cursor.py
│  │        │  ├─ cursor_shared.py
│  │        │  ├─ daemon.py
│  │        │  ├─ database.py
│  │        │  ├─ database_shared.py
│  │        │  ├─ driver_info.py
│  │        │  ├─ encryption.py
│  │        │  ├─ encryption_options.py
│  │        │  ├─ errors.py
│  │        │  ├─ event_loggers.py
│  │        │  ├─ hello.py
│  │        │  ├─ helpers_shared.py
│  │        │  ├─ lock.py
│  │        │  ├─ logger.py
│  │        │  ├─ max_staleness_selectors.py
│  │        │  ├─ message.py
│  │        │  ├─ mongo_client.py
│  │        │  ├─ monitoring.py
│  │        │  ├─ network_layer.py
│  │        │  ├─ ocsp_cache.py
│  │        │  ├─ ocsp_support.py
│  │        │  ├─ operations.py
│  │        │  ├─ periodic_executor.py
│  │        │  ├─ pool.py
│  │        │  ├─ pool_options.py
│  │        │  ├─ pool_shared.py
│  │        │  ├─ py.typed
│  │        │  ├─ pyopenssl_context.py
│  │        │  ├─ read_concern.py
│  │        │  ├─ read_preferences.py
│  │        │  ├─ response.py
│  │        │  ├─ results.py
│  │        │  ├─ saslprep.py
│  │        │  ├─ server_api.py
│  │        │  ├─ server_description.py
│  │        │  ├─ server_selectors.py
│  │        │  ├─ server_type.py
│  │        │  ├─ socket_checker.py
│  │        │  ├─ ssl_context.py
│  │        │  ├─ ssl_support.py
│  │        │  ├─ synchronous
│  │        │  │  ├─ aggregation.py
│  │        │  │  ├─ auth.py
│  │        │  │  ├─ auth_aws.py
│  │        │  │  ├─ auth_oidc.py
│  │        │  │  ├─ bulk.py
│  │        │  │  ├─ change_stream.py
│  │        │  │  ├─ client_bulk.py
│  │        │  │  ├─ client_session.py
│  │        │  │  ├─ collection.py
│  │        │  │  ├─ command_cursor.py
│  │        │  │  ├─ cursor.py
│  │        │  │  ├─ database.py
│  │        │  │  ├─ encryption.py
│  │        │  │  ├─ helpers.py
│  │        │  │  ├─ mongo_client.py
│  │        │  │  ├─ monitor.py
│  │        │  │  ├─ network.py
│  │        │  │  ├─ pool.py
│  │        │  │  ├─ server.py
│  │        │  │  ├─ settings.py
│  │        │  │  ├─ srv_resolver.py
│  │        │  │  ├─ topology.py
│  │        │  │  ├─ uri_parser.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ aggregation.cpython-312.pyc
│  │        │  │     ├─ auth.cpython-312.pyc
│  │        │  │     ├─ auth_aws.cpython-312.pyc
│  │        │  │     ├─ auth_oidc.cpython-312.pyc
│  │        │  │     ├─ bulk.cpython-312.pyc
│  │        │  │     ├─ change_stream.cpython-312.pyc
│  │        │  │     ├─ client_bulk.cpython-312.pyc
│  │        │  │     ├─ client_session.cpython-312.pyc
│  │        │  │     ├─ collection.cpython-312.pyc
│  │        │  │     ├─ command_cursor.cpython-312.pyc
│  │        │  │     ├─ cursor.cpython-312.pyc
│  │        │  │     ├─ database.cpython-312.pyc
│  │        │  │     ├─ encryption.cpython-312.pyc
│  │        │  │     ├─ helpers.cpython-312.pyc
│  │        │  │     ├─ mongo_client.cpython-312.pyc
│  │        │  │     ├─ monitor.cpython-312.pyc
│  │        │  │     ├─ network.cpython-312.pyc
│  │        │  │     ├─ pool.cpython-312.pyc
│  │        │  │     ├─ server.cpython-312.pyc
│  │        │  │     ├─ settings.cpython-312.pyc
│  │        │  │     ├─ srv_resolver.cpython-312.pyc
│  │        │  │     ├─ topology.cpython-312.pyc
│  │        │  │     ├─ uri_parser.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ topology_description.py
│  │        │  ├─ typings.py
│  │        │  ├─ uri_parser.py
│  │        │  ├─ uri_parser_shared.py
│  │        │  ├─ write_concern.py
│  │        │  ├─ _asyncio_lock.py
│  │        │  ├─ _asyncio_task.py
│  │        │  ├─ _azure_helpers.py
│  │        │  ├─ _client_bulk_shared.py
│  │        │  ├─ _cmessage.cpython-310-darwin.so
│  │        │  ├─ _cmessage.cpython-311-darwin.so
│  │        │  ├─ _cmessage.cpython-312-darwin.so
│  │        │  ├─ _cmessage.cpython-39-darwin.so
│  │        │  ├─ _cmessagemodule.c
│  │        │  ├─ _csot.py
│  │        │  ├─ _gcp_helpers.py
│  │        │  ├─ _version.py
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     ├─ auth.cpython-312.pyc
│  │        │     ├─ auth_oidc.cpython-312.pyc
│  │        │     ├─ auth_oidc_shared.cpython-312.pyc
│  │        │     ├─ auth_shared.cpython-312.pyc
│  │        │     ├─ bulk_shared.cpython-312.pyc
│  │        │     ├─ change_stream.cpython-312.pyc
│  │        │     ├─ client_options.cpython-312.pyc
│  │        │     ├─ client_session.cpython-312.pyc
│  │        │     ├─ collation.cpython-312.pyc
│  │        │     ├─ collection.cpython-312.pyc
│  │        │     ├─ command_cursor.cpython-312.pyc
│  │        │     ├─ common.cpython-312.pyc
│  │        │     ├─ compression_support.cpython-312.pyc
│  │        │     ├─ cursor.cpython-312.pyc
│  │        │     ├─ cursor_shared.cpython-312.pyc
│  │        │     ├─ daemon.cpython-312.pyc
│  │        │     ├─ database.cpython-312.pyc
│  │        │     ├─ database_shared.cpython-312.pyc
│  │        │     ├─ driver_info.cpython-312.pyc
│  │        │     ├─ encryption.cpython-312.pyc
│  │        │     ├─ encryption_options.cpython-312.pyc
│  │        │     ├─ errors.cpython-312.pyc
│  │        │     ├─ event_loggers.cpython-312.pyc
│  │        │     ├─ hello.cpython-312.pyc
│  │        │     ├─ helpers_shared.cpython-312.pyc
│  │        │     ├─ lock.cpython-312.pyc
│  │        │     ├─ logger.cpython-312.pyc
│  │        │     ├─ max_staleness_selectors.cpython-312.pyc
│  │        │     ├─ message.cpython-312.pyc
│  │        │     ├─ mongo_client.cpython-312.pyc
│  │        │     ├─ monitoring.cpython-312.pyc
│  │        │     ├─ network_layer.cpython-312.pyc
│  │        │     ├─ ocsp_cache.cpython-312.pyc
│  │        │     ├─ ocsp_support.cpython-312.pyc
│  │        │     ├─ operations.cpython-312.pyc
│  │        │     ├─ periodic_executor.cpython-312.pyc
│  │        │     ├─ pool.cpython-312.pyc
│  │        │     ├─ pool_options.cpython-312.pyc
│  │        │     ├─ pool_shared.cpython-312.pyc
│  │        │     ├─ pyopenssl_context.cpython-312.pyc
│  │        │     ├─ read_concern.cpython-312.pyc
│  │        │     ├─ read_preferences.cpython-312.pyc
│  │        │     ├─ response.cpython-312.pyc
│  │        │     ├─ results.cpython-312.pyc
│  │        │     ├─ saslprep.cpython-312.pyc
│  │        │     ├─ server_api.cpython-312.pyc
│  │        │     ├─ server_description.cpython-312.pyc
│  │        │     ├─ server_selectors.cpython-312.pyc
│  │        │     ├─ server_type.cpython-312.pyc
│  │        │     ├─ socket_checker.cpython-312.pyc
│  │        │     ├─ ssl_context.cpython-312.pyc
│  │        │     ├─ ssl_support.cpython-312.pyc
│  │        │     ├─ topology_description.cpython-312.pyc
│  │        │     ├─ typings.cpython-312.pyc
│  │        │     ├─ uri_parser.cpython-312.pyc
│  │        │     ├─ uri_parser_shared.cpython-312.pyc
│  │        │     ├─ write_concern.cpython-312.pyc
│  │        │     ├─ _asyncio_lock.cpython-312.pyc
│  │        │     ├─ _asyncio_task.cpython-312.pyc
│  │        │     ├─ _azure_helpers.cpython-312.pyc
│  │        │     ├─ _client_bulk_shared.cpython-312.pyc
│  │        │     ├─ _csot.cpython-312.pyc
│  │        │     ├─ _gcp_helpers.cpython-312.pyc
│  │        │     ├─ _version.cpython-312.pyc
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ pymongo-4.13.0.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ licenses
│  │        │  │  └─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ REQUESTED
│  │        │  └─ WHEEL
│  │        ├─ python_dateutil-2.9.0.post0.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ top_level.txt
│  │        │  ├─ WHEEL
│  │        │  └─ zip-safe
│  │        ├─ python_dotenv-1.1.0.dist-info
│  │        │  ├─ entry_points.txt
│  │        │  ├─ INSTALLER
│  │        │  ├─ licenses
│  │        │  │  └─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ top_level.txt
│  │        │  └─ WHEEL
│  │        ├─ python_multipart
│  │        │  ├─ decoders.py
│  │        │  ├─ exceptions.py
│  │        │  ├─ multipart.py
│  │        │  ├─ py.typed
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     ├─ decoders.cpython-312.pyc
│  │        │     ├─ exceptions.cpython-312.pyc
│  │        │     ├─ multipart.cpython-312.pyc
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ python_multipart-0.0.20.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ licenses
│  │        │  │  └─ LICENSE.txt
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  └─ WHEEL
│  │        ├─ pytz
│  │        │  ├─ exceptions.py
│  │        │  ├─ lazy.py
│  │        │  ├─ reference.py
│  │        │  ├─ tzfile.py
│  │        │  ├─ tzinfo.py
│  │        │  ├─ zoneinfo
│  │        │  │  ├─ Africa
│  │        │  │  │  ├─ Abidjan
│  │        │  │  │  ├─ Accra
│  │        │  │  │  ├─ Addis_Ababa
│  │        │  │  │  ├─ Algiers
│  │        │  │  │  ├─ Asmara
│  │        │  │  │  ├─ Asmera
│  │        │  │  │  ├─ Bamako
│  │        │  │  │  ├─ Bangui
│  │        │  │  │  ├─ Banjul
│  │        │  │  │  ├─ Bissau
│  │        │  │  │  ├─ Blantyre
│  │        │  │  │  ├─ Brazzaville
│  │        │  │  │  ├─ Bujumbura
│  │        │  │  │  ├─ Cairo
│  │        │  │  │  ├─ Casablanca
│  │        │  │  │  ├─ Ceuta
│  │        │  │  │  ├─ Conakry
│  │        │  │  │  ├─ Dakar
│  │        │  │  │  ├─ Dar_es_Salaam
│  │        │  │  │  ├─ Djibouti
│  │        │  │  │  ├─ Douala
│  │        │  │  │  ├─ El_Aaiun
│  │        │  │  │  ├─ Freetown
│  │        │  │  │  ├─ Gaborone
│  │        │  │  │  ├─ Harare
│  │        │  │  │  ├─ Johannesburg
│  │        │  │  │  ├─ Juba
│  │        │  │  │  ├─ Kampala
│  │        │  │  │  ├─ Khartoum
│  │        │  │  │  ├─ Kigali
│  │        │  │  │  ├─ Kinshasa
│  │        │  │  │  ├─ Lagos
│  │        │  │  │  ├─ Libreville
│  │        │  │  │  ├─ Lome
│  │        │  │  │  ├─ Luanda
│  │        │  │  │  ├─ Lubumbashi
│  │        │  │  │  ├─ Lusaka
│  │        │  │  │  ├─ Malabo
│  │        │  │  │  ├─ Maputo
│  │        │  │  │  ├─ Maseru
│  │        │  │  │  ├─ Mbabane
│  │        │  │  │  ├─ Mogadishu
│  │        │  │  │  ├─ Monrovia
│  │        │  │  │  ├─ Nairobi
│  │        │  │  │  ├─ Ndjamena
│  │        │  │  │  ├─ Niamey
│  │        │  │  │  ├─ Nouakchott
│  │        │  │  │  ├─ Ouagadougou
│  │        │  │  │  ├─ Porto-Novo
│  │        │  │  │  ├─ Sao_Tome
│  │        │  │  │  ├─ Timbuktu
│  │        │  │  │  ├─ Tripoli
│  │        │  │  │  ├─ Tunis
│  │        │  │  │  └─ Windhoek
│  │        │  │  ├─ America
│  │        │  │  │  ├─ Adak
│  │        │  │  │  ├─ Anchorage
│  │        │  │  │  ├─ Anguilla
│  │        │  │  │  ├─ Antigua
│  │        │  │  │  ├─ Araguaina
│  │        │  │  │  ├─ Argentina
│  │        │  │  │  │  ├─ Buenos_Aires
│  │        │  │  │  │  ├─ Catamarca
│  │        │  │  │  │  ├─ ComodRivadavia
│  │        │  │  │  │  ├─ Cordoba
│  │        │  │  │  │  ├─ Jujuy
│  │        │  │  │  │  ├─ La_Rioja
│  │        │  │  │  │  ├─ Mendoza
│  │        │  │  │  │  ├─ Rio_Gallegos
│  │        │  │  │  │  ├─ Salta
│  │        │  │  │  │  ├─ San_Juan
│  │        │  │  │  │  ├─ San_Luis
│  │        │  │  │  │  ├─ Tucuman
│  │        │  │  │  │  └─ Ushuaia
│  │        │  │  │  ├─ Aruba
│  │        │  │  │  ├─ Asuncion
│  │        │  │  │  ├─ Atikokan
│  │        │  │  │  ├─ Atka
│  │        │  │  │  ├─ Bahia
│  │        │  │  │  ├─ Bahia_Banderas
│  │        │  │  │  ├─ Barbados
│  │        │  │  │  ├─ Belem
│  │        │  │  │  ├─ Belize
│  │        │  │  │  ├─ Blanc-Sablon
│  │        │  │  │  ├─ Boa_Vista
│  │        │  │  │  ├─ Bogota
│  │        │  │  │  ├─ Boise
│  │        │  │  │  ├─ Buenos_Aires
│  │        │  │  │  ├─ Cambridge_Bay
│  │        │  │  │  ├─ Campo_Grande
│  │        │  │  │  ├─ Cancun
│  │        │  │  │  ├─ Caracas
│  │        │  │  │  ├─ Catamarca
│  │        │  │  │  ├─ Cayenne
│  │        │  │  │  ├─ Cayman
│  │        │  │  │  ├─ Chicago
│  │        │  │  │  ├─ Chihuahua
│  │        │  │  │  ├─ Ciudad_Juarez
│  │        │  │  │  ├─ Coral_Harbour
│  │        │  │  │  ├─ Cordoba
│  │        │  │  │  ├─ Costa_Rica
│  │        │  │  │  ├─ Coyhaique
│  │        │  │  │  ├─ Creston
│  │        │  │  │  ├─ Cuiaba
│  │        │  │  │  ├─ Curacao
│  │        │  │  │  ├─ Danmarkshavn
│  │        │  │  │  ├─ Dawson
│  │        │  │  │  ├─ Dawson_Creek
│  │        │  │  │  ├─ Denver
│  │        │  │  │  ├─ Detroit
│  │        │  │  │  ├─ Dominica
│  │        │  │  │  ├─ Edmonton
│  │        │  │  │  ├─ Eirunepe
│  │        │  │  │  ├─ El_Salvador
│  │        │  │  │  ├─ Ensenada
│  │        │  │  │  ├─ Fortaleza
│  │        │  │  │  ├─ Fort_Nelson
│  │        │  │  │  ├─ Fort_Wayne
│  │        │  │  │  ├─ Glace_Bay
│  │        │  │  │  ├─ Godthab
│  │        │  │  │  ├─ Goose_Bay
│  │        │  │  │  ├─ Grand_Turk
│  │        │  │  │  ├─ Grenada
│  │        │  │  │  ├─ Guadeloupe
│  │        │  │  │  ├─ Guatemala
│  │        │  │  │  ├─ Guayaquil
│  │        │  │  │  ├─ Guyana
│  │        │  │  │  ├─ Halifax
│  │        │  │  │  ├─ Havana
│  │        │  │  │  ├─ Hermosillo
│  │        │  │  │  ├─ Indiana
│  │        │  │  │  │  ├─ Indianapolis
│  │        │  │  │  │  ├─ Knox
│  │        │  │  │  │  ├─ Marengo
│  │        │  │  │  │  ├─ Petersburg
│  │        │  │  │  │  ├─ Tell_City
│  │        │  │  │  │  ├─ Vevay
│  │        │  │  │  │  ├─ Vincennes
│  │        │  │  │  │  └─ Winamac
│  │        │  │  │  ├─ Indianapolis
│  │        │  │  │  ├─ Inuvik
│  │        │  │  │  ├─ Iqaluit
│  │        │  │  │  ├─ Jamaica
│  │        │  │  │  ├─ Jujuy
│  │        │  │  │  ├─ Juneau
│  │        │  │  │  ├─ Kentucky
│  │        │  │  │  │  ├─ Louisville
│  │        │  │  │  │  └─ Monticello
│  │        │  │  │  ├─ Knox_IN
│  │        │  │  │  ├─ Kralendijk
│  │        │  │  │  ├─ La_Paz
│  │        │  │  │  ├─ Lima
│  │        │  │  │  ├─ Los_Angeles
│  │        │  │  │  ├─ Louisville
│  │        │  │  │  ├─ Lower_Princes
│  │        │  │  │  ├─ Maceio
│  │        │  │  │  ├─ Managua
│  │        │  │  │  ├─ Manaus
│  │        │  │  │  ├─ Marigot
│  │        │  │  │  ├─ Martinique
│  │        │  │  │  ├─ Matamoros
│  │        │  │  │  ├─ Mazatlan
│  │        │  │  │  ├─ Mendoza
│  │        │  │  │  ├─ Menominee
│  │        │  │  │  ├─ Merida
│  │        │  │  │  ├─ Metlakatla
│  │        │  │  │  ├─ Mexico_City
│  │        │  │  │  ├─ Miquelon
│  │        │  │  │  ├─ Moncton
│  │        │  │  │  ├─ Monterrey
│  │        │  │  │  ├─ Montevideo
│  │        │  │  │  ├─ Montreal
│  │        │  │  │  ├─ Montserrat
│  │        │  │  │  ├─ Nassau
│  │        │  │  │  ├─ New_York
│  │        │  │  │  ├─ Nipigon
│  │        │  │  │  ├─ Nome
│  │        │  │  │  ├─ Noronha
│  │        │  │  │  ├─ North_Dakota
│  │        │  │  │  │  ├─ Beulah
│  │        │  │  │  │  ├─ Center
│  │        │  │  │  │  └─ New_Salem
│  │        │  │  │  ├─ Nuuk
│  │        │  │  │  ├─ Ojinaga
│  │        │  │  │  ├─ Panama
│  │        │  │  │  ├─ Pangnirtung
│  │        │  │  │  ├─ Paramaribo
│  │        │  │  │  ├─ Phoenix
│  │        │  │  │  ├─ Port-au-Prince
│  │        │  │  │  ├─ Porto_Acre
│  │        │  │  │  ├─ Porto_Velho
│  │        │  │  │  ├─ Port_of_Spain
│  │        │  │  │  ├─ Puerto_Rico
│  │        │  │  │  ├─ Punta_Arenas
│  │        │  │  │  ├─ Rainy_River
│  │        │  │  │  ├─ Rankin_Inlet
│  │        │  │  │  ├─ Recife
│  │        │  │  │  ├─ Regina
│  │        │  │  │  ├─ Resolute
│  │        │  │  │  ├─ Rio_Branco
│  │        │  │  │  ├─ Rosario
│  │        │  │  │  ├─ Santarem
│  │        │  │  │  ├─ Santa_Isabel
│  │        │  │  │  ├─ Santiago
│  │        │  │  │  ├─ Santo_Domingo
│  │        │  │  │  ├─ Sao_Paulo
│  │        │  │  │  ├─ Scoresbysund
│  │        │  │  │  ├─ Shiprock
│  │        │  │  │  ├─ Sitka
│  │        │  │  │  ├─ St_Barthelemy
│  │        │  │  │  ├─ St_Johns
│  │        │  │  │  ├─ St_Kitts
│  │        │  │  │  ├─ St_Lucia
│  │        │  │  │  ├─ St_Thomas
│  │        │  │  │  ├─ St_Vincent
│  │        │  │  │  ├─ Swift_Current
│  │        │  │  │  ├─ Tegucigalpa
│  │        │  │  │  ├─ Thule
│  │        │  │  │  ├─ Thunder_Bay
│  │        │  │  │  ├─ Tijuana
│  │        │  │  │  ├─ Toronto
│  │        │  │  │  ├─ Tortola
│  │        │  │  │  ├─ Vancouver
│  │        │  │  │  ├─ Virgin
│  │        │  │  │  ├─ Whitehorse
│  │        │  │  │  ├─ Winnipeg
│  │        │  │  │  ├─ Yakutat
│  │        │  │  │  └─ Yellowknife
│  │        │  │  ├─ Antarctica
│  │        │  │  │  ├─ Casey
│  │        │  │  │  ├─ Davis
│  │        │  │  │  ├─ DumontDUrville
│  │        │  │  │  ├─ Macquarie
│  │        │  │  │  ├─ Mawson
│  │        │  │  │  ├─ McMurdo
│  │        │  │  │  ├─ Palmer
│  │        │  │  │  ├─ Rothera
│  │        │  │  │  ├─ South_Pole
│  │        │  │  │  ├─ Syowa
│  │        │  │  │  ├─ Troll
│  │        │  │  │  └─ Vostok
│  │        │  │  ├─ Arctic
│  │        │  │  │  └─ Longyearbyen
│  │        │  │  ├─ Asia
│  │        │  │  │  ├─ Aden
│  │        │  │  │  ├─ Almaty
│  │        │  │  │  ├─ Amman
│  │        │  │  │  ├─ Anadyr
│  │        │  │  │  ├─ Aqtau
│  │        │  │  │  ├─ Aqtobe
│  │        │  │  │  ├─ Ashgabat
│  │        │  │  │  ├─ Ashkhabad
│  │        │  │  │  ├─ Atyrau
│  │        │  │  │  ├─ Baghdad
│  │        │  │  │  ├─ Bahrain
│  │        │  │  │  ├─ Baku
│  │        │  │  │  ├─ Bangkok
│  │        │  │  │  ├─ Barnaul
│  │        │  │  │  ├─ Beirut
│  │        │  │  │  ├─ Bishkek
│  │        │  │  │  ├─ Brunei
│  │        │  │  │  ├─ Calcutta
│  │        │  │  │  ├─ Chita
│  │        │  │  │  ├─ Choibalsan
│  │        │  │  │  ├─ Chongqing
│  │        │  │  │  ├─ Chungking
│  │        │  │  │  ├─ Colombo
│  │        │  │  │  ├─ Dacca
│  │        │  │  │  ├─ Damascus
│  │        │  │  │  ├─ Dhaka
│  │        │  │  │  ├─ Dili
│  │        │  │  │  ├─ Dubai
│  │        │  │  │  ├─ Dushanbe
│  │        │  │  │  ├─ Famagusta
│  │        │  │  │  ├─ Gaza
│  │        │  │  │  ├─ Harbin
│  │        │  │  │  ├─ Hebron
│  │        │  │  │  ├─ Hong_Kong
│  │        │  │  │  ├─ Hovd
│  │        │  │  │  ├─ Ho_Chi_Minh
│  │        │  │  │  ├─ Irkutsk
│  │        │  │  │  ├─ Istanbul
│  │        │  │  │  ├─ Jakarta
│  │        │  │  │  ├─ Jayapura
│  │        │  │  │  ├─ Jerusalem
│  │        │  │  │  ├─ Kabul
│  │        │  │  │  ├─ Kamchatka
│  │        │  │  │  ├─ Karachi
│  │        │  │  │  ├─ Kashgar
│  │        │  │  │  ├─ Kathmandu
│  │        │  │  │  ├─ Katmandu
│  │        │  │  │  ├─ Khandyga
│  │        │  │  │  ├─ Kolkata
│  │        │  │  │  ├─ Krasnoyarsk
│  │        │  │  │  ├─ Kuala_Lumpur
│  │        │  │  │  ├─ Kuching
│  │        │  │  │  ├─ Kuwait
│  │        │  │  │  ├─ Macao
│  │        │  │  │  ├─ Macau
│  │        │  │  │  ├─ Magadan
│  │        │  │  │  ├─ Makassar
│  │        │  │  │  ├─ Manila
│  │        │  │  │  ├─ Muscat
│  │        │  │  │  ├─ Nicosia
│  │        │  │  │  ├─ Novokuznetsk
│  │        │  │  │  ├─ Novosibirsk
│  │        │  │  │  ├─ Omsk
│  │        │  │  │  ├─ Oral
│  │        │  │  │  ├─ Phnom_Penh
│  │        │  │  │  ├─ Pontianak
│  │        │  │  │  ├─ Pyongyang
│  │        │  │  │  ├─ Qatar
│  │        │  │  │  ├─ Qostanay
│  │        │  │  │  ├─ Qyzylorda
│  │        │  │  │  ├─ Rangoon
│  │        │  │  │  ├─ Riyadh
│  │        │  │  │  ├─ Saigon
│  │        │  │  │  ├─ Sakhalin
│  │        │  │  │  ├─ Samarkand
│  │        │  │  │  ├─ Seoul
│  │        │  │  │  ├─ Shanghai
│  │        │  │  │  ├─ Singapore
│  │        │  │  │  ├─ Srednekolymsk
│  │        │  │  │  ├─ Taipei
│  │        │  │  │  ├─ Tashkent
│  │        │  │  │  ├─ Tbilisi
│  │        │  │  │  ├─ Tehran
│  │        │  │  │  ├─ Tel_Aviv
│  │        │  │  │  ├─ Thimbu
│  │        │  │  │  ├─ Thimphu
│  │        │  │  │  ├─ Tokyo
│  │        │  │  │  ├─ Tomsk
│  │        │  │  │  ├─ Ujung_Pandang
│  │        │  │  │  ├─ Ulaanbaatar
│  │        │  │  │  ├─ Ulan_Bator
│  │        │  │  │  ├─ Urumqi
│  │        │  │  │  ├─ Ust-Nera
│  │        │  │  │  ├─ Vientiane
│  │        │  │  │  ├─ Vladivostok
│  │        │  │  │  ├─ Yakutsk
│  │        │  │  │  ├─ Yangon
│  │        │  │  │  ├─ Yekaterinburg
│  │        │  │  │  └─ Yerevan
│  │        │  │  ├─ Atlantic
│  │        │  │  │  ├─ Azores
│  │        │  │  │  ├─ Bermuda
│  │        │  │  │  ├─ Canary
│  │        │  │  │  ├─ Cape_Verde
│  │        │  │  │  ├─ Faeroe
│  │        │  │  │  ├─ Faroe
│  │        │  │  │  ├─ Jan_Mayen
│  │        │  │  │  ├─ Madeira
│  │        │  │  │  ├─ Reykjavik
│  │        │  │  │  ├─ South_Georgia
│  │        │  │  │  ├─ Stanley
│  │        │  │  │  └─ St_Helena
│  │        │  │  ├─ Australia
│  │        │  │  │  ├─ ACT
│  │        │  │  │  ├─ Adelaide
│  │        │  │  │  ├─ Brisbane
│  │        │  │  │  ├─ Broken_Hill
│  │        │  │  │  ├─ Canberra
│  │        │  │  │  ├─ Currie
│  │        │  │  │  ├─ Darwin
│  │        │  │  │  ├─ Eucla
│  │        │  │  │  ├─ Hobart
│  │        │  │  │  ├─ LHI
│  │        │  │  │  ├─ Lindeman
│  │        │  │  │  ├─ Lord_Howe
│  │        │  │  │  ├─ Melbourne
│  │        │  │  │  ├─ North
│  │        │  │  │  ├─ NSW
│  │        │  │  │  ├─ Perth
│  │        │  │  │  ├─ Queensland
│  │        │  │  │  ├─ South
│  │        │  │  │  ├─ Sydney
│  │        │  │  │  ├─ Tasmania
│  │        │  │  │  ├─ Victoria
│  │        │  │  │  ├─ West
│  │        │  │  │  └─ Yancowinna
│  │        │  │  ├─ Brazil
│  │        │  │  │  ├─ Acre
│  │        │  │  │  ├─ DeNoronha
│  │        │  │  │  ├─ East
│  │        │  │  │  └─ West
│  │        │  │  ├─ Canada
│  │        │  │  │  ├─ Atlantic
│  │        │  │  │  ├─ Central
│  │        │  │  │  ├─ Eastern
│  │        │  │  │  ├─ Mountain
│  │        │  │  │  ├─ Newfoundland
│  │        │  │  │  ├─ Pacific
│  │        │  │  │  ├─ Saskatchewan
│  │        │  │  │  └─ Yukon
│  │        │  │  ├─ CET
│  │        │  │  ├─ Chile
│  │        │  │  │  ├─ Continental
│  │        │  │  │  └─ EasterIsland
│  │        │  │  ├─ CST6CDT
│  │        │  │  ├─ Cuba
│  │        │  │  ├─ EET
│  │        │  │  ├─ Egypt
│  │        │  │  ├─ Eire
│  │        │  │  ├─ EST
│  │        │  │  ├─ EST5EDT
│  │        │  │  ├─ Etc
│  │        │  │  │  ├─ GMT
│  │        │  │  │  ├─ GMT+0
│  │        │  │  │  ├─ GMT+1
│  │        │  │  │  ├─ GMT+10
│  │        │  │  │  ├─ GMT+11
│  │        │  │  │  ├─ GMT+12
│  │        │  │  │  ├─ GMT+2
│  │        │  │  │  ├─ GMT+3
│  │        │  │  │  ├─ GMT+4
│  │        │  │  │  ├─ GMT+5
│  │        │  │  │  ├─ GMT+6
│  │        │  │  │  ├─ GMT+7
│  │        │  │  │  ├─ GMT+8
│  │        │  │  │  ├─ GMT+9
│  │        │  │  │  ├─ GMT-0
│  │        │  │  │  ├─ GMT-1
│  │        │  │  │  ├─ GMT-10
│  │        │  │  │  ├─ GMT-11
│  │        │  │  │  ├─ GMT-12
│  │        │  │  │  ├─ GMT-13
│  │        │  │  │  ├─ GMT-14
│  │        │  │  │  ├─ GMT-2
│  │        │  │  │  ├─ GMT-3
│  │        │  │  │  ├─ GMT-4
│  │        │  │  │  ├─ GMT-5
│  │        │  │  │  ├─ GMT-6
│  │        │  │  │  ├─ GMT-7
│  │        │  │  │  ├─ GMT-8
│  │        │  │  │  ├─ GMT-9
│  │        │  │  │  ├─ GMT0
│  │        │  │  │  ├─ Greenwich
│  │        │  │  │  ├─ UCT
│  │        │  │  │  ├─ Universal
│  │        │  │  │  ├─ UTC
│  │        │  │  │  └─ Zulu
│  │        │  │  ├─ Europe
│  │        │  │  │  ├─ Amsterdam
│  │        │  │  │  ├─ Andorra
│  │        │  │  │  ├─ Astrakhan
│  │        │  │  │  ├─ Athens
│  │        │  │  │  ├─ Belfast
│  │        │  │  │  ├─ Belgrade
│  │        │  │  │  ├─ Berlin
│  │        │  │  │  ├─ Bratislava
│  │        │  │  │  ├─ Brussels
│  │        │  │  │  ├─ Bucharest
│  │        │  │  │  ├─ Budapest
│  │        │  │  │  ├─ Busingen
│  │        │  │  │  ├─ Chisinau
│  │        │  │  │  ├─ Copenhagen
│  │        │  │  │  ├─ Dublin
│  │        │  │  │  ├─ Gibraltar
│  │        │  │  │  ├─ Guernsey
│  │        │  │  │  ├─ Helsinki
│  │        │  │  │  ├─ Isle_of_Man
│  │        │  │  │  ├─ Istanbul
│  │        │  │  │  ├─ Jersey
│  │        │  │  │  ├─ Kaliningrad
│  │        │  │  │  ├─ Kiev
│  │        │  │  │  ├─ Kirov
│  │        │  │  │  ├─ Kyiv
│  │        │  │  │  ├─ Lisbon
│  │        │  │  │  ├─ Ljubljana
│  │        │  │  │  ├─ London
│  │        │  │  │  ├─ Luxembourg
│  │        │  │  │  ├─ Madrid
│  │        │  │  │  ├─ Malta
│  │        │  │  │  ├─ Mariehamn
│  │        │  │  │  ├─ Minsk
│  │        │  │  │  ├─ Monaco
│  │        │  │  │  ├─ Moscow
│  │        │  │  │  ├─ Nicosia
│  │        │  │  │  ├─ Oslo
│  │        │  │  │  ├─ Paris
│  │        │  │  │  ├─ Podgorica
│  │        │  │  │  ├─ Prague
│  │        │  │  │  ├─ Riga
│  │        │  │  │  ├─ Rome
│  │        │  │  │  ├─ Samara
│  │        │  │  │  ├─ San_Marino
│  │        │  │  │  ├─ Sarajevo
│  │        │  │  │  ├─ Saratov
│  │        │  │  │  ├─ Simferopol
│  │        │  │  │  ├─ Skopje
│  │        │  │  │  ├─ Sofia
│  │        │  │  │  ├─ Stockholm
│  │        │  │  │  ├─ Tallinn
│  │        │  │  │  ├─ Tirane
│  │        │  │  │  ├─ Tiraspol
│  │        │  │  │  ├─ Ulyanovsk
│  │        │  │  │  ├─ Uzhgorod
│  │        │  │  │  ├─ Vaduz
│  │        │  │  │  ├─ Vatican
│  │        │  │  │  ├─ Vienna
│  │        │  │  │  ├─ Vilnius
│  │        │  │  │  ├─ Volgograd
│  │        │  │  │  ├─ Warsaw
│  │        │  │  │  ├─ Zagreb
│  │        │  │  │  ├─ Zaporozhye
│  │        │  │  │  └─ Zurich
│  │        │  │  ├─ Factory
│  │        │  │  ├─ GB
│  │        │  │  ├─ GB-Eire
│  │        │  │  ├─ GMT
│  │        │  │  ├─ GMT+0
│  │        │  │  ├─ GMT-0
│  │        │  │  ├─ GMT0
│  │        │  │  ├─ Greenwich
│  │        │  │  ├─ Hongkong
│  │        │  │  ├─ HST
│  │        │  │  ├─ Iceland
│  │        │  │  ├─ Indian
│  │        │  │  │  ├─ Antananarivo
│  │        │  │  │  ├─ Chagos
│  │        │  │  │  ├─ Christmas
│  │        │  │  │  ├─ Cocos
│  │        │  │  │  ├─ Comoro
│  │        │  │  │  ├─ Kerguelen
│  │        │  │  │  ├─ Mahe
│  │        │  │  │  ├─ Maldives
│  │        │  │  │  ├─ Mauritius
│  │        │  │  │  ├─ Mayotte
│  │        │  │  │  └─ Reunion
│  │        │  │  ├─ Iran
│  │        │  │  ├─ iso3166.tab
│  │        │  │  ├─ Israel
│  │        │  │  ├─ Jamaica
│  │        │  │  ├─ Japan
│  │        │  │  ├─ Kwajalein
│  │        │  │  ├─ leapseconds
│  │        │  │  ├─ Libya
│  │        │  │  ├─ MET
│  │        │  │  ├─ Mexico
│  │        │  │  │  ├─ BajaNorte
│  │        │  │  │  ├─ BajaSur
│  │        │  │  │  └─ General
│  │        │  │  ├─ MST
│  │        │  │  ├─ MST7MDT
│  │        │  │  ├─ Navajo
│  │        │  │  ├─ NZ
│  │        │  │  ├─ NZ-CHAT
│  │        │  │  ├─ Pacific
│  │        │  │  │  ├─ Apia
│  │        │  │  │  ├─ Auckland
│  │        │  │  │  ├─ Bougainville
│  │        │  │  │  ├─ Chatham
│  │        │  │  │  ├─ Chuuk
│  │        │  │  │  ├─ Easter
│  │        │  │  │  ├─ Efate
│  │        │  │  │  ├─ Enderbury
│  │        │  │  │  ├─ Fakaofo
│  │        │  │  │  ├─ Fiji
│  │        │  │  │  ├─ Funafuti
│  │        │  │  │  ├─ Galapagos
│  │        │  │  │  ├─ Gambier
│  │        │  │  │  ├─ Guadalcanal
│  │        │  │  │  ├─ Guam
│  │        │  │  │  ├─ Honolulu
│  │        │  │  │  ├─ Johnston
│  │        │  │  │  ├─ Kanton
│  │        │  │  │  ├─ Kiritimati
│  │        │  │  │  ├─ Kosrae
│  │        │  │  │  ├─ Kwajalein
│  │        │  │  │  ├─ Majuro
│  │        │  │  │  ├─ Marquesas
│  │        │  │  │  ├─ Midway
│  │        │  │  │  ├─ Nauru
│  │        │  │  │  ├─ Niue
│  │        │  │  │  ├─ Norfolk
│  │        │  │  │  ├─ Noumea
│  │        │  │  │  ├─ Pago_Pago
│  │        │  │  │  ├─ Palau
│  │        │  │  │  ├─ Pitcairn
│  │        │  │  │  ├─ Pohnpei
│  │        │  │  │  ├─ Ponape
│  │        │  │  │  ├─ Port_Moresby
│  │        │  │  │  ├─ Rarotonga
│  │        │  │  │  ├─ Saipan
│  │        │  │  │  ├─ Samoa
│  │        │  │  │  ├─ Tahiti
│  │        │  │  │  ├─ Tarawa
│  │        │  │  │  ├─ Tongatapu
│  │        │  │  │  ├─ Truk
│  │        │  │  │  ├─ Wake
│  │        │  │  │  ├─ Wallis
│  │        │  │  │  └─ Yap
│  │        │  │  ├─ Poland
│  │        │  │  ├─ Portugal
│  │        │  │  ├─ PRC
│  │        │  │  ├─ PST8PDT
│  │        │  │  ├─ ROC
│  │        │  │  ├─ ROK
│  │        │  │  ├─ Singapore
│  │        │  │  ├─ Turkey
│  │        │  │  ├─ tzdata.zi
│  │        │  │  ├─ UCT
│  │        │  │  ├─ Universal
│  │        │  │  ├─ US
│  │        │  │  │  ├─ Alaska
│  │        │  │  │  ├─ Aleutian
│  │        │  │  │  ├─ Arizona
│  │        │  │  │  ├─ Central
│  │        │  │  │  ├─ East-Indiana
│  │        │  │  │  ├─ Eastern
│  │        │  │  │  ├─ Hawaii
│  │        │  │  │  ├─ Indiana-Starke
│  │        │  │  │  ├─ Michigan
│  │        │  │  │  ├─ Mountain
│  │        │  │  │  ├─ Pacific
│  │        │  │  │  └─ Samoa
│  │        │  │  ├─ UTC
│  │        │  │  ├─ W-SU
│  │        │  │  ├─ WET
│  │        │  │  ├─ zone.tab
│  │        │  │  ├─ zone1970.tab
│  │        │  │  ├─ zonenow.tab
│  │        │  │  └─ Zulu
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     ├─ exceptions.cpython-312.pyc
│  │        │     ├─ lazy.cpython-312.pyc
│  │        │     ├─ reference.cpython-312.pyc
│  │        │     ├─ tzfile.cpython-312.pyc
│  │        │     ├─ tzinfo.cpython-312.pyc
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ pytz-2025.2.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE.txt
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ top_level.txt
│  │        │  ├─ WHEEL
│  │        │  └─ zip-safe
│  │        ├─ PyYAML-6.0.2.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ top_level.txt
│  │        │  └─ WHEEL
│  │        ├─ rich
│  │        │  ├─ abc.py
│  │        │  ├─ align.py
│  │        │  ├─ ansi.py
│  │        │  ├─ bar.py
│  │        │  ├─ box.py
│  │        │  ├─ cells.py
│  │        │  ├─ color.py
│  │        │  ├─ color_triplet.py
│  │        │  ├─ columns.py
│  │        │  ├─ console.py
│  │        │  ├─ constrain.py
│  │        │  ├─ containers.py
│  │        │  ├─ control.py
│  │        │  ├─ default_styles.py
│  │        │  ├─ diagnose.py
│  │        │  ├─ emoji.py
│  │        │  ├─ errors.py
│  │        │  ├─ filesize.py
│  │        │  ├─ file_proxy.py
│  │        │  ├─ highlighter.py
│  │        │  ├─ json.py
│  │        │  ├─ jupyter.py
│  │        │  ├─ layout.py
│  │        │  ├─ live.py
│  │        │  ├─ live_render.py
│  │        │  ├─ logging.py
│  │        │  ├─ markdown.py
│  │        │  ├─ markup.py
│  │        │  ├─ measure.py
│  │        │  ├─ padding.py
│  │        │  ├─ pager.py
│  │        │  ├─ palette.py
│  │        │  ├─ panel.py
│  │        │  ├─ pretty.py
│  │        │  ├─ progress.py
│  │        │  ├─ progress_bar.py
│  │        │  ├─ prompt.py
│  │        │  ├─ protocol.py
│  │        │  ├─ py.typed
│  │        │  ├─ region.py
│  │        │  ├─ repr.py
│  │        │  ├─ rule.py
│  │        │  ├─ scope.py
│  │        │  ├─ screen.py
│  │        │  ├─ segment.py
│  │        │  ├─ spinner.py
│  │        │  ├─ status.py
│  │        │  ├─ style.py
│  │        │  ├─ styled.py
│  │        │  ├─ syntax.py
│  │        │  ├─ table.py
│  │        │  ├─ terminal_theme.py
│  │        │  ├─ text.py
│  │        │  ├─ theme.py
│  │        │  ├─ themes.py
│  │        │  ├─ traceback.py
│  │        │  ├─ tree.py
│  │        │  ├─ _cell_widths.py
│  │        │  ├─ _emoji_codes.py
│  │        │  ├─ _emoji_replace.py
│  │        │  ├─ _export_format.py
│  │        │  ├─ _extension.py
│  │        │  ├─ _fileno.py
│  │        │  ├─ _inspect.py
│  │        │  ├─ _log_render.py
│  │        │  ├─ _loop.py
│  │        │  ├─ _null_file.py
│  │        │  ├─ _palettes.py
│  │        │  ├─ _pick.py
│  │        │  ├─ _ratio.py
│  │        │  ├─ _spinners.py
│  │        │  ├─ _stack.py
│  │        │  ├─ _timer.py
│  │        │  ├─ _win32_console.py
│  │        │  ├─ _windows.py
│  │        │  ├─ _windows_renderer.py
│  │        │  ├─ _wrap.py
│  │        │  ├─ __init__.py
│  │        │  ├─ __main__.py
│  │        │  └─ __pycache__
│  │        │     ├─ abc.cpython-312.pyc
│  │        │     ├─ align.cpython-312.pyc
│  │        │     ├─ ansi.cpython-312.pyc
│  │        │     ├─ bar.cpython-312.pyc
│  │        │     ├─ box.cpython-312.pyc
│  │        │     ├─ cells.cpython-312.pyc
│  │        │     ├─ color.cpython-312.pyc
│  │        │     ├─ color_triplet.cpython-312.pyc
│  │        │     ├─ columns.cpython-312.pyc
│  │        │     ├─ console.cpython-312.pyc
│  │        │     ├─ constrain.cpython-312.pyc
│  │        │     ├─ containers.cpython-312.pyc
│  │        │     ├─ control.cpython-312.pyc
│  │        │     ├─ default_styles.cpython-312.pyc
│  │        │     ├─ diagnose.cpython-312.pyc
│  │        │     ├─ emoji.cpython-312.pyc
│  │        │     ├─ errors.cpython-312.pyc
│  │        │     ├─ filesize.cpython-312.pyc
│  │        │     ├─ file_proxy.cpython-312.pyc
│  │        │     ├─ highlighter.cpython-312.pyc
│  │        │     ├─ json.cpython-312.pyc
│  │        │     ├─ jupyter.cpython-312.pyc
│  │        │     ├─ layout.cpython-312.pyc
│  │        │     ├─ live.cpython-312.pyc
│  │        │     ├─ live_render.cpython-312.pyc
│  │        │     ├─ logging.cpython-312.pyc
│  │        │     ├─ markdown.cpython-312.pyc
│  │        │     ├─ markup.cpython-312.pyc
│  │        │     ├─ measure.cpython-312.pyc
│  │        │     ├─ padding.cpython-312.pyc
│  │        │     ├─ pager.cpython-312.pyc
│  │        │     ├─ palette.cpython-312.pyc
│  │        │     ├─ panel.cpython-312.pyc
│  │        │     ├─ pretty.cpython-312.pyc
│  │        │     ├─ progress.cpython-312.pyc
│  │        │     ├─ progress_bar.cpython-312.pyc
│  │        │     ├─ prompt.cpython-312.pyc
│  │        │     ├─ protocol.cpython-312.pyc
│  │        │     ├─ region.cpython-312.pyc
│  │        │     ├─ repr.cpython-312.pyc
│  │        │     ├─ rule.cpython-312.pyc
│  │        │     ├─ scope.cpython-312.pyc
│  │        │     ├─ screen.cpython-312.pyc
│  │        │     ├─ segment.cpython-312.pyc
│  │        │     ├─ spinner.cpython-312.pyc
│  │        │     ├─ status.cpython-312.pyc
│  │        │     ├─ style.cpython-312.pyc
│  │        │     ├─ styled.cpython-312.pyc
│  │        │     ├─ syntax.cpython-312.pyc
│  │        │     ├─ table.cpython-312.pyc
│  │        │     ├─ terminal_theme.cpython-312.pyc
│  │        │     ├─ text.cpython-312.pyc
│  │        │     ├─ theme.cpython-312.pyc
│  │        │     ├─ themes.cpython-312.pyc
│  │        │     ├─ traceback.cpython-312.pyc
│  │        │     ├─ tree.cpython-312.pyc
│  │        │     ├─ _cell_widths.cpython-312.pyc
│  │        │     ├─ _emoji_codes.cpython-312.pyc
│  │        │     ├─ _emoji_replace.cpython-312.pyc
│  │        │     ├─ _export_format.cpython-312.pyc
│  │        │     ├─ _extension.cpython-312.pyc
│  │        │     ├─ _fileno.cpython-312.pyc
│  │        │     ├─ _inspect.cpython-312.pyc
│  │        │     ├─ _log_render.cpython-312.pyc
│  │        │     ├─ _loop.cpython-312.pyc
│  │        │     ├─ _null_file.cpython-312.pyc
│  │        │     ├─ _palettes.cpython-312.pyc
│  │        │     ├─ _pick.cpython-312.pyc
│  │        │     ├─ _ratio.cpython-312.pyc
│  │        │     ├─ _spinners.cpython-312.pyc
│  │        │     ├─ _stack.cpython-312.pyc
│  │        │     ├─ _timer.cpython-312.pyc
│  │        │     ├─ _win32_console.cpython-312.pyc
│  │        │     ├─ _windows.cpython-312.pyc
│  │        │     ├─ _windows_renderer.cpython-312.pyc
│  │        │     ├─ _wrap.cpython-312.pyc
│  │        │     ├─ __init__.cpython-312.pyc
│  │        │     └─ __main__.cpython-312.pyc
│  │        ├─ rich-14.0.0.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  └─ WHEEL
│  │        ├─ rich_toolkit
│  │        │  ├─ button.py
│  │        │  ├─ container.py
│  │        │  ├─ element.py
│  │        │  ├─ form.py
│  │        │  ├─ input.py
│  │        │  ├─ menu.py
│  │        │  ├─ progress.py
│  │        │  ├─ py.typed
│  │        │  ├─ spacer.py
│  │        │  ├─ styles
│  │        │  │  ├─ base.py
│  │        │  │  ├─ border.py
│  │        │  │  ├─ fancy.py
│  │        │  │  ├─ minimal.py
│  │        │  │  ├─ tagged.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ base.cpython-312.pyc
│  │        │  │     ├─ border.cpython-312.pyc
│  │        │  │     ├─ fancy.cpython-312.pyc
│  │        │  │     ├─ minimal.cpython-312.pyc
│  │        │  │     ├─ tagged.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ toolkit.py
│  │        │  ├─ utils
│  │        │  │  ├─ colors.py
│  │        │  │  ├─ map_range.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ colors.cpython-312.pyc
│  │        │  │     ├─ map_range.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ _input_handler.py
│  │        │  ├─ _rich_components.py
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     ├─ button.cpython-312.pyc
│  │        │     ├─ container.cpython-312.pyc
│  │        │     ├─ element.cpython-312.pyc
│  │        │     ├─ form.cpython-312.pyc
│  │        │     ├─ input.cpython-312.pyc
│  │        │     ├─ menu.cpython-312.pyc
│  │        │     ├─ progress.cpython-312.pyc
│  │        │     ├─ spacer.cpython-312.pyc
│  │        │     ├─ toolkit.cpython-312.pyc
│  │        │     ├─ _input_handler.cpython-312.pyc
│  │        │     ├─ _rich_components.cpython-312.pyc
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ rich_toolkit-0.14.7.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ licenses
│  │        │  │  └─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  └─ WHEEL
│  │        ├─ scikit_learn-1.7.0.dist-info
│  │        │  ├─ COPYING
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ REQUESTED
│  │        │  └─ WHEEL
│  │        ├─ scipy
│  │        │  ├─ .dylibs
│  │        │  │  ├─ libgcc_s.1.1.dylib
│  │        │  │  ├─ libgfortran.5.dylib
│  │        │  │  └─ libquadmath.0.dylib
│  │        │  ├─ cluster
│  │        │  │  ├─ hierarchy.py
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ hierarchy_test_data.py
│  │        │  │  │  ├─ test_disjoint_set.py
│  │        │  │  │  ├─ test_hierarchy.py
│  │        │  │  │  ├─ test_vq.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ hierarchy_test_data.cpython-312.pyc
│  │        │  │  │     ├─ test_disjoint_set.cpython-312.pyc
│  │        │  │  │     ├─ test_hierarchy.cpython-312.pyc
│  │        │  │  │     ├─ test_vq.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ vq.py
│  │        │  │  ├─ _hierarchy.cpython-312-darwin.so
│  │        │  │  ├─ _optimal_leaf_ordering.cpython-312-darwin.so
│  │        │  │  ├─ _vq.cpython-312-darwin.so
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ hierarchy.cpython-312.pyc
│  │        │  │     ├─ vq.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ conftest.py
│  │        │  ├─ constants
│  │        │  │  ├─ codata.py
│  │        │  │  ├─ constants.py
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ test_codata.py
│  │        │  │  │  ├─ test_constants.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_codata.cpython-312.pyc
│  │        │  │  │     ├─ test_constants.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _codata.py
│  │        │  │  ├─ _constants.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ codata.cpython-312.pyc
│  │        │  │     ├─ constants.cpython-312.pyc
│  │        │  │     ├─ _codata.cpython-312.pyc
│  │        │  │     ├─ _constants.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ datasets
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ test_data.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_data.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _download_all.py
│  │        │  │  ├─ _fetchers.py
│  │        │  │  ├─ _registry.py
│  │        │  │  ├─ _utils.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ _download_all.cpython-312.pyc
│  │        │  │     ├─ _fetchers.cpython-312.pyc
│  │        │  │     ├─ _registry.cpython-312.pyc
│  │        │  │     ├─ _utils.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ differentiate
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ test_differentiate.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_differentiate.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _differentiate.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ _differentiate.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ fft
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ mock_backend.py
│  │        │  │  │  ├─ test_backend.py
│  │        │  │  │  ├─ test_basic.py
│  │        │  │  │  ├─ test_fftlog.py
│  │        │  │  │  ├─ test_helper.py
│  │        │  │  │  ├─ test_multithreading.py
│  │        │  │  │  ├─ test_real_transforms.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ mock_backend.cpython-312.pyc
│  │        │  │  │     ├─ test_backend.cpython-312.pyc
│  │        │  │  │     ├─ test_basic.cpython-312.pyc
│  │        │  │  │     ├─ test_fftlog.cpython-312.pyc
│  │        │  │  │     ├─ test_helper.cpython-312.pyc
│  │        │  │  │     ├─ test_multithreading.cpython-312.pyc
│  │        │  │  │     ├─ test_real_transforms.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _backend.py
│  │        │  │  ├─ _basic.py
│  │        │  │  ├─ _basic_backend.py
│  │        │  │  ├─ _debug_backends.py
│  │        │  │  ├─ _fftlog.py
│  │        │  │  ├─ _fftlog_backend.py
│  │        │  │  ├─ _helper.py
│  │        │  │  ├─ _pocketfft
│  │        │  │  │  ├─ basic.py
│  │        │  │  │  ├─ helper.py
│  │        │  │  │  ├─ LICENSE.md
│  │        │  │  │  ├─ pypocketfft.cpython-312-darwin.so
│  │        │  │  │  ├─ realtransforms.py
│  │        │  │  │  ├─ tests
│  │        │  │  │  │  ├─ test_basic.py
│  │        │  │  │  │  ├─ test_real_transforms.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_basic.cpython-312.pyc
│  │        │  │  │  │     ├─ test_real_transforms.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ basic.cpython-312.pyc
│  │        │  │  │     ├─ helper.cpython-312.pyc
│  │        │  │  │     ├─ realtransforms.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _realtransforms.py
│  │        │  │  ├─ _realtransforms_backend.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ _backend.cpython-312.pyc
│  │        │  │     ├─ _basic.cpython-312.pyc
│  │        │  │     ├─ _basic_backend.cpython-312.pyc
│  │        │  │     ├─ _debug_backends.cpython-312.pyc
│  │        │  │     ├─ _fftlog.cpython-312.pyc
│  │        │  │     ├─ _fftlog_backend.cpython-312.pyc
│  │        │  │     ├─ _helper.cpython-312.pyc
│  │        │  │     ├─ _realtransforms.cpython-312.pyc
│  │        │  │     ├─ _realtransforms_backend.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ fftpack
│  │        │  │  ├─ basic.py
│  │        │  │  ├─ convolve.cpython-312-darwin.so
│  │        │  │  ├─ helper.py
│  │        │  │  ├─ pseudo_diffs.py
│  │        │  │  ├─ realtransforms.py
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ fftw_double_ref.npz
│  │        │  │  │  ├─ fftw_longdouble_ref.npz
│  │        │  │  │  ├─ fftw_single_ref.npz
│  │        │  │  │  ├─ test.npz
│  │        │  │  │  ├─ test_basic.py
│  │        │  │  │  ├─ test_helper.py
│  │        │  │  │  ├─ test_import.py
│  │        │  │  │  ├─ test_pseudo_diffs.py
│  │        │  │  │  ├─ test_real_transforms.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_basic.cpython-312.pyc
│  │        │  │  │     ├─ test_helper.cpython-312.pyc
│  │        │  │  │     ├─ test_import.cpython-312.pyc
│  │        │  │  │     ├─ test_pseudo_diffs.cpython-312.pyc
│  │        │  │  │     ├─ test_real_transforms.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _basic.py
│  │        │  │  ├─ _helper.py
│  │        │  │  ├─ _pseudo_diffs.py
│  │        │  │  ├─ _realtransforms.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ basic.cpython-312.pyc
│  │        │  │     ├─ helper.cpython-312.pyc
│  │        │  │     ├─ pseudo_diffs.cpython-312.pyc
│  │        │  │     ├─ realtransforms.cpython-312.pyc
│  │        │  │     ├─ _basic.cpython-312.pyc
│  │        │  │     ├─ _helper.cpython-312.pyc
│  │        │  │     ├─ _pseudo_diffs.cpython-312.pyc
│  │        │  │     ├─ _realtransforms.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ integrate
│  │        │  │  ├─ dop.py
│  │        │  │  ├─ lsoda.py
│  │        │  │  ├─ odepack.py
│  │        │  │  ├─ quadpack.py
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ test_banded_ode_solvers.py
│  │        │  │  │  ├─ test_bvp.py
│  │        │  │  │  ├─ test_cubature.py
│  │        │  │  │  ├─ test_integrate.py
│  │        │  │  │  ├─ test_odeint_jac.py
│  │        │  │  │  ├─ test_quadpack.py
│  │        │  │  │  ├─ test_quadrature.py
│  │        │  │  │  ├─ test_tanhsinh.py
│  │        │  │  │  ├─ test__quad_vec.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_banded_ode_solvers.cpython-312.pyc
│  │        │  │  │     ├─ test_bvp.cpython-312.pyc
│  │        │  │  │     ├─ test_cubature.cpython-312.pyc
│  │        │  │  │     ├─ test_integrate.cpython-312.pyc
│  │        │  │  │     ├─ test_odeint_jac.cpython-312.pyc
│  │        │  │  │     ├─ test_quadpack.cpython-312.pyc
│  │        │  │  │     ├─ test_quadrature.cpython-312.pyc
│  │        │  │  │     ├─ test_tanhsinh.cpython-312.pyc
│  │        │  │  │     ├─ test__quad_vec.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ vode.py
│  │        │  │  ├─ _bvp.py
│  │        │  │  ├─ _cubature.py
│  │        │  │  ├─ _dop.cpython-312-darwin.so
│  │        │  │  ├─ _ivp
│  │        │  │  │  ├─ base.py
│  │        │  │  │  ├─ bdf.py
│  │        │  │  │  ├─ common.py
│  │        │  │  │  ├─ dop853_coefficients.py
│  │        │  │  │  ├─ ivp.py
│  │        │  │  │  ├─ lsoda.py
│  │        │  │  │  ├─ radau.py
│  │        │  │  │  ├─ rk.py
│  │        │  │  │  ├─ tests
│  │        │  │  │  │  ├─ test_ivp.py
│  │        │  │  │  │  ├─ test_rk.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_ivp.cpython-312.pyc
│  │        │  │  │  │     ├─ test_rk.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ base.cpython-312.pyc
│  │        │  │  │     ├─ bdf.cpython-312.pyc
│  │        │  │  │     ├─ common.cpython-312.pyc
│  │        │  │  │     ├─ dop853_coefficients.cpython-312.pyc
│  │        │  │  │     ├─ ivp.cpython-312.pyc
│  │        │  │  │     ├─ lsoda.cpython-312.pyc
│  │        │  │  │     ├─ radau.cpython-312.pyc
│  │        │  │  │     ├─ rk.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _lebedev.py
│  │        │  │  ├─ _lsoda.cpython-312-darwin.so
│  │        │  │  ├─ _ode.py
│  │        │  │  ├─ _odepack.cpython-312-darwin.so
│  │        │  │  ├─ _odepack_py.py
│  │        │  │  ├─ _quadpack.cpython-312-darwin.so
│  │        │  │  ├─ _quadpack_py.py
│  │        │  │  ├─ _quadrature.py
│  │        │  │  ├─ _quad_vec.py
│  │        │  │  ├─ _rules
│  │        │  │  │  ├─ _base.py
│  │        │  │  │  ├─ _gauss_kronrod.py
│  │        │  │  │  ├─ _gauss_legendre.py
│  │        │  │  │  ├─ _genz_malik.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ _base.cpython-312.pyc
│  │        │  │  │     ├─ _gauss_kronrod.cpython-312.pyc
│  │        │  │  │     ├─ _gauss_legendre.cpython-312.pyc
│  │        │  │  │     ├─ _genz_malik.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _tanhsinh.py
│  │        │  │  ├─ _test_multivariate.cpython-312-darwin.so
│  │        │  │  ├─ _test_odeint_banded.cpython-312-darwin.so
│  │        │  │  ├─ _vode.cpython-312-darwin.so
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ dop.cpython-312.pyc
│  │        │  │     ├─ lsoda.cpython-312.pyc
│  │        │  │     ├─ odepack.cpython-312.pyc
│  │        │  │     ├─ quadpack.cpython-312.pyc
│  │        │  │     ├─ vode.cpython-312.pyc
│  │        │  │     ├─ _bvp.cpython-312.pyc
│  │        │  │     ├─ _cubature.cpython-312.pyc
│  │        │  │     ├─ _lebedev.cpython-312.pyc
│  │        │  │     ├─ _ode.cpython-312.pyc
│  │        │  │     ├─ _odepack_py.cpython-312.pyc
│  │        │  │     ├─ _quadpack_py.cpython-312.pyc
│  │        │  │     ├─ _quadrature.cpython-312.pyc
│  │        │  │     ├─ _quad_vec.cpython-312.pyc
│  │        │  │     ├─ _tanhsinh.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ interpolate
│  │        │  │  ├─ dfitpack.py
│  │        │  │  ├─ fitpack.py
│  │        │  │  ├─ fitpack2.py
│  │        │  │  ├─ interpnd.py
│  │        │  │  ├─ interpolate.py
│  │        │  │  ├─ ndgriddata.py
│  │        │  │  ├─ polyint.py
│  │        │  │  ├─ rbf.py
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ data
│  │        │  │  │  │  ├─ bug-1310.npz
│  │        │  │  │  │  ├─ estimate_gradients_hang.npy
│  │        │  │  │  │  └─ gcvspl.npz
│  │        │  │  │  ├─ test_bary_rational.py
│  │        │  │  │  ├─ test_bsplines.py
│  │        │  │  │  ├─ test_fitpack.py
│  │        │  │  │  ├─ test_fitpack2.py
│  │        │  │  │  ├─ test_gil.py
│  │        │  │  │  ├─ test_interpnd.py
│  │        │  │  │  ├─ test_interpolate.py
│  │        │  │  │  ├─ test_ndgriddata.py
│  │        │  │  │  ├─ test_pade.py
│  │        │  │  │  ├─ test_polyint.py
│  │        │  │  │  ├─ test_rbf.py
│  │        │  │  │  ├─ test_rbfinterp.py
│  │        │  │  │  ├─ test_rgi.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_bary_rational.cpython-312.pyc
│  │        │  │  │     ├─ test_bsplines.cpython-312.pyc
│  │        │  │  │     ├─ test_fitpack.cpython-312.pyc
│  │        │  │  │     ├─ test_fitpack2.cpython-312.pyc
│  │        │  │  │     ├─ test_gil.cpython-312.pyc
│  │        │  │  │     ├─ test_interpnd.cpython-312.pyc
│  │        │  │  │     ├─ test_interpolate.cpython-312.pyc
│  │        │  │  │     ├─ test_ndgriddata.cpython-312.pyc
│  │        │  │  │     ├─ test_pade.cpython-312.pyc
│  │        │  │  │     ├─ test_polyint.cpython-312.pyc
│  │        │  │  │     ├─ test_rbf.cpython-312.pyc
│  │        │  │  │     ├─ test_rbfinterp.cpython-312.pyc
│  │        │  │  │     ├─ test_rgi.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _bary_rational.py
│  │        │  │  ├─ _bspl.cpython-312-darwin.so
│  │        │  │  ├─ _bsplines.py
│  │        │  │  ├─ _cubic.py
│  │        │  │  ├─ _dfitpack.cpython-312-darwin.so
│  │        │  │  ├─ _dierckx.cpython-312-darwin.so
│  │        │  │  ├─ _fitpack.cpython-312-darwin.so
│  │        │  │  ├─ _fitpack2.py
│  │        │  │  ├─ _fitpack_impl.py
│  │        │  │  ├─ _fitpack_py.py
│  │        │  │  ├─ _fitpack_repro.py
│  │        │  │  ├─ _interpnd.cpython-312-darwin.so
│  │        │  │  ├─ _interpolate.py
│  │        │  │  ├─ _ndbspline.py
│  │        │  │  ├─ _ndgriddata.py
│  │        │  │  ├─ _pade.py
│  │        │  │  ├─ _polyint.py
│  │        │  │  ├─ _ppoly.cpython-312-darwin.so
│  │        │  │  ├─ _rbf.py
│  │        │  │  ├─ _rbfinterp.py
│  │        │  │  ├─ _rbfinterp_pythran.cpython-312-darwin.so
│  │        │  │  ├─ _rgi.py
│  │        │  │  ├─ _rgi_cython.cpython-312-darwin.so
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ dfitpack.cpython-312.pyc
│  │        │  │     ├─ fitpack.cpython-312.pyc
│  │        │  │     ├─ fitpack2.cpython-312.pyc
│  │        │  │     ├─ interpnd.cpython-312.pyc
│  │        │  │     ├─ interpolate.cpython-312.pyc
│  │        │  │     ├─ ndgriddata.cpython-312.pyc
│  │        │  │     ├─ polyint.cpython-312.pyc
│  │        │  │     ├─ rbf.cpython-312.pyc
│  │        │  │     ├─ _bary_rational.cpython-312.pyc
│  │        │  │     ├─ _bsplines.cpython-312.pyc
│  │        │  │     ├─ _cubic.cpython-312.pyc
│  │        │  │     ├─ _fitpack2.cpython-312.pyc
│  │        │  │     ├─ _fitpack_impl.cpython-312.pyc
│  │        │  │     ├─ _fitpack_py.cpython-312.pyc
│  │        │  │     ├─ _fitpack_repro.cpython-312.pyc
│  │        │  │     ├─ _interpolate.cpython-312.pyc
│  │        │  │     ├─ _ndbspline.cpython-312.pyc
│  │        │  │     ├─ _ndgriddata.cpython-312.pyc
│  │        │  │     ├─ _pade.cpython-312.pyc
│  │        │  │     ├─ _polyint.cpython-312.pyc
│  │        │  │     ├─ _rbf.cpython-312.pyc
│  │        │  │     ├─ _rbfinterp.cpython-312.pyc
│  │        │  │     ├─ _rgi.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ io
│  │        │  │  ├─ arff
│  │        │  │  │  ├─ arffread.py
│  │        │  │  │  ├─ tests
│  │        │  │  │  │  ├─ data
│  │        │  │  │  │  │  ├─ iris.arff
│  │        │  │  │  │  │  ├─ missing.arff
│  │        │  │  │  │  │  ├─ nodata.arff
│  │        │  │  │  │  │  ├─ quoted_nominal.arff
│  │        │  │  │  │  │  ├─ quoted_nominal_spaces.arff
│  │        │  │  │  │  │  ├─ test1.arff
│  │        │  │  │  │  │  ├─ test10.arff
│  │        │  │  │  │  │  ├─ test11.arff
│  │        │  │  │  │  │  ├─ test2.arff
│  │        │  │  │  │  │  ├─ test3.arff
│  │        │  │  │  │  │  ├─ test4.arff
│  │        │  │  │  │  │  ├─ test5.arff
│  │        │  │  │  │  │  ├─ test6.arff
│  │        │  │  │  │  │  ├─ test7.arff
│  │        │  │  │  │  │  ├─ test8.arff
│  │        │  │  │  │  │  └─ test9.arff
│  │        │  │  │  │  ├─ test_arffread.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_arffread.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ _arffread.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ arffread.cpython-312.pyc
│  │        │  │  │     ├─ _arffread.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ harwell_boeing.py
│  │        │  │  ├─ idl.py
│  │        │  │  ├─ matlab
│  │        │  │  │  ├─ byteordercodes.py
│  │        │  │  │  ├─ mio.py
│  │        │  │  │  ├─ mio4.py
│  │        │  │  │  ├─ mio5.py
│  │        │  │  │  ├─ mio5_params.py
│  │        │  │  │  ├─ mio5_utils.py
│  │        │  │  │  ├─ miobase.py
│  │        │  │  │  ├─ mio_utils.py
│  │        │  │  │  ├─ streams.py
│  │        │  │  │  ├─ tests
│  │        │  │  │  │  ├─ data
│  │        │  │  │  │  │  ├─ bad_miuint32.mat
│  │        │  │  │  │  │  ├─ bad_miutf8_array_name.mat
│  │        │  │  │  │  │  ├─ big_endian.mat
│  │        │  │  │  │  │  ├─ broken_utf8.mat
│  │        │  │  │  │  │  ├─ corrupted_zlib_checksum.mat
│  │        │  │  │  │  │  ├─ corrupted_zlib_data.mat
│  │        │  │  │  │  │  ├─ debigged_m4.mat
│  │        │  │  │  │  │  ├─ japanese_utf8.txt
│  │        │  │  │  │  │  ├─ little_endian.mat
│  │        │  │  │  │  │  ├─ logical_sparse.mat
│  │        │  │  │  │  │  ├─ malformed1.mat
│  │        │  │  │  │  │  ├─ miuint32_for_miint32.mat
│  │        │  │  │  │  │  ├─ miutf8_array_name.mat
│  │        │  │  │  │  │  ├─ nasty_duplicate_fieldnames.mat
│  │        │  │  │  │  │  ├─ one_by_zero_char.mat
│  │        │  │  │  │  │  ├─ parabola.mat
│  │        │  │  │  │  │  ├─ single_empty_string.mat
│  │        │  │  │  │  │  ├─ some_functions.mat
│  │        │  │  │  │  │  ├─ sqr.mat
│  │        │  │  │  │  │  ├─ test3dmatrix_6.1_SOL2.mat
│  │        │  │  │  │  │  ├─ test3dmatrix_6.5.1_GLNX86.mat
│  │        │  │  │  │  │  ├─ test3dmatrix_7.1_GLNX86.mat
│  │        │  │  │  │  │  ├─ test3dmatrix_7.4_GLNX86.mat
│  │        │  │  │  │  │  ├─ testbool_8_WIN64.mat
│  │        │  │  │  │  │  ├─ testcellnest_6.1_SOL2.mat
│  │        │  │  │  │  │  ├─ testcellnest_6.5.1_GLNX86.mat
│  │        │  │  │  │  │  ├─ testcellnest_7.1_GLNX86.mat
│  │        │  │  │  │  │  ├─ testcellnest_7.4_GLNX86.mat
│  │        │  │  │  │  │  ├─ testcell_6.1_SOL2.mat
│  │        │  │  │  │  │  ├─ testcell_6.5.1_GLNX86.mat
│  │        │  │  │  │  │  ├─ testcell_7.1_GLNX86.mat
│  │        │  │  │  │  │  ├─ testcell_7.4_GLNX86.mat
│  │        │  │  │  │  │  ├─ testcomplex_4.2c_SOL2.mat
│  │        │  │  │  │  │  ├─ testcomplex_6.1_SOL2.mat
│  │        │  │  │  │  │  ├─ testcomplex_6.5.1_GLNX86.mat
│  │        │  │  │  │  │  ├─ testcomplex_7.1_GLNX86.mat
│  │        │  │  │  │  │  ├─ testcomplex_7.4_GLNX86.mat
│  │        │  │  │  │  │  ├─ testdouble_4.2c_SOL2.mat
│  │        │  │  │  │  │  ├─ testdouble_6.1_SOL2.mat
│  │        │  │  │  │  │  ├─ testdouble_6.5.1_GLNX86.mat
│  │        │  │  │  │  │  ├─ testdouble_7.1_GLNX86.mat
│  │        │  │  │  │  │  ├─ testdouble_7.4_GLNX86.mat
│  │        │  │  │  │  │  ├─ testemptycell_5.3_SOL2.mat
│  │        │  │  │  │  │  ├─ testemptycell_6.5.1_GLNX86.mat
│  │        │  │  │  │  │  ├─ testemptycell_7.1_GLNX86.mat
│  │        │  │  │  │  │  ├─ testemptycell_7.4_GLNX86.mat
│  │        │  │  │  │  │  ├─ testfunc_7.4_GLNX86.mat
│  │        │  │  │  │  │  ├─ testhdf5_7.4_GLNX86.mat
│  │        │  │  │  │  │  ├─ testmatrix_4.2c_SOL2.mat
│  │        │  │  │  │  │  ├─ testmatrix_6.1_SOL2.mat
│  │        │  │  │  │  │  ├─ testmatrix_6.5.1_GLNX86.mat
│  │        │  │  │  │  │  ├─ testmatrix_7.1_GLNX86.mat
│  │        │  │  │  │  │  ├─ testmatrix_7.4_GLNX86.mat
│  │        │  │  │  │  │  ├─ testminus_4.2c_SOL2.mat
│  │        │  │  │  │  │  ├─ testminus_6.1_SOL2.mat
│  │        │  │  │  │  │  ├─ testminus_6.5.1_GLNX86.mat
│  │        │  │  │  │  │  ├─ testminus_7.1_GLNX86.mat
│  │        │  │  │  │  │  ├─ testminus_7.4_GLNX86.mat
│  │        │  │  │  │  │  ├─ testmulti_4.2c_SOL2.mat
│  │        │  │  │  │  │  ├─ testmulti_7.1_GLNX86.mat
│  │        │  │  │  │  │  ├─ testmulti_7.4_GLNX86.mat
│  │        │  │  │  │  │  ├─ testobject_6.1_SOL2.mat
│  │        │  │  │  │  │  ├─ testobject_6.5.1_GLNX86.mat
│  │        │  │  │  │  │  ├─ testobject_7.1_GLNX86.mat
│  │        │  │  │  │  │  ├─ testobject_7.4_GLNX86.mat
│  │        │  │  │  │  │  ├─ testonechar_4.2c_SOL2.mat
│  │        │  │  │  │  │  ├─ testonechar_6.1_SOL2.mat
│  │        │  │  │  │  │  ├─ testonechar_6.5.1_GLNX86.mat
│  │        │  │  │  │  │  ├─ testonechar_7.1_GLNX86.mat
│  │        │  │  │  │  │  ├─ testonechar_7.4_GLNX86.mat
│  │        │  │  │  │  │  ├─ testscalarcell_7.4_GLNX86.mat
│  │        │  │  │  │  │  ├─ testsimplecell.mat
│  │        │  │  │  │  │  ├─ testsparsecomplex_4.2c_SOL2.mat
│  │        │  │  │  │  │  ├─ testsparsecomplex_6.1_SOL2.mat
│  │        │  │  │  │  │  ├─ testsparsecomplex_6.5.1_GLNX86.mat
│  │        │  │  │  │  │  ├─ testsparsecomplex_7.1_GLNX86.mat
│  │        │  │  │  │  │  ├─ testsparsecomplex_7.4_GLNX86.mat
│  │        │  │  │  │  │  ├─ testsparsefloat_7.4_GLNX86.mat
│  │        │  │  │  │  │  ├─ testsparse_4.2c_SOL2.mat
│  │        │  │  │  │  │  ├─ testsparse_6.1_SOL2.mat
│  │        │  │  │  │  │  ├─ testsparse_6.5.1_GLNX86.mat
│  │        │  │  │  │  │  ├─ testsparse_7.1_GLNX86.mat
│  │        │  │  │  │  │  ├─ testsparse_7.4_GLNX86.mat
│  │        │  │  │  │  │  ├─ teststringarray_4.2c_SOL2.mat
│  │        │  │  │  │  │  ├─ teststringarray_6.1_SOL2.mat
│  │        │  │  │  │  │  ├─ teststringarray_6.5.1_GLNX86.mat
│  │        │  │  │  │  │  ├─ teststringarray_7.1_GLNX86.mat
│  │        │  │  │  │  │  ├─ teststringarray_7.4_GLNX86.mat
│  │        │  │  │  │  │  ├─ teststring_4.2c_SOL2.mat
│  │        │  │  │  │  │  ├─ teststring_6.1_SOL2.mat
│  │        │  │  │  │  │  ├─ teststring_6.5.1_GLNX86.mat
│  │        │  │  │  │  │  ├─ teststring_7.1_GLNX86.mat
│  │        │  │  │  │  │  ├─ teststring_7.4_GLNX86.mat
│  │        │  │  │  │  │  ├─ teststructarr_6.1_SOL2.mat
│  │        │  │  │  │  │  ├─ teststructarr_6.5.1_GLNX86.mat
│  │        │  │  │  │  │  ├─ teststructarr_7.1_GLNX86.mat
│  │        │  │  │  │  │  ├─ teststructarr_7.4_GLNX86.mat
│  │        │  │  │  │  │  ├─ teststructnest_6.1_SOL2.mat
│  │        │  │  │  │  │  ├─ teststructnest_6.5.1_GLNX86.mat
│  │        │  │  │  │  │  ├─ teststructnest_7.1_GLNX86.mat
│  │        │  │  │  │  │  ├─ teststructnest_7.4_GLNX86.mat
│  │        │  │  │  │  │  ├─ teststruct_6.1_SOL2.mat
│  │        │  │  │  │  │  ├─ teststruct_6.5.1_GLNX86.mat
│  │        │  │  │  │  │  ├─ teststruct_7.1_GLNX86.mat
│  │        │  │  │  │  │  ├─ teststruct_7.4_GLNX86.mat
│  │        │  │  │  │  │  ├─ testunicode_7.1_GLNX86.mat
│  │        │  │  │  │  │  ├─ testunicode_7.4_GLNX86.mat
│  │        │  │  │  │  │  ├─ testvec_4_GLNX86.mat
│  │        │  │  │  │  │  ├─ test_empty_struct.mat
│  │        │  │  │  │  │  ├─ test_mat4_le_floats.mat
│  │        │  │  │  │  │  └─ test_skip_variable.mat
│  │        │  │  │  │  ├─ test_byteordercodes.py
│  │        │  │  │  │  ├─ test_mio.py
│  │        │  │  │  │  ├─ test_mio5_utils.py
│  │        │  │  │  │  ├─ test_miobase.py
│  │        │  │  │  │  ├─ test_mio_funcs.py
│  │        │  │  │  │  ├─ test_mio_utils.py
│  │        │  │  │  │  ├─ test_pathological.py
│  │        │  │  │  │  ├─ test_streams.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_byteordercodes.cpython-312.pyc
│  │        │  │  │  │     ├─ test_mio.cpython-312.pyc
│  │        │  │  │  │     ├─ test_mio5_utils.cpython-312.pyc
│  │        │  │  │  │     ├─ test_miobase.cpython-312.pyc
│  │        │  │  │  │     ├─ test_mio_funcs.cpython-312.pyc
│  │        │  │  │  │     ├─ test_mio_utils.cpython-312.pyc
│  │        │  │  │  │     ├─ test_pathological.cpython-312.pyc
│  │        │  │  │  │     ├─ test_streams.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ _byteordercodes.py
│  │        │  │  │  ├─ _mio.py
│  │        │  │  │  ├─ _mio4.py
│  │        │  │  │  ├─ _mio5.py
│  │        │  │  │  ├─ _mio5_params.py
│  │        │  │  │  ├─ _mio5_utils.cpython-312-darwin.so
│  │        │  │  │  ├─ _miobase.py
│  │        │  │  │  ├─ _mio_utils.cpython-312-darwin.so
│  │        │  │  │  ├─ _streams.cpython-312-darwin.so
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ byteordercodes.cpython-312.pyc
│  │        │  │  │     ├─ mio.cpython-312.pyc
│  │        │  │  │     ├─ mio4.cpython-312.pyc
│  │        │  │  │     ├─ mio5.cpython-312.pyc
│  │        │  │  │     ├─ mio5_params.cpython-312.pyc
│  │        │  │  │     ├─ mio5_utils.cpython-312.pyc
│  │        │  │  │     ├─ miobase.cpython-312.pyc
│  │        │  │  │     ├─ mio_utils.cpython-312.pyc
│  │        │  │  │     ├─ streams.cpython-312.pyc
│  │        │  │  │     ├─ _byteordercodes.cpython-312.pyc
│  │        │  │  │     ├─ _mio.cpython-312.pyc
│  │        │  │  │     ├─ _mio4.cpython-312.pyc
│  │        │  │  │     ├─ _mio5.cpython-312.pyc
│  │        │  │  │     ├─ _mio5_params.cpython-312.pyc
│  │        │  │  │     ├─ _miobase.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ mmio.py
│  │        │  │  ├─ netcdf.py
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ data
│  │        │  │  │  │  ├─ array_float32_1d.sav
│  │        │  │  │  │  ├─ array_float32_2d.sav
│  │        │  │  │  │  ├─ array_float32_3d.sav
│  │        │  │  │  │  ├─ array_float32_4d.sav
│  │        │  │  │  │  ├─ array_float32_5d.sav
│  │        │  │  │  │  ├─ array_float32_6d.sav
│  │        │  │  │  │  ├─ array_float32_7d.sav
│  │        │  │  │  │  ├─ array_float32_8d.sav
│  │        │  │  │  │  ├─ array_float32_pointer_1d.sav
│  │        │  │  │  │  ├─ array_float32_pointer_2d.sav
│  │        │  │  │  │  ├─ array_float32_pointer_3d.sav
│  │        │  │  │  │  ├─ array_float32_pointer_4d.sav
│  │        │  │  │  │  ├─ array_float32_pointer_5d.sav
│  │        │  │  │  │  ├─ array_float32_pointer_6d.sav
│  │        │  │  │  │  ├─ array_float32_pointer_7d.sav
│  │        │  │  │  │  ├─ array_float32_pointer_8d.sav
│  │        │  │  │  │  ├─ example_1.nc
│  │        │  │  │  │  ├─ example_2.nc
│  │        │  │  │  │  ├─ example_3_maskedvals.nc
│  │        │  │  │  │  ├─ fortran-3x3d-2i.dat
│  │        │  │  │  │  ├─ fortran-mixed.dat
│  │        │  │  │  │  ├─ fortran-sf8-11x1x10.dat
│  │        │  │  │  │  ├─ fortran-sf8-15x10x22.dat
│  │        │  │  │  │  ├─ fortran-sf8-1x1x1.dat
│  │        │  │  │  │  ├─ fortran-sf8-1x1x5.dat
│  │        │  │  │  │  ├─ fortran-sf8-1x1x7.dat
│  │        │  │  │  │  ├─ fortran-sf8-1x3x5.dat
│  │        │  │  │  │  ├─ fortran-si4-11x1x10.dat
│  │        │  │  │  │  ├─ fortran-si4-15x10x22.dat
│  │        │  │  │  │  ├─ fortran-si4-1x1x1.dat
│  │        │  │  │  │  ├─ fortran-si4-1x1x5.dat
│  │        │  │  │  │  ├─ fortran-si4-1x1x7.dat
│  │        │  │  │  │  ├─ fortran-si4-1x3x5.dat
│  │        │  │  │  │  ├─ invalid_pointer.sav
│  │        │  │  │  │  ├─ null_pointer.sav
│  │        │  │  │  │  ├─ scalar_byte.sav
│  │        │  │  │  │  ├─ scalar_byte_descr.sav
│  │        │  │  │  │  ├─ scalar_complex32.sav
│  │        │  │  │  │  ├─ scalar_complex64.sav
│  │        │  │  │  │  ├─ scalar_float32.sav
│  │        │  │  │  │  ├─ scalar_float64.sav
│  │        │  │  │  │  ├─ scalar_heap_pointer.sav
│  │        │  │  │  │  ├─ scalar_int16.sav
│  │        │  │  │  │  ├─ scalar_int32.sav
│  │        │  │  │  │  ├─ scalar_int64.sav
│  │        │  │  │  │  ├─ scalar_string.sav
│  │        │  │  │  │  ├─ scalar_uint16.sav
│  │        │  │  │  │  ├─ scalar_uint32.sav
│  │        │  │  │  │  ├─ scalar_uint64.sav
│  │        │  │  │  │  ├─ struct_arrays.sav
│  │        │  │  │  │  ├─ struct_arrays_byte_idl80.sav
│  │        │  │  │  │  ├─ struct_arrays_replicated.sav
│  │        │  │  │  │  ├─ struct_arrays_replicated_3d.sav
│  │        │  │  │  │  ├─ struct_inherit.sav
│  │        │  │  │  │  ├─ struct_pointers.sav
│  │        │  │  │  │  ├─ struct_pointers_replicated.sav
│  │        │  │  │  │  ├─ struct_pointers_replicated_3d.sav
│  │        │  │  │  │  ├─ struct_pointer_arrays.sav
│  │        │  │  │  │  ├─ struct_pointer_arrays_replicated.sav
│  │        │  │  │  │  ├─ struct_pointer_arrays_replicated_3d.sav
│  │        │  │  │  │  ├─ struct_scalars.sav
│  │        │  │  │  │  ├─ struct_scalars_replicated.sav
│  │        │  │  │  │  ├─ struct_scalars_replicated_3d.sav
│  │        │  │  │  │  ├─ test-1234Hz-le-1ch-10S-20bit-extra.wav
│  │        │  │  │  │  ├─ test-44100Hz-2ch-32bit-float-be.wav
│  │        │  │  │  │  ├─ test-44100Hz-2ch-32bit-float-le.wav
│  │        │  │  │  │  ├─ test-44100Hz-be-1ch-4bytes.wav
│  │        │  │  │  │  ├─ test-44100Hz-le-1ch-4bytes-early-eof-no-data.wav
│  │        │  │  │  │  ├─ test-44100Hz-le-1ch-4bytes-early-eof.wav
│  │        │  │  │  │  ├─ test-44100Hz-le-1ch-4bytes-incomplete-chunk.wav
│  │        │  │  │  │  ├─ test-44100Hz-le-1ch-4bytes-rf64.wav
│  │        │  │  │  │  ├─ test-44100Hz-le-1ch-4bytes.wav
│  │        │  │  │  │  ├─ test-48000Hz-2ch-64bit-float-le-wavex.wav
│  │        │  │  │  │  ├─ test-8000Hz-be-3ch-5S-24bit.wav
│  │        │  │  │  │  ├─ test-8000Hz-le-1ch-1byte-ulaw.wav
│  │        │  │  │  │  ├─ test-8000Hz-le-2ch-1byteu.wav
│  │        │  │  │  │  ├─ test-8000Hz-le-3ch-5S-24bit-inconsistent.wav
│  │        │  │  │  │  ├─ test-8000Hz-le-3ch-5S-24bit-rf64.wav
│  │        │  │  │  │  ├─ test-8000Hz-le-3ch-5S-24bit.wav
│  │        │  │  │  │  ├─ test-8000Hz-le-3ch-5S-36bit.wav
│  │        │  │  │  │  ├─ test-8000Hz-le-3ch-5S-45bit.wav
│  │        │  │  │  │  ├─ test-8000Hz-le-3ch-5S-53bit.wav
│  │        │  │  │  │  ├─ test-8000Hz-le-3ch-5S-64bit.wav
│  │        │  │  │  │  ├─ test-8000Hz-le-4ch-9S-12bit.wav
│  │        │  │  │  │  ├─ test-8000Hz-le-5ch-9S-5bit.wav
│  │        │  │  │  │  ├─ Transparent Busy.ani
│  │        │  │  │  │  └─ various_compressed.sav
│  │        │  │  │  ├─ test_fortran.py
│  │        │  │  │  ├─ test_idl.py
│  │        │  │  │  ├─ test_mmio.py
│  │        │  │  │  ├─ test_netcdf.py
│  │        │  │  │  ├─ test_paths.py
│  │        │  │  │  ├─ test_wavfile.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_fortran.cpython-312.pyc
│  │        │  │  │     ├─ test_idl.cpython-312.pyc
│  │        │  │  │     ├─ test_mmio.cpython-312.pyc
│  │        │  │  │     ├─ test_netcdf.cpython-312.pyc
│  │        │  │  │     ├─ test_paths.cpython-312.pyc
│  │        │  │  │     ├─ test_wavfile.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ wavfile.py
│  │        │  │  ├─ _fast_matrix_market
│  │        │  │  │  ├─ _fmm_core.cpython-312-darwin.so
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _fortran.py
│  │        │  │  ├─ _harwell_boeing
│  │        │  │  │  ├─ hb.py
│  │        │  │  │  ├─ tests
│  │        │  │  │  │  ├─ test_fortran_format.py
│  │        │  │  │  │  ├─ test_hb.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_fortran_format.cpython-312.pyc
│  │        │  │  │  │     ├─ test_hb.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ _fortran_format_parser.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ hb.cpython-312.pyc
│  │        │  │  │     ├─ _fortran_format_parser.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _idl.py
│  │        │  │  ├─ _mmio.py
│  │        │  │  ├─ _netcdf.py
│  │        │  │  ├─ _test_fortran.cpython-312-darwin.so
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ harwell_boeing.cpython-312.pyc
│  │        │  │     ├─ idl.cpython-312.pyc
│  │        │  │     ├─ mmio.cpython-312.pyc
│  │        │  │     ├─ netcdf.cpython-312.pyc
│  │        │  │     ├─ wavfile.cpython-312.pyc
│  │        │  │     ├─ _fortran.cpython-312.pyc
│  │        │  │     ├─ _idl.cpython-312.pyc
│  │        │  │     ├─ _mmio.cpython-312.pyc
│  │        │  │     ├─ _netcdf.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ linalg
│  │        │  │  ├─ basic.py
│  │        │  │  ├─ blas.py
│  │        │  │  ├─ cython_blas.cpython-312-darwin.so
│  │        │  │  ├─ cython_blas.pxd
│  │        │  │  ├─ cython_blas.pyx
│  │        │  │  ├─ cython_lapack.cpython-312-darwin.so
│  │        │  │  ├─ cython_lapack.pxd
│  │        │  │  ├─ cython_lapack.pyx
│  │        │  │  ├─ decomp.py
│  │        │  │  ├─ decomp_cholesky.py
│  │        │  │  ├─ decomp_lu.py
│  │        │  │  ├─ decomp_qr.py
│  │        │  │  ├─ decomp_schur.py
│  │        │  │  ├─ decomp_svd.py
│  │        │  │  ├─ interpolative.py
│  │        │  │  ├─ lapack.py
│  │        │  │  ├─ matfuncs.py
│  │        │  │  ├─ misc.py
│  │        │  │  ├─ special_matrices.py
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ data
│  │        │  │  │  │  ├─ carex_15_data.npz
│  │        │  │  │  │  ├─ carex_18_data.npz
│  │        │  │  │  │  ├─ carex_19_data.npz
│  │        │  │  │  │  ├─ carex_20_data.npz
│  │        │  │  │  │  ├─ carex_6_data.npz
│  │        │  │  │  │  └─ gendare_20170120_data.npz
│  │        │  │  │  ├─ test_basic.py
│  │        │  │  │  ├─ test_blas.py
│  │        │  │  │  ├─ test_cythonized_array_utils.py
│  │        │  │  │  ├─ test_cython_blas.py
│  │        │  │  │  ├─ test_cython_lapack.py
│  │        │  │  │  ├─ test_decomp.py
│  │        │  │  │  ├─ test_decomp_cholesky.py
│  │        │  │  │  ├─ test_decomp_cossin.py
│  │        │  │  │  ├─ test_decomp_ldl.py
│  │        │  │  │  ├─ test_decomp_lu.py
│  │        │  │  │  ├─ test_decomp_polar.py
│  │        │  │  │  ├─ test_decomp_update.py
│  │        │  │  │  ├─ test_extending.py
│  │        │  │  │  ├─ test_fblas.py
│  │        │  │  │  ├─ test_interpolative.py
│  │        │  │  │  ├─ test_lapack.py
│  │        │  │  │  ├─ test_matfuncs.py
│  │        │  │  │  ├─ test_matmul_toeplitz.py
│  │        │  │  │  ├─ test_procrustes.py
│  │        │  │  │  ├─ test_sketches.py
│  │        │  │  │  ├─ test_solvers.py
│  │        │  │  │  ├─ test_solve_toeplitz.py
│  │        │  │  │  ├─ test_special_matrices.py
│  │        │  │  │  ├─ _cython_examples
│  │        │  │  │  │  ├─ extending.pyx
│  │        │  │  │  │  └─ meson.build
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_basic.cpython-312.pyc
│  │        │  │  │     ├─ test_blas.cpython-312.pyc
│  │        │  │  │     ├─ test_cythonized_array_utils.cpython-312.pyc
│  │        │  │  │     ├─ test_cython_blas.cpython-312.pyc
│  │        │  │  │     ├─ test_cython_lapack.cpython-312.pyc
│  │        │  │  │     ├─ test_decomp.cpython-312.pyc
│  │        │  │  │     ├─ test_decomp_cholesky.cpython-312.pyc
│  │        │  │  │     ├─ test_decomp_cossin.cpython-312.pyc
│  │        │  │  │     ├─ test_decomp_ldl.cpython-312.pyc
│  │        │  │  │     ├─ test_decomp_lu.cpython-312.pyc
│  │        │  │  │     ├─ test_decomp_polar.cpython-312.pyc
│  │        │  │  │     ├─ test_decomp_update.cpython-312.pyc
│  │        │  │  │     ├─ test_extending.cpython-312.pyc
│  │        │  │  │     ├─ test_fblas.cpython-312.pyc
│  │        │  │  │     ├─ test_interpolative.cpython-312.pyc
│  │        │  │  │     ├─ test_lapack.cpython-312.pyc
│  │        │  │  │     ├─ test_matfuncs.cpython-312.pyc
│  │        │  │  │     ├─ test_matmul_toeplitz.cpython-312.pyc
│  │        │  │  │     ├─ test_procrustes.cpython-312.pyc
│  │        │  │  │     ├─ test_sketches.cpython-312.pyc
│  │        │  │  │     ├─ test_solvers.cpython-312.pyc
│  │        │  │  │     ├─ test_solve_toeplitz.cpython-312.pyc
│  │        │  │  │     ├─ test_special_matrices.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _basic.py
│  │        │  │  ├─ _blas_subroutines.h
│  │        │  │  ├─ _cythonized_array_utils.cpython-312-darwin.so
│  │        │  │  ├─ _cythonized_array_utils.pxd
│  │        │  │  ├─ _cythonized_array_utils.pyi
│  │        │  │  ├─ _decomp.py
│  │        │  │  ├─ _decomp_cholesky.py
│  │        │  │  ├─ _decomp_cossin.py
│  │        │  │  ├─ _decomp_interpolative.cpython-312-darwin.so
│  │        │  │  ├─ _decomp_ldl.py
│  │        │  │  ├─ _decomp_lu.py
│  │        │  │  ├─ _decomp_lu_cython.cpython-312-darwin.so
│  │        │  │  ├─ _decomp_lu_cython.pyi
│  │        │  │  ├─ _decomp_polar.py
│  │        │  │  ├─ _decomp_qr.py
│  │        │  │  ├─ _decomp_qz.py
│  │        │  │  ├─ _decomp_schur.py
│  │        │  │  ├─ _decomp_svd.py
│  │        │  │  ├─ _decomp_update.cpython-312-darwin.so
│  │        │  │  ├─ _expm_frechet.py
│  │        │  │  ├─ _fblas.cpython-312-darwin.so
│  │        │  │  ├─ _flapack.cpython-312-darwin.so
│  │        │  │  ├─ _lapack_subroutines.h
│  │        │  │  ├─ _linalg_pythran.cpython-312-darwin.so
│  │        │  │  ├─ _matfuncs.py
│  │        │  │  ├─ _matfuncs_expm.cpython-312-darwin.so
│  │        │  │  ├─ _matfuncs_expm.pyi
│  │        │  │  ├─ _matfuncs_inv_ssq.py
│  │        │  │  ├─ _matfuncs_sqrtm.py
│  │        │  │  ├─ _matfuncs_sqrtm_triu.cpython-312-darwin.so
│  │        │  │  ├─ _misc.py
│  │        │  │  ├─ _procrustes.py
│  │        │  │  ├─ _sketches.py
│  │        │  │  ├─ _solvers.py
│  │        │  │  ├─ _solve_toeplitz.cpython-312-darwin.so
│  │        │  │  ├─ _special_matrices.py
│  │        │  │  ├─ _testutils.py
│  │        │  │  ├─ __init__.pxd
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ basic.cpython-312.pyc
│  │        │  │     ├─ blas.cpython-312.pyc
│  │        │  │     ├─ decomp.cpython-312.pyc
│  │        │  │     ├─ decomp_cholesky.cpython-312.pyc
│  │        │  │     ├─ decomp_lu.cpython-312.pyc
│  │        │  │     ├─ decomp_qr.cpython-312.pyc
│  │        │  │     ├─ decomp_schur.cpython-312.pyc
│  │        │  │     ├─ decomp_svd.cpython-312.pyc
│  │        │  │     ├─ interpolative.cpython-312.pyc
│  │        │  │     ├─ lapack.cpython-312.pyc
│  │        │  │     ├─ matfuncs.cpython-312.pyc
│  │        │  │     ├─ misc.cpython-312.pyc
│  │        │  │     ├─ special_matrices.cpython-312.pyc
│  │        │  │     ├─ _basic.cpython-312.pyc
│  │        │  │     ├─ _decomp.cpython-312.pyc
│  │        │  │     ├─ _decomp_cholesky.cpython-312.pyc
│  │        │  │     ├─ _decomp_cossin.cpython-312.pyc
│  │        │  │     ├─ _decomp_ldl.cpython-312.pyc
│  │        │  │     ├─ _decomp_lu.cpython-312.pyc
│  │        │  │     ├─ _decomp_polar.cpython-312.pyc
│  │        │  │     ├─ _decomp_qr.cpython-312.pyc
│  │        │  │     ├─ _decomp_qz.cpython-312.pyc
│  │        │  │     ├─ _decomp_schur.cpython-312.pyc
│  │        │  │     ├─ _decomp_svd.cpython-312.pyc
│  │        │  │     ├─ _expm_frechet.cpython-312.pyc
│  │        │  │     ├─ _matfuncs.cpython-312.pyc
│  │        │  │     ├─ _matfuncs_inv_ssq.cpython-312.pyc
│  │        │  │     ├─ _matfuncs_sqrtm.cpython-312.pyc
│  │        │  │     ├─ _misc.cpython-312.pyc
│  │        │  │     ├─ _procrustes.cpython-312.pyc
│  │        │  │     ├─ _sketches.cpython-312.pyc
│  │        │  │     ├─ _solvers.cpython-312.pyc
│  │        │  │     ├─ _special_matrices.cpython-312.pyc
│  │        │  │     ├─ _testutils.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ misc
│  │        │  │  ├─ common.py
│  │        │  │  ├─ doccer.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ common.cpython-312.pyc
│  │        │  │     ├─ doccer.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ ndimage
│  │        │  │  ├─ filters.py
│  │        │  │  ├─ fourier.py
│  │        │  │  ├─ interpolation.py
│  │        │  │  ├─ measurements.py
│  │        │  │  ├─ morphology.py
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ data
│  │        │  │  │  │  ├─ label_inputs.txt
│  │        │  │  │  │  ├─ label_results.txt
│  │        │  │  │  │  └─ label_strels.txt
│  │        │  │  │  ├─ dots.png
│  │        │  │  │  ├─ test_c_api.py
│  │        │  │  │  ├─ test_datatypes.py
│  │        │  │  │  ├─ test_filters.py
│  │        │  │  │  ├─ test_fourier.py
│  │        │  │  │  ├─ test_interpolation.py
│  │        │  │  │  ├─ test_measurements.py
│  │        │  │  │  ├─ test_morphology.py
│  │        │  │  │  ├─ test_ni_support.py
│  │        │  │  │  ├─ test_splines.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_c_api.cpython-312.pyc
│  │        │  │  │     ├─ test_datatypes.cpython-312.pyc
│  │        │  │  │     ├─ test_filters.cpython-312.pyc
│  │        │  │  │     ├─ test_fourier.cpython-312.pyc
│  │        │  │  │     ├─ test_interpolation.cpython-312.pyc
│  │        │  │  │     ├─ test_measurements.cpython-312.pyc
│  │        │  │  │     ├─ test_morphology.cpython-312.pyc
│  │        │  │  │     ├─ test_ni_support.cpython-312.pyc
│  │        │  │  │     ├─ test_splines.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _ctest.cpython-312-darwin.so
│  │        │  │  ├─ _cytest.cpython-312-darwin.so
│  │        │  │  ├─ _delegators.py
│  │        │  │  ├─ _filters.py
│  │        │  │  ├─ _fourier.py
│  │        │  │  ├─ _interpolation.py
│  │        │  │  ├─ _measurements.py
│  │        │  │  ├─ _morphology.py
│  │        │  │  ├─ _ndimage_api.py
│  │        │  │  ├─ _nd_image.cpython-312-darwin.so
│  │        │  │  ├─ _ni_docstrings.py
│  │        │  │  ├─ _ni_label.cpython-312-darwin.so
│  │        │  │  ├─ _ni_support.py
│  │        │  │  ├─ _rank_filter_1d.cpython-312-darwin.so
│  │        │  │  ├─ _support_alternative_backends.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ filters.cpython-312.pyc
│  │        │  │     ├─ fourier.cpython-312.pyc
│  │        │  │     ├─ interpolation.cpython-312.pyc
│  │        │  │     ├─ measurements.cpython-312.pyc
│  │        │  │     ├─ morphology.cpython-312.pyc
│  │        │  │     ├─ _delegators.cpython-312.pyc
│  │        │  │     ├─ _filters.cpython-312.pyc
│  │        │  │     ├─ _fourier.cpython-312.pyc
│  │        │  │     ├─ _interpolation.cpython-312.pyc
│  │        │  │     ├─ _measurements.cpython-312.pyc
│  │        │  │     ├─ _morphology.cpython-312.pyc
│  │        │  │     ├─ _ndimage_api.cpython-312.pyc
│  │        │  │     ├─ _ni_docstrings.cpython-312.pyc
│  │        │  │     ├─ _ni_support.cpython-312.pyc
│  │        │  │     ├─ _support_alternative_backends.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ odr
│  │        │  │  ├─ models.py
│  │        │  │  ├─ odrpack.py
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ test_odr.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_odr.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _add_newdocs.py
│  │        │  │  ├─ _models.py
│  │        │  │  ├─ _odrpack.py
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ __odrpack.cpython-312-darwin.so
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ models.cpython-312.pyc
│  │        │  │     ├─ odrpack.cpython-312.pyc
│  │        │  │     ├─ _add_newdocs.cpython-312.pyc
│  │        │  │     ├─ _models.cpython-312.pyc
│  │        │  │     ├─ _odrpack.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ optimize
│  │        │  │  ├─ cobyla.py
│  │        │  │  ├─ cython_optimize
│  │        │  │  │  ├─ c_zeros.pxd
│  │        │  │  │  ├─ _zeros.cpython-312-darwin.so
│  │        │  │  │  ├─ _zeros.pxd
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ cython_optimize.pxd
│  │        │  │  ├─ elementwise.py
│  │        │  │  ├─ lbfgsb.py
│  │        │  │  ├─ linesearch.py
│  │        │  │  ├─ minpack.py
│  │        │  │  ├─ minpack2.py
│  │        │  │  ├─ moduleTNC.py
│  │        │  │  ├─ nonlin.py
│  │        │  │  ├─ optimize.py
│  │        │  │  ├─ slsqp.py
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ test_bracket.py
│  │        │  │  │  ├─ test_chandrupatla.py
│  │        │  │  │  ├─ test_cobyla.py
│  │        │  │  │  ├─ test_cobyqa.py
│  │        │  │  │  ├─ test_constraints.py
│  │        │  │  │  ├─ test_constraint_conversion.py
│  │        │  │  │  ├─ test_cython_optimize.py
│  │        │  │  │  ├─ test_differentiable_functions.py
│  │        │  │  │  ├─ test_direct.py
│  │        │  │  │  ├─ test_extending.py
│  │        │  │  │  ├─ test_hessian_update_strategy.py
│  │        │  │  │  ├─ test_isotonic_regression.py
│  │        │  │  │  ├─ test_lbfgsb_hessinv.py
│  │        │  │  │  ├─ test_lbfgsb_setulb.py
│  │        │  │  │  ├─ test_least_squares.py
│  │        │  │  │  ├─ test_linear_assignment.py
│  │        │  │  │  ├─ test_linesearch.py
│  │        │  │  │  ├─ test_linprog.py
│  │        │  │  │  ├─ test_lsq_common.py
│  │        │  │  │  ├─ test_lsq_linear.py
│  │        │  │  │  ├─ test_milp.py
│  │        │  │  │  ├─ test_minimize_constrained.py
│  │        │  │  │  ├─ test_minpack.py
│  │        │  │  │  ├─ test_nnls.py
│  │        │  │  │  ├─ test_nonlin.py
│  │        │  │  │  ├─ test_optimize.py
│  │        │  │  │  ├─ test_quadratic_assignment.py
│  │        │  │  │  ├─ test_regression.py
│  │        │  │  │  ├─ test_slsqp.py
│  │        │  │  │  ├─ test_tnc.py
│  │        │  │  │  ├─ test_trustregion.py
│  │        │  │  │  ├─ test_trustregion_exact.py
│  │        │  │  │  ├─ test_trustregion_krylov.py
│  │        │  │  │  ├─ test_zeros.py
│  │        │  │  │  ├─ test__basinhopping.py
│  │        │  │  │  ├─ test__differential_evolution.py
│  │        │  │  │  ├─ test__dual_annealing.py
│  │        │  │  │  ├─ test__linprog_clean_inputs.py
│  │        │  │  │  ├─ test__numdiff.py
│  │        │  │  │  ├─ test__remove_redundancy.py
│  │        │  │  │  ├─ test__root.py
│  │        │  │  │  ├─ test__shgo.py
│  │        │  │  │  ├─ test__spectral.py
│  │        │  │  │  ├─ _cython_examples
│  │        │  │  │  │  ├─ extending.pyx
│  │        │  │  │  │  └─ meson.build
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_bracket.cpython-312.pyc
│  │        │  │  │     ├─ test_chandrupatla.cpython-312.pyc
│  │        │  │  │     ├─ test_cobyla.cpython-312.pyc
│  │        │  │  │     ├─ test_cobyqa.cpython-312.pyc
│  │        │  │  │     ├─ test_constraints.cpython-312.pyc
│  │        │  │  │     ├─ test_constraint_conversion.cpython-312.pyc
│  │        │  │  │     ├─ test_cython_optimize.cpython-312.pyc
│  │        │  │  │     ├─ test_differentiable_functions.cpython-312.pyc
│  │        │  │  │     ├─ test_direct.cpython-312.pyc
│  │        │  │  │     ├─ test_extending.cpython-312.pyc
│  │        │  │  │     ├─ test_hessian_update_strategy.cpython-312.pyc
│  │        │  │  │     ├─ test_isotonic_regression.cpython-312.pyc
│  │        │  │  │     ├─ test_lbfgsb_hessinv.cpython-312.pyc
│  │        │  │  │     ├─ test_lbfgsb_setulb.cpython-312.pyc
│  │        │  │  │     ├─ test_least_squares.cpython-312.pyc
│  │        │  │  │     ├─ test_linear_assignment.cpython-312.pyc
│  │        │  │  │     ├─ test_linesearch.cpython-312.pyc
│  │        │  │  │     ├─ test_linprog.cpython-312.pyc
│  │        │  │  │     ├─ test_lsq_common.cpython-312.pyc
│  │        │  │  │     ├─ test_lsq_linear.cpython-312.pyc
│  │        │  │  │     ├─ test_milp.cpython-312.pyc
│  │        │  │  │     ├─ test_minimize_constrained.cpython-312.pyc
│  │        │  │  │     ├─ test_minpack.cpython-312.pyc
│  │        │  │  │     ├─ test_nnls.cpython-312.pyc
│  │        │  │  │     ├─ test_nonlin.cpython-312.pyc
│  │        │  │  │     ├─ test_optimize.cpython-312.pyc
│  │        │  │  │     ├─ test_quadratic_assignment.cpython-312.pyc
│  │        │  │  │     ├─ test_regression.cpython-312.pyc
│  │        │  │  │     ├─ test_slsqp.cpython-312.pyc
│  │        │  │  │     ├─ test_tnc.cpython-312.pyc
│  │        │  │  │     ├─ test_trustregion.cpython-312.pyc
│  │        │  │  │     ├─ test_trustregion_exact.cpython-312.pyc
│  │        │  │  │     ├─ test_trustregion_krylov.cpython-312.pyc
│  │        │  │  │     ├─ test_zeros.cpython-312.pyc
│  │        │  │  │     ├─ test__basinhopping.cpython-312.pyc
│  │        │  │  │     ├─ test__differential_evolution.cpython-312.pyc
│  │        │  │  │     ├─ test__dual_annealing.cpython-312.pyc
│  │        │  │  │     ├─ test__linprog_clean_inputs.cpython-312.pyc
│  │        │  │  │     ├─ test__numdiff.cpython-312.pyc
│  │        │  │  │     ├─ test__remove_redundancy.cpython-312.pyc
│  │        │  │  │     ├─ test__root.cpython-312.pyc
│  │        │  │  │     ├─ test__shgo.cpython-312.pyc
│  │        │  │  │     ├─ test__spectral.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ tnc.py
│  │        │  │  ├─ zeros.py
│  │        │  │  ├─ _basinhopping.py
│  │        │  │  ├─ _bglu_dense.cpython-312-darwin.so
│  │        │  │  ├─ _bracket.py
│  │        │  │  ├─ _chandrupatla.py
│  │        │  │  ├─ _cobyla.cpython-312-darwin.so
│  │        │  │  ├─ _cobyla_py.py
│  │        │  │  ├─ _cobyqa_py.py
│  │        │  │  ├─ _constraints.py
│  │        │  │  ├─ _cython_nnls.cpython-312-darwin.so
│  │        │  │  ├─ _dcsrch.py
│  │        │  │  ├─ _differentiable_functions.py
│  │        │  │  ├─ _differentialevolution.py
│  │        │  │  ├─ _direct.cpython-312-darwin.so
│  │        │  │  ├─ _direct_py.py
│  │        │  │  ├─ _dual_annealing.py
│  │        │  │  ├─ _elementwise.py
│  │        │  │  ├─ _group_columns.cpython-312-darwin.so
│  │        │  │  ├─ _hessian_update_strategy.py
│  │        │  │  ├─ _highspy
│  │        │  │  │  ├─ _core.cpython-312-darwin.so
│  │        │  │  │  ├─ _highs_options.cpython-312-darwin.so
│  │        │  │  │  ├─ _highs_wrapper.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ _highs_wrapper.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _isotonic.py
│  │        │  │  ├─ _lbfgsb.cpython-312-darwin.so
│  │        │  │  ├─ _lbfgsb_py.py
│  │        │  │  ├─ _linesearch.py
│  │        │  │  ├─ _linprog.py
│  │        │  │  ├─ _linprog_doc.py
│  │        │  │  ├─ _linprog_highs.py
│  │        │  │  ├─ _linprog_ip.py
│  │        │  │  ├─ _linprog_rs.py
│  │        │  │  ├─ _linprog_simplex.py
│  │        │  │  ├─ _linprog_util.py
│  │        │  │  ├─ _lsap.cpython-312-darwin.so
│  │        │  │  ├─ _lsq
│  │        │  │  │  ├─ bvls.py
│  │        │  │  │  ├─ common.py
│  │        │  │  │  ├─ dogbox.py
│  │        │  │  │  ├─ givens_elimination.cpython-312-darwin.so
│  │        │  │  │  ├─ least_squares.py
│  │        │  │  │  ├─ lsq_linear.py
│  │        │  │  │  ├─ trf.py
│  │        │  │  │  ├─ trf_linear.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ bvls.cpython-312.pyc
│  │        │  │  │     ├─ common.cpython-312.pyc
│  │        │  │  │     ├─ dogbox.cpython-312.pyc
│  │        │  │  │     ├─ least_squares.cpython-312.pyc
│  │        │  │  │     ├─ lsq_linear.cpython-312.pyc
│  │        │  │  │     ├─ trf.cpython-312.pyc
│  │        │  │  │     ├─ trf_linear.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _milp.py
│  │        │  │  ├─ _minimize.py
│  │        │  │  ├─ _minpack.cpython-312-darwin.so
│  │        │  │  ├─ _minpack_py.py
│  │        │  │  ├─ _moduleTNC.cpython-312-darwin.so
│  │        │  │  ├─ _nnls.py
│  │        │  │  ├─ _nonlin.py
│  │        │  │  ├─ _numdiff.py
│  │        │  │  ├─ _optimize.py
│  │        │  │  ├─ _pava_pybind.cpython-312-darwin.so
│  │        │  │  ├─ _qap.py
│  │        │  │  ├─ _remove_redundancy.py
│  │        │  │  ├─ _root.py
│  │        │  │  ├─ _root_scalar.py
│  │        │  │  ├─ _shgo.py
│  │        │  │  ├─ _shgo_lib
│  │        │  │  │  ├─ _complex.py
│  │        │  │  │  ├─ _vertex.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ _complex.cpython-312.pyc
│  │        │  │  │     ├─ _vertex.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _slsqp.cpython-312-darwin.so
│  │        │  │  ├─ _slsqp_py.py
│  │        │  │  ├─ _spectral.py
│  │        │  │  ├─ _tnc.py
│  │        │  │  ├─ _trlib
│  │        │  │  │  ├─ _trlib.cpython-312-darwin.so
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _trustregion.py
│  │        │  │  ├─ _trustregion_constr
│  │        │  │  │  ├─ canonical_constraint.py
│  │        │  │  │  ├─ equality_constrained_sqp.py
│  │        │  │  │  ├─ minimize_trustregion_constr.py
│  │        │  │  │  ├─ projections.py
│  │        │  │  │  ├─ qp_subproblem.py
│  │        │  │  │  ├─ report.py
│  │        │  │  │  ├─ tests
│  │        │  │  │  │  ├─ test_canonical_constraint.py
│  │        │  │  │  │  ├─ test_nested_minimize.py
│  │        │  │  │  │  ├─ test_projections.py
│  │        │  │  │  │  ├─ test_qp_subproblem.py
│  │        │  │  │  │  ├─ test_report.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_canonical_constraint.cpython-312.pyc
│  │        │  │  │  │     ├─ test_nested_minimize.cpython-312.pyc
│  │        │  │  │  │     ├─ test_projections.cpython-312.pyc
│  │        │  │  │  │     ├─ test_qp_subproblem.cpython-312.pyc
│  │        │  │  │  │     ├─ test_report.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ tr_interior_point.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ canonical_constraint.cpython-312.pyc
│  │        │  │  │     ├─ equality_constrained_sqp.cpython-312.pyc
│  │        │  │  │     ├─ minimize_trustregion_constr.cpython-312.pyc
│  │        │  │  │     ├─ projections.cpython-312.pyc
│  │        │  │  │     ├─ qp_subproblem.cpython-312.pyc
│  │        │  │  │     ├─ report.cpython-312.pyc
│  │        │  │  │     ├─ tr_interior_point.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _trustregion_dogleg.py
│  │        │  │  ├─ _trustregion_exact.py
│  │        │  │  ├─ _trustregion_krylov.py
│  │        │  │  ├─ _trustregion_ncg.py
│  │        │  │  ├─ _tstutils.py
│  │        │  │  ├─ _zeros.cpython-312-darwin.so
│  │        │  │  ├─ _zeros_py.py
│  │        │  │  ├─ __init__.pxd
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ cobyla.cpython-312.pyc
│  │        │  │     ├─ elementwise.cpython-312.pyc
│  │        │  │     ├─ lbfgsb.cpython-312.pyc
│  │        │  │     ├─ linesearch.cpython-312.pyc
│  │        │  │     ├─ minpack.cpython-312.pyc
│  │        │  │     ├─ minpack2.cpython-312.pyc
│  │        │  │     ├─ moduleTNC.cpython-312.pyc
│  │        │  │     ├─ nonlin.cpython-312.pyc
│  │        │  │     ├─ optimize.cpython-312.pyc
│  │        │  │     ├─ slsqp.cpython-312.pyc
│  │        │  │     ├─ tnc.cpython-312.pyc
│  │        │  │     ├─ zeros.cpython-312.pyc
│  │        │  │     ├─ _basinhopping.cpython-312.pyc
│  │        │  │     ├─ _bracket.cpython-312.pyc
│  │        │  │     ├─ _chandrupatla.cpython-312.pyc
│  │        │  │     ├─ _cobyla_py.cpython-312.pyc
│  │        │  │     ├─ _cobyqa_py.cpython-312.pyc
│  │        │  │     ├─ _constraints.cpython-312.pyc
│  │        │  │     ├─ _dcsrch.cpython-312.pyc
│  │        │  │     ├─ _differentiable_functions.cpython-312.pyc
│  │        │  │     ├─ _differentialevolution.cpython-312.pyc
│  │        │  │     ├─ _direct_py.cpython-312.pyc
│  │        │  │     ├─ _dual_annealing.cpython-312.pyc
│  │        │  │     ├─ _elementwise.cpython-312.pyc
│  │        │  │     ├─ _hessian_update_strategy.cpython-312.pyc
│  │        │  │     ├─ _isotonic.cpython-312.pyc
│  │        │  │     ├─ _lbfgsb_py.cpython-312.pyc
│  │        │  │     ├─ _linesearch.cpython-312.pyc
│  │        │  │     ├─ _linprog.cpython-312.pyc
│  │        │  │     ├─ _linprog_doc.cpython-312.pyc
│  │        │  │     ├─ _linprog_highs.cpython-312.pyc
│  │        │  │     ├─ _linprog_ip.cpython-312.pyc
│  │        │  │     ├─ _linprog_rs.cpython-312.pyc
│  │        │  │     ├─ _linprog_simplex.cpython-312.pyc
│  │        │  │     ├─ _linprog_util.cpython-312.pyc
│  │        │  │     ├─ _milp.cpython-312.pyc
│  │        │  │     ├─ _minimize.cpython-312.pyc
│  │        │  │     ├─ _minpack_py.cpython-312.pyc
│  │        │  │     ├─ _nnls.cpython-312.pyc
│  │        │  │     ├─ _nonlin.cpython-312.pyc
│  │        │  │     ├─ _numdiff.cpython-312.pyc
│  │        │  │     ├─ _optimize.cpython-312.pyc
│  │        │  │     ├─ _qap.cpython-312.pyc
│  │        │  │     ├─ _remove_redundancy.cpython-312.pyc
│  │        │  │     ├─ _root.cpython-312.pyc
│  │        │  │     ├─ _root_scalar.cpython-312.pyc
│  │        │  │     ├─ _shgo.cpython-312.pyc
│  │        │  │     ├─ _slsqp_py.cpython-312.pyc
│  │        │  │     ├─ _spectral.cpython-312.pyc
│  │        │  │     ├─ _tnc.cpython-312.pyc
│  │        │  │     ├─ _trustregion.cpython-312.pyc
│  │        │  │     ├─ _trustregion_dogleg.cpython-312.pyc
│  │        │  │     ├─ _trustregion_exact.cpython-312.pyc
│  │        │  │     ├─ _trustregion_krylov.cpython-312.pyc
│  │        │  │     ├─ _trustregion_ncg.cpython-312.pyc
│  │        │  │     ├─ _tstutils.cpython-312.pyc
│  │        │  │     ├─ _zeros_py.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ signal
│  │        │  │  ├─ bsplines.py
│  │        │  │  ├─ filter_design.py
│  │        │  │  ├─ fir_filter_design.py
│  │        │  │  ├─ ltisys.py
│  │        │  │  ├─ lti_conversion.py
│  │        │  │  ├─ signaltools.py
│  │        │  │  ├─ spectral.py
│  │        │  │  ├─ spline.py
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ mpsig.py
│  │        │  │  │  ├─ test_array_tools.py
│  │        │  │  │  ├─ test_bsplines.py
│  │        │  │  │  ├─ test_cont2discrete.py
│  │        │  │  │  ├─ test_czt.py
│  │        │  │  │  ├─ test_dltisys.py
│  │        │  │  │  ├─ test_filter_design.py
│  │        │  │  │  ├─ test_fir_filter_design.py
│  │        │  │  │  ├─ test_ltisys.py
│  │        │  │  │  ├─ test_max_len_seq.py
│  │        │  │  │  ├─ test_peak_finding.py
│  │        │  │  │  ├─ test_result_type.py
│  │        │  │  │  ├─ test_savitzky_golay.py
│  │        │  │  │  ├─ test_short_time_fft.py
│  │        │  │  │  ├─ test_signaltools.py
│  │        │  │  │  ├─ test_spectral.py
│  │        │  │  │  ├─ test_splines.py
│  │        │  │  │  ├─ test_upfirdn.py
│  │        │  │  │  ├─ test_waveforms.py
│  │        │  │  │  ├─ test_wavelets.py
│  │        │  │  │  ├─ test_windows.py
│  │        │  │  │  ├─ _scipy_spectral_test_shim.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ mpsig.cpython-312.pyc
│  │        │  │  │     ├─ test_array_tools.cpython-312.pyc
│  │        │  │  │     ├─ test_bsplines.cpython-312.pyc
│  │        │  │  │     ├─ test_cont2discrete.cpython-312.pyc
│  │        │  │  │     ├─ test_czt.cpython-312.pyc
│  │        │  │  │     ├─ test_dltisys.cpython-312.pyc
│  │        │  │  │     ├─ test_filter_design.cpython-312.pyc
│  │        │  │  │     ├─ test_fir_filter_design.cpython-312.pyc
│  │        │  │  │     ├─ test_ltisys.cpython-312.pyc
│  │        │  │  │     ├─ test_max_len_seq.cpython-312.pyc
│  │        │  │  │     ├─ test_peak_finding.cpython-312.pyc
│  │        │  │  │     ├─ test_result_type.cpython-312.pyc
│  │        │  │  │     ├─ test_savitzky_golay.cpython-312.pyc
│  │        │  │  │     ├─ test_short_time_fft.cpython-312.pyc
│  │        │  │  │     ├─ test_signaltools.cpython-312.pyc
│  │        │  │  │     ├─ test_spectral.cpython-312.pyc
│  │        │  │  │     ├─ test_splines.cpython-312.pyc
│  │        │  │  │     ├─ test_upfirdn.cpython-312.pyc
│  │        │  │  │     ├─ test_waveforms.cpython-312.pyc
│  │        │  │  │     ├─ test_wavelets.cpython-312.pyc
│  │        │  │  │     ├─ test_windows.cpython-312.pyc
│  │        │  │  │     ├─ _scipy_spectral_test_shim.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ waveforms.py
│  │        │  │  ├─ wavelets.py
│  │        │  │  ├─ windows
│  │        │  │  │  ├─ windows.py
│  │        │  │  │  ├─ _windows.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ windows.cpython-312.pyc
│  │        │  │  │     ├─ _windows.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _arraytools.py
│  │        │  │  ├─ _czt.py
│  │        │  │  ├─ _filter_design.py
│  │        │  │  ├─ _fir_filter_design.py
│  │        │  │  ├─ _ltisys.py
│  │        │  │  ├─ _lti_conversion.py
│  │        │  │  ├─ _max_len_seq.py
│  │        │  │  ├─ _max_len_seq_inner.cpython-312-darwin.so
│  │        │  │  ├─ _peak_finding.py
│  │        │  │  ├─ _peak_finding_utils.cpython-312-darwin.so
│  │        │  │  ├─ _savitzky_golay.py
│  │        │  │  ├─ _short_time_fft.py
│  │        │  │  ├─ _signaltools.py
│  │        │  │  ├─ _sigtools.cpython-312-darwin.so
│  │        │  │  ├─ _sosfilt.cpython-312-darwin.so
│  │        │  │  ├─ _spectral_py.py
│  │        │  │  ├─ _spline.cpython-312-darwin.so
│  │        │  │  ├─ _spline.pyi
│  │        │  │  ├─ _spline_filters.py
│  │        │  │  ├─ _upfirdn.py
│  │        │  │  ├─ _upfirdn_apply.cpython-312-darwin.so
│  │        │  │  ├─ _waveforms.py
│  │        │  │  ├─ _wavelets.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ bsplines.cpython-312.pyc
│  │        │  │     ├─ filter_design.cpython-312.pyc
│  │        │  │     ├─ fir_filter_design.cpython-312.pyc
│  │        │  │     ├─ ltisys.cpython-312.pyc
│  │        │  │     ├─ lti_conversion.cpython-312.pyc
│  │        │  │     ├─ signaltools.cpython-312.pyc
│  │        │  │     ├─ spectral.cpython-312.pyc
│  │        │  │     ├─ spline.cpython-312.pyc
│  │        │  │     ├─ waveforms.cpython-312.pyc
│  │        │  │     ├─ wavelets.cpython-312.pyc
│  │        │  │     ├─ _arraytools.cpython-312.pyc
│  │        │  │     ├─ _czt.cpython-312.pyc
│  │        │  │     ├─ _filter_design.cpython-312.pyc
│  │        │  │     ├─ _fir_filter_design.cpython-312.pyc
│  │        │  │     ├─ _ltisys.cpython-312.pyc
│  │        │  │     ├─ _lti_conversion.cpython-312.pyc
│  │        │  │     ├─ _max_len_seq.cpython-312.pyc
│  │        │  │     ├─ _peak_finding.cpython-312.pyc
│  │        │  │     ├─ _savitzky_golay.cpython-312.pyc
│  │        │  │     ├─ _short_time_fft.cpython-312.pyc
│  │        │  │     ├─ _signaltools.cpython-312.pyc
│  │        │  │     ├─ _spectral_py.cpython-312.pyc
│  │        │  │     ├─ _spline_filters.cpython-312.pyc
│  │        │  │     ├─ _upfirdn.cpython-312.pyc
│  │        │  │     ├─ _waveforms.cpython-312.pyc
│  │        │  │     ├─ _wavelets.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ sparse
│  │        │  │  ├─ base.py
│  │        │  │  ├─ bsr.py
│  │        │  │  ├─ compressed.py
│  │        │  │  ├─ construct.py
│  │        │  │  ├─ coo.py
│  │        │  │  ├─ csc.py
│  │        │  │  ├─ csgraph
│  │        │  │  │  ├─ tests
│  │        │  │  │  │  ├─ test_connected_components.py
│  │        │  │  │  │  ├─ test_conversions.py
│  │        │  │  │  │  ├─ test_flow.py
│  │        │  │  │  │  ├─ test_graph_laplacian.py
│  │        │  │  │  │  ├─ test_matching.py
│  │        │  │  │  │  ├─ test_pydata_sparse.py
│  │        │  │  │  │  ├─ test_reordering.py
│  │        │  │  │  │  ├─ test_shortest_path.py
│  │        │  │  │  │  ├─ test_spanning_tree.py
│  │        │  │  │  │  ├─ test_traversal.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_connected_components.cpython-312.pyc
│  │        │  │  │  │     ├─ test_conversions.cpython-312.pyc
│  │        │  │  │  │     ├─ test_flow.cpython-312.pyc
│  │        │  │  │  │     ├─ test_graph_laplacian.cpython-312.pyc
│  │        │  │  │  │     ├─ test_matching.cpython-312.pyc
│  │        │  │  │  │     ├─ test_pydata_sparse.cpython-312.pyc
│  │        │  │  │  │     ├─ test_reordering.cpython-312.pyc
│  │        │  │  │  │     ├─ test_shortest_path.cpython-312.pyc
│  │        │  │  │  │     ├─ test_spanning_tree.cpython-312.pyc
│  │        │  │  │  │     ├─ test_traversal.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ _flow.cpython-312-darwin.so
│  │        │  │  │  ├─ _laplacian.py
│  │        │  │  │  ├─ _matching.cpython-312-darwin.so
│  │        │  │  │  ├─ _min_spanning_tree.cpython-312-darwin.so
│  │        │  │  │  ├─ _reordering.cpython-312-darwin.so
│  │        │  │  │  ├─ _shortest_path.cpython-312-darwin.so
│  │        │  │  │  ├─ _tools.cpython-312-darwin.so
│  │        │  │  │  ├─ _traversal.cpython-312-darwin.so
│  │        │  │  │  ├─ _validation.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ _laplacian.cpython-312.pyc
│  │        │  │  │     ├─ _validation.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ csr.py
│  │        │  │  ├─ data.py
│  │        │  │  ├─ dia.py
│  │        │  │  ├─ dok.py
│  │        │  │  ├─ extract.py
│  │        │  │  ├─ lil.py
│  │        │  │  ├─ linalg
│  │        │  │  │  ├─ dsolve.py
│  │        │  │  │  ├─ eigen.py
│  │        │  │  │  ├─ interface.py
│  │        │  │  │  ├─ isolve.py
│  │        │  │  │  ├─ matfuncs.py
│  │        │  │  │  ├─ tests
│  │        │  │  │  │  ├─ propack_test_data.npz
│  │        │  │  │  │  ├─ test_expm_multiply.py
│  │        │  │  │  │  ├─ test_interface.py
│  │        │  │  │  │  ├─ test_matfuncs.py
│  │        │  │  │  │  ├─ test_norm.py
│  │        │  │  │  │  ├─ test_onenormest.py
│  │        │  │  │  │  ├─ test_propack.py
│  │        │  │  │  │  ├─ test_pydata_sparse.py
│  │        │  │  │  │  ├─ test_special_sparse_arrays.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_expm_multiply.cpython-312.pyc
│  │        │  │  │  │     ├─ test_interface.cpython-312.pyc
│  │        │  │  │  │     ├─ test_matfuncs.cpython-312.pyc
│  │        │  │  │  │     ├─ test_norm.cpython-312.pyc
│  │        │  │  │  │     ├─ test_onenormest.cpython-312.pyc
│  │        │  │  │  │     ├─ test_propack.cpython-312.pyc
│  │        │  │  │  │     ├─ test_pydata_sparse.cpython-312.pyc
│  │        │  │  │  │     ├─ test_special_sparse_arrays.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ _dsolve
│  │        │  │  │  │  ├─ linsolve.py
│  │        │  │  │  │  ├─ tests
│  │        │  │  │  │  │  ├─ test_linsolve.py
│  │        │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │     ├─ test_linsolve.cpython-312.pyc
│  │        │  │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  │  ├─ _add_newdocs.py
│  │        │  │  │  │  ├─ _superlu.cpython-312-darwin.so
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ linsolve.cpython-312.pyc
│  │        │  │  │  │     ├─ _add_newdocs.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ _eigen
│  │        │  │  │  │  ├─ arpack
│  │        │  │  │  │  │  ├─ arpack.py
│  │        │  │  │  │  │  ├─ COPYING
│  │        │  │  │  │  │  ├─ tests
│  │        │  │  │  │  │  │  ├─ test_arpack.py
│  │        │  │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │  │     ├─ test_arpack.cpython-312.pyc
│  │        │  │  │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  │  │  ├─ _arpack.cpython-312-darwin.so
│  │        │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │     ├─ arpack.cpython-312.pyc
│  │        │  │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  │  ├─ lobpcg
│  │        │  │  │  │  │  ├─ lobpcg.py
│  │        │  │  │  │  │  ├─ tests
│  │        │  │  │  │  │  │  ├─ test_lobpcg.py
│  │        │  │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │  │     ├─ test_lobpcg.cpython-312.pyc
│  │        │  │  │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │     ├─ lobpcg.cpython-312.pyc
│  │        │  │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  │  ├─ tests
│  │        │  │  │  │  │  ├─ test_svds.py
│  │        │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │     ├─ test_svds.cpython-312.pyc
│  │        │  │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  │  ├─ _svds.py
│  │        │  │  │  │  ├─ _svds_doc.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ _svds.cpython-312.pyc
│  │        │  │  │  │     ├─ _svds_doc.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ _expm_multiply.py
│  │        │  │  │  ├─ _interface.py
│  │        │  │  │  ├─ _isolve
│  │        │  │  │  │  ├─ iterative.py
│  │        │  │  │  │  ├─ lgmres.py
│  │        │  │  │  │  ├─ lsmr.py
│  │        │  │  │  │  ├─ lsqr.py
│  │        │  │  │  │  ├─ minres.py
│  │        │  │  │  │  ├─ tests
│  │        │  │  │  │  │  ├─ test_gcrotmk.py
│  │        │  │  │  │  │  ├─ test_iterative.py
│  │        │  │  │  │  │  ├─ test_lgmres.py
│  │        │  │  │  │  │  ├─ test_lsmr.py
│  │        │  │  │  │  │  ├─ test_lsqr.py
│  │        │  │  │  │  │  ├─ test_minres.py
│  │        │  │  │  │  │  ├─ test_utils.py
│  │        │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │     ├─ test_gcrotmk.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_iterative.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_lgmres.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_lsmr.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_lsqr.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_minres.cpython-312.pyc
│  │        │  │  │  │  │     ├─ test_utils.cpython-312.pyc
│  │        │  │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  │  ├─ tfqmr.py
│  │        │  │  │  │  ├─ utils.py
│  │        │  │  │  │  ├─ _gcrotmk.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ iterative.cpython-312.pyc
│  │        │  │  │  │     ├─ lgmres.cpython-312.pyc
│  │        │  │  │  │     ├─ lsmr.cpython-312.pyc
│  │        │  │  │  │     ├─ lsqr.cpython-312.pyc
│  │        │  │  │  │     ├─ minres.cpython-312.pyc
│  │        │  │  │  │     ├─ tfqmr.cpython-312.pyc
│  │        │  │  │  │     ├─ utils.cpython-312.pyc
│  │        │  │  │  │     ├─ _gcrotmk.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ _matfuncs.py
│  │        │  │  │  ├─ _norm.py
│  │        │  │  │  ├─ _onenormest.py
│  │        │  │  │  ├─ _propack
│  │        │  │  │  │  ├─ _cpropack.cpython-312-darwin.so
│  │        │  │  │  │  ├─ _dpropack.cpython-312-darwin.so
│  │        │  │  │  │  ├─ _spropack.cpython-312-darwin.so
│  │        │  │  │  │  └─ _zpropack.cpython-312-darwin.so
│  │        │  │  │  ├─ _special_sparse_arrays.py
│  │        │  │  │  ├─ _svdp.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ dsolve.cpython-312.pyc
│  │        │  │  │     ├─ eigen.cpython-312.pyc
│  │        │  │  │     ├─ interface.cpython-312.pyc
│  │        │  │  │     ├─ isolve.cpython-312.pyc
│  │        │  │  │     ├─ matfuncs.cpython-312.pyc
│  │        │  │  │     ├─ _expm_multiply.cpython-312.pyc
│  │        │  │  │     ├─ _interface.cpython-312.pyc
│  │        │  │  │     ├─ _matfuncs.cpython-312.pyc
│  │        │  │  │     ├─ _norm.cpython-312.pyc
│  │        │  │  │     ├─ _onenormest.cpython-312.pyc
│  │        │  │  │     ├─ _special_sparse_arrays.cpython-312.pyc
│  │        │  │  │     ├─ _svdp.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ sparsetools.py
│  │        │  │  ├─ spfuncs.py
│  │        │  │  ├─ sputils.py
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ data
│  │        │  │  │  │  ├─ csc_py2.npz
│  │        │  │  │  │  └─ csc_py3.npz
│  │        │  │  │  ├─ test_arithmetic1d.py
│  │        │  │  │  ├─ test_array_api.py
│  │        │  │  │  ├─ test_base.py
│  │        │  │  │  ├─ test_common1d.py
│  │        │  │  │  ├─ test_construct.py
│  │        │  │  │  ├─ test_coo.py
│  │        │  │  │  ├─ test_csc.py
│  │        │  │  │  ├─ test_csr.py
│  │        │  │  │  ├─ test_dok.py
│  │        │  │  │  ├─ test_extract.py
│  │        │  │  │  ├─ test_indexing1d.py
│  │        │  │  │  ├─ test_matrix_io.py
│  │        │  │  │  ├─ test_minmax1d.py
│  │        │  │  │  ├─ test_sparsetools.py
│  │        │  │  │  ├─ test_spfuncs.py
│  │        │  │  │  ├─ test_sputils.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_arithmetic1d.cpython-312.pyc
│  │        │  │  │     ├─ test_array_api.cpython-312.pyc
│  │        │  │  │     ├─ test_base.cpython-312.pyc
│  │        │  │  │     ├─ test_common1d.cpython-312.pyc
│  │        │  │  │     ├─ test_construct.cpython-312.pyc
│  │        │  │  │     ├─ test_coo.cpython-312.pyc
│  │        │  │  │     ├─ test_csc.cpython-312.pyc
│  │        │  │  │     ├─ test_csr.cpython-312.pyc
│  │        │  │  │     ├─ test_dok.cpython-312.pyc
│  │        │  │  │     ├─ test_extract.cpython-312.pyc
│  │        │  │  │     ├─ test_indexing1d.cpython-312.pyc
│  │        │  │  │     ├─ test_matrix_io.cpython-312.pyc
│  │        │  │  │     ├─ test_minmax1d.cpython-312.pyc
│  │        │  │  │     ├─ test_sparsetools.cpython-312.pyc
│  │        │  │  │     ├─ test_spfuncs.cpython-312.pyc
│  │        │  │  │     ├─ test_sputils.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _base.py
│  │        │  │  ├─ _bsr.py
│  │        │  │  ├─ _compressed.py
│  │        │  │  ├─ _construct.py
│  │        │  │  ├─ _coo.py
│  │        │  │  ├─ _csc.py
│  │        │  │  ├─ _csparsetools.cpython-312-darwin.so
│  │        │  │  ├─ _csr.py
│  │        │  │  ├─ _data.py
│  │        │  │  ├─ _dia.py
│  │        │  │  ├─ _dok.py
│  │        │  │  ├─ _extract.py
│  │        │  │  ├─ _index.py
│  │        │  │  ├─ _lil.py
│  │        │  │  ├─ _matrix.py
│  │        │  │  ├─ _matrix_io.py
│  │        │  │  ├─ _sparsetools.cpython-312-darwin.so
│  │        │  │  ├─ _spfuncs.py
│  │        │  │  ├─ _sputils.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ base.cpython-312.pyc
│  │        │  │     ├─ bsr.cpython-312.pyc
│  │        │  │     ├─ compressed.cpython-312.pyc
│  │        │  │     ├─ construct.cpython-312.pyc
│  │        │  │     ├─ coo.cpython-312.pyc
│  │        │  │     ├─ csc.cpython-312.pyc
│  │        │  │     ├─ csr.cpython-312.pyc
│  │        │  │     ├─ data.cpython-312.pyc
│  │        │  │     ├─ dia.cpython-312.pyc
│  │        │  │     ├─ dok.cpython-312.pyc
│  │        │  │     ├─ extract.cpython-312.pyc
│  │        │  │     ├─ lil.cpython-312.pyc
│  │        │  │     ├─ sparsetools.cpython-312.pyc
│  │        │  │     ├─ spfuncs.cpython-312.pyc
│  │        │  │     ├─ sputils.cpython-312.pyc
│  │        │  │     ├─ _base.cpython-312.pyc
│  │        │  │     ├─ _bsr.cpython-312.pyc
│  │        │  │     ├─ _compressed.cpython-312.pyc
│  │        │  │     ├─ _construct.cpython-312.pyc
│  │        │  │     ├─ _coo.cpython-312.pyc
│  │        │  │     ├─ _csc.cpython-312.pyc
│  │        │  │     ├─ _csr.cpython-312.pyc
│  │        │  │     ├─ _data.cpython-312.pyc
│  │        │  │     ├─ _dia.cpython-312.pyc
│  │        │  │     ├─ _dok.cpython-312.pyc
│  │        │  │     ├─ _extract.cpython-312.pyc
│  │        │  │     ├─ _index.cpython-312.pyc
│  │        │  │     ├─ _lil.cpython-312.pyc
│  │        │  │     ├─ _matrix.cpython-312.pyc
│  │        │  │     ├─ _matrix_io.cpython-312.pyc
│  │        │  │     ├─ _spfuncs.cpython-312.pyc
│  │        │  │     ├─ _sputils.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ spatial
│  │        │  │  ├─ ckdtree.py
│  │        │  │  ├─ distance.py
│  │        │  │  ├─ distance.pyi
│  │        │  │  ├─ kdtree.py
│  │        │  │  ├─ qhull.py
│  │        │  │  ├─ qhull_src
│  │        │  │  │  └─ COPYING.txt
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ data
│  │        │  │  │  │  ├─ cdist-X1.txt
│  │        │  │  │  │  ├─ cdist-X2.txt
│  │        │  │  │  │  ├─ degenerate_pointset.npz
│  │        │  │  │  │  ├─ iris.txt
│  │        │  │  │  │  ├─ pdist-boolean-inp.txt
│  │        │  │  │  │  ├─ pdist-chebyshev-ml-iris.txt
│  │        │  │  │  │  ├─ pdist-chebyshev-ml.txt
│  │        │  │  │  │  ├─ pdist-cityblock-ml-iris.txt
│  │        │  │  │  │  ├─ pdist-cityblock-ml.txt
│  │        │  │  │  │  ├─ pdist-correlation-ml-iris.txt
│  │        │  │  │  │  ├─ pdist-correlation-ml.txt
│  │        │  │  │  │  ├─ pdist-cosine-ml-iris.txt
│  │        │  │  │  │  ├─ pdist-cosine-ml.txt
│  │        │  │  │  │  ├─ pdist-double-inp.txt
│  │        │  │  │  │  ├─ pdist-euclidean-ml-iris.txt
│  │        │  │  │  │  ├─ pdist-euclidean-ml.txt
│  │        │  │  │  │  ├─ pdist-hamming-ml.txt
│  │        │  │  │  │  ├─ pdist-jaccard-ml.txt
│  │        │  │  │  │  ├─ pdist-jensenshannon-ml-iris.txt
│  │        │  │  │  │  ├─ pdist-jensenshannon-ml.txt
│  │        │  │  │  │  ├─ pdist-minkowski-3.2-ml-iris.txt
│  │        │  │  │  │  ├─ pdist-minkowski-3.2-ml.txt
│  │        │  │  │  │  ├─ pdist-minkowski-5.8-ml-iris.txt
│  │        │  │  │  │  ├─ pdist-seuclidean-ml-iris.txt
│  │        │  │  │  │  ├─ pdist-seuclidean-ml.txt
│  │        │  │  │  │  ├─ pdist-spearman-ml.txt
│  │        │  │  │  │  ├─ random-bool-data.txt
│  │        │  │  │  │  ├─ random-double-data.txt
│  │        │  │  │  │  ├─ random-int-data.txt
│  │        │  │  │  │  ├─ random-uint-data.txt
│  │        │  │  │  │  └─ selfdual-4d-polytope.txt
│  │        │  │  │  ├─ test_distance.py
│  │        │  │  │  ├─ test_hausdorff.py
│  │        │  │  │  ├─ test_kdtree.py
│  │        │  │  │  ├─ test_qhull.py
│  │        │  │  │  ├─ test_slerp.py
│  │        │  │  │  ├─ test_spherical_voronoi.py
│  │        │  │  │  ├─ test__plotutils.py
│  │        │  │  │  ├─ test__procrustes.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_distance.cpython-312.pyc
│  │        │  │  │     ├─ test_hausdorff.cpython-312.pyc
│  │        │  │  │     ├─ test_kdtree.cpython-312.pyc
│  │        │  │  │     ├─ test_qhull.cpython-312.pyc
│  │        │  │  │     ├─ test_slerp.cpython-312.pyc
│  │        │  │  │     ├─ test_spherical_voronoi.cpython-312.pyc
│  │        │  │  │     ├─ test__plotutils.cpython-312.pyc
│  │        │  │  │     ├─ test__procrustes.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ transform
│  │        │  │  │  ├─ rotation.py
│  │        │  │  │  ├─ tests
│  │        │  │  │  │  ├─ test_rotation.py
│  │        │  │  │  │  ├─ test_rotation_groups.py
│  │        │  │  │  │  ├─ test_rotation_spline.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_rotation.cpython-312.pyc
│  │        │  │  │  │     ├─ test_rotation_groups.cpython-312.pyc
│  │        │  │  │  │     ├─ test_rotation_spline.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ _rotation.cpython-312-darwin.so
│  │        │  │  │  ├─ _rotation_groups.py
│  │        │  │  │  ├─ _rotation_spline.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ rotation.cpython-312.pyc
│  │        │  │  │     ├─ _rotation_groups.cpython-312.pyc
│  │        │  │  │     ├─ _rotation_spline.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _ckdtree.cpython-312-darwin.so
│  │        │  │  ├─ _distance_pybind.cpython-312-darwin.so
│  │        │  │  ├─ _distance_wrap.cpython-312-darwin.so
│  │        │  │  ├─ _geometric_slerp.py
│  │        │  │  ├─ _hausdorff.cpython-312-darwin.so
│  │        │  │  ├─ _kdtree.py
│  │        │  │  ├─ _plotutils.py
│  │        │  │  ├─ _procrustes.py
│  │        │  │  ├─ _qhull.cpython-312-darwin.so
│  │        │  │  ├─ _qhull.pyi
│  │        │  │  ├─ _spherical_voronoi.py
│  │        │  │  ├─ _voronoi.cpython-312-darwin.so
│  │        │  │  ├─ _voronoi.pyi
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ ckdtree.cpython-312.pyc
│  │        │  │     ├─ distance.cpython-312.pyc
│  │        │  │     ├─ kdtree.cpython-312.pyc
│  │        │  │     ├─ qhull.cpython-312.pyc
│  │        │  │     ├─ _geometric_slerp.cpython-312.pyc
│  │        │  │     ├─ _kdtree.cpython-312.pyc
│  │        │  │     ├─ _plotutils.cpython-312.pyc
│  │        │  │     ├─ _procrustes.cpython-312.pyc
│  │        │  │     ├─ _spherical_voronoi.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ special
│  │        │  │  ├─ add_newdocs.py
│  │        │  │  ├─ basic.py
│  │        │  │  ├─ cython_special.cpython-312-darwin.so
│  │        │  │  ├─ cython_special.pxd
│  │        │  │  ├─ cython_special.pyi
│  │        │  │  ├─ libsf_error_state.dylib
│  │        │  │  ├─ orthogonal.py
│  │        │  │  ├─ sf_error.py
│  │        │  │  ├─ specfun.py
│  │        │  │  ├─ spfun_stats.py
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ data
│  │        │  │  │  │  ├─ boost.npz
│  │        │  │  │  │  ├─ gsl.npz
│  │        │  │  │  │  ├─ local.npz
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ test_basic.py
│  │        │  │  │  ├─ test_bdtr.py
│  │        │  │  │  ├─ test_boost_ufuncs.py
│  │        │  │  │  ├─ test_boxcox.py
│  │        │  │  │  ├─ test_cdflib.py
│  │        │  │  │  ├─ test_cdft_asymptotic.py
│  │        │  │  │  ├─ test_cephes_intp_cast.py
│  │        │  │  │  ├─ test_cosine_distr.py
│  │        │  │  │  ├─ test_cython_special.py
│  │        │  │  │  ├─ test_data.py
│  │        │  │  │  ├─ test_dd.py
│  │        │  │  │  ├─ test_digamma.py
│  │        │  │  │  ├─ test_ellip_harm.py
│  │        │  │  │  ├─ test_erfinv.py
│  │        │  │  │  ├─ test_exponential_integrals.py
│  │        │  │  │  ├─ test_extending.py
│  │        │  │  │  ├─ test_faddeeva.py
│  │        │  │  │  ├─ test_gamma.py
│  │        │  │  │  ├─ test_gammainc.py
│  │        │  │  │  ├─ test_hyp2f1.py
│  │        │  │  │  ├─ test_hypergeometric.py
│  │        │  │  │  ├─ test_iv_ratio.py
│  │        │  │  │  ├─ test_kolmogorov.py
│  │        │  │  │  ├─ test_lambertw.py
│  │        │  │  │  ├─ test_legendre.py
│  │        │  │  │  ├─ test_loggamma.py
│  │        │  │  │  ├─ test_logit.py
│  │        │  │  │  ├─ test_logsumexp.py
│  │        │  │  │  ├─ test_log_softmax.py
│  │        │  │  │  ├─ test_mpmath.py
│  │        │  │  │  ├─ test_nan_inputs.py
│  │        │  │  │  ├─ test_ndtr.py
│  │        │  │  │  ├─ test_ndtri_exp.py
│  │        │  │  │  ├─ test_orthogonal.py
│  │        │  │  │  ├─ test_orthogonal_eval.py
│  │        │  │  │  ├─ test_owens_t.py
│  │        │  │  │  ├─ test_pcf.py
│  │        │  │  │  ├─ test_pdtr.py
│  │        │  │  │  ├─ test_powm1.py
│  │        │  │  │  ├─ test_precompute_expn_asy.py
│  │        │  │  │  ├─ test_precompute_gammainc.py
│  │        │  │  │  ├─ test_precompute_utils.py
│  │        │  │  │  ├─ test_round.py
│  │        │  │  │  ├─ test_sf_error.py
│  │        │  │  │  ├─ test_sici.py
│  │        │  │  │  ├─ test_specfun.py
│  │        │  │  │  ├─ test_spence.py
│  │        │  │  │  ├─ test_spfun_stats.py
│  │        │  │  │  ├─ test_spherical_bessel.py
│  │        │  │  │  ├─ test_sph_harm.py
│  │        │  │  │  ├─ test_support_alternative_backends.py
│  │        │  │  │  ├─ test_trig.py
│  │        │  │  │  ├─ test_ufunc_signatures.py
│  │        │  │  │  ├─ test_wrightomega.py
│  │        │  │  │  ├─ test_wright_bessel.py
│  │        │  │  │  ├─ test_xsf_cuda.py
│  │        │  │  │  ├─ test_zeta.py
│  │        │  │  │  ├─ _cython_examples
│  │        │  │  │  │  ├─ extending.pyx
│  │        │  │  │  │  └─ meson.build
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_basic.cpython-312.pyc
│  │        │  │  │     ├─ test_bdtr.cpython-312.pyc
│  │        │  │  │     ├─ test_boost_ufuncs.cpython-312.pyc
│  │        │  │  │     ├─ test_boxcox.cpython-312.pyc
│  │        │  │  │     ├─ test_cdflib.cpython-312.pyc
│  │        │  │  │     ├─ test_cdft_asymptotic.cpython-312.pyc
│  │        │  │  │     ├─ test_cephes_intp_cast.cpython-312.pyc
│  │        │  │  │     ├─ test_cosine_distr.cpython-312.pyc
│  │        │  │  │     ├─ test_cython_special.cpython-312.pyc
│  │        │  │  │     ├─ test_data.cpython-312.pyc
│  │        │  │  │     ├─ test_dd.cpython-312.pyc
│  │        │  │  │     ├─ test_digamma.cpython-312.pyc
│  │        │  │  │     ├─ test_ellip_harm.cpython-312.pyc
│  │        │  │  │     ├─ test_erfinv.cpython-312.pyc
│  │        │  │  │     ├─ test_exponential_integrals.cpython-312.pyc
│  │        │  │  │     ├─ test_extending.cpython-312.pyc
│  │        │  │  │     ├─ test_faddeeva.cpython-312.pyc
│  │        │  │  │     ├─ test_gamma.cpython-312.pyc
│  │        │  │  │     ├─ test_gammainc.cpython-312.pyc
│  │        │  │  │     ├─ test_hyp2f1.cpython-312.pyc
│  │        │  │  │     ├─ test_hypergeometric.cpython-312.pyc
│  │        │  │  │     ├─ test_iv_ratio.cpython-312.pyc
│  │        │  │  │     ├─ test_kolmogorov.cpython-312.pyc
│  │        │  │  │     ├─ test_lambertw.cpython-312.pyc
│  │        │  │  │     ├─ test_legendre.cpython-312.pyc
│  │        │  │  │     ├─ test_loggamma.cpython-312.pyc
│  │        │  │  │     ├─ test_logit.cpython-312.pyc
│  │        │  │  │     ├─ test_logsumexp.cpython-312.pyc
│  │        │  │  │     ├─ test_log_softmax.cpython-312.pyc
│  │        │  │  │     ├─ test_mpmath.cpython-312.pyc
│  │        │  │  │     ├─ test_nan_inputs.cpython-312.pyc
│  │        │  │  │     ├─ test_ndtr.cpython-312.pyc
│  │        │  │  │     ├─ test_ndtri_exp.cpython-312.pyc
│  │        │  │  │     ├─ test_orthogonal.cpython-312.pyc
│  │        │  │  │     ├─ test_orthogonal_eval.cpython-312.pyc
│  │        │  │  │     ├─ test_owens_t.cpython-312.pyc
│  │        │  │  │     ├─ test_pcf.cpython-312.pyc
│  │        │  │  │     ├─ test_pdtr.cpython-312.pyc
│  │        │  │  │     ├─ test_powm1.cpython-312.pyc
│  │        │  │  │     ├─ test_precompute_expn_asy.cpython-312.pyc
│  │        │  │  │     ├─ test_precompute_gammainc.cpython-312.pyc
│  │        │  │  │     ├─ test_precompute_utils.cpython-312.pyc
│  │        │  │  │     ├─ test_round.cpython-312.pyc
│  │        │  │  │     ├─ test_sf_error.cpython-312.pyc
│  │        │  │  │     ├─ test_sici.cpython-312.pyc
│  │        │  │  │     ├─ test_specfun.cpython-312.pyc
│  │        │  │  │     ├─ test_spence.cpython-312.pyc
│  │        │  │  │     ├─ test_spfun_stats.cpython-312.pyc
│  │        │  │  │     ├─ test_spherical_bessel.cpython-312.pyc
│  │        │  │  │     ├─ test_sph_harm.cpython-312.pyc
│  │        │  │  │     ├─ test_support_alternative_backends.cpython-312.pyc
│  │        │  │  │     ├─ test_trig.cpython-312.pyc
│  │        │  │  │     ├─ test_ufunc_signatures.cpython-312.pyc
│  │        │  │  │     ├─ test_wrightomega.cpython-312.pyc
│  │        │  │  │     ├─ test_wright_bessel.cpython-312.pyc
│  │        │  │  │     ├─ test_xsf_cuda.cpython-312.pyc
│  │        │  │  │     ├─ test_zeta.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ xsf
│  │        │  │  │  ├─ binom.h
│  │        │  │  │  ├─ cdflib.h
│  │        │  │  │  ├─ cephes
│  │        │  │  │  │  ├─ airy.h
│  │        │  │  │  │  ├─ besselpoly.h
│  │        │  │  │  │  ├─ beta.h
│  │        │  │  │  │  ├─ cbrt.h
│  │        │  │  │  │  ├─ chbevl.h
│  │        │  │  │  │  ├─ chdtr.h
│  │        │  │  │  │  ├─ const.h
│  │        │  │  │  │  ├─ ellie.h
│  │        │  │  │  │  ├─ ellik.h
│  │        │  │  │  │  ├─ ellpe.h
│  │        │  │  │  │  ├─ ellpk.h
│  │        │  │  │  │  ├─ expn.h
│  │        │  │  │  │  ├─ gamma.h
│  │        │  │  │  │  ├─ hyp2f1.h
│  │        │  │  │  │  ├─ hyperg.h
│  │        │  │  │  │  ├─ i0.h
│  │        │  │  │  │  ├─ i1.h
│  │        │  │  │  │  ├─ igam.h
│  │        │  │  │  │  ├─ igami.h
│  │        │  │  │  │  ├─ igam_asymp_coeff.h
│  │        │  │  │  │  ├─ j0.h
│  │        │  │  │  │  ├─ j1.h
│  │        │  │  │  │  ├─ jv.h
│  │        │  │  │  │  ├─ k0.h
│  │        │  │  │  │  ├─ k1.h
│  │        │  │  │  │  ├─ kn.h
│  │        │  │  │  │  ├─ lanczos.h
│  │        │  │  │  │  ├─ ndtr.h
│  │        │  │  │  │  ├─ poch.h
│  │        │  │  │  │  ├─ polevl.h
│  │        │  │  │  │  ├─ psi.h
│  │        │  │  │  │  ├─ rgamma.h
│  │        │  │  │  │  ├─ scipy_iv.h
│  │        │  │  │  │  ├─ shichi.h
│  │        │  │  │  │  ├─ sici.h
│  │        │  │  │  │  ├─ sindg.h
│  │        │  │  │  │  ├─ tandg.h
│  │        │  │  │  │  ├─ trig.h
│  │        │  │  │  │  ├─ unity.h
│  │        │  │  │  │  └─ zeta.h
│  │        │  │  │  ├─ config.h
│  │        │  │  │  ├─ digamma.h
│  │        │  │  │  ├─ error.h
│  │        │  │  │  ├─ evalpoly.h
│  │        │  │  │  ├─ expint.h
│  │        │  │  │  ├─ hyp2f1.h
│  │        │  │  │  ├─ iv_ratio.h
│  │        │  │  │  ├─ lambertw.h
│  │        │  │  │  ├─ loggamma.h
│  │        │  │  │  ├─ sici.h
│  │        │  │  │  ├─ tools.h
│  │        │  │  │  ├─ trig.h
│  │        │  │  │  ├─ wright_bessel.h
│  │        │  │  │  └─ zlog1.h
│  │        │  │  ├─ _add_newdocs.py
│  │        │  │  ├─ _basic.py
│  │        │  │  ├─ _comb.cpython-312-darwin.so
│  │        │  │  ├─ _ellip_harm.py
│  │        │  │  ├─ _ellip_harm_2.cpython-312-darwin.so
│  │        │  │  ├─ _gufuncs.cpython-312-darwin.so
│  │        │  │  ├─ _input_validation.py
│  │        │  │  ├─ _lambertw.py
│  │        │  │  ├─ _logsumexp.py
│  │        │  │  ├─ _mptestutils.py
│  │        │  │  ├─ _multiufuncs.py
│  │        │  │  ├─ _orthogonal.py
│  │        │  │  ├─ _orthogonal.pyi
│  │        │  │  ├─ _precompute
│  │        │  │  │  ├─ cosine_cdf.py
│  │        │  │  │  ├─ expn_asy.py
│  │        │  │  │  ├─ gammainc_asy.py
│  │        │  │  │  ├─ gammainc_data.py
│  │        │  │  │  ├─ hyp2f1_data.py
│  │        │  │  │  ├─ lambertw.py
│  │        │  │  │  ├─ loggamma.py
│  │        │  │  │  ├─ struve_convergence.py
│  │        │  │  │  ├─ utils.py
│  │        │  │  │  ├─ wrightomega.py
│  │        │  │  │  ├─ wright_bessel.py
│  │        │  │  │  ├─ wright_bessel_data.py
│  │        │  │  │  ├─ zetac.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ cosine_cdf.cpython-312.pyc
│  │        │  │  │     ├─ expn_asy.cpython-312.pyc
│  │        │  │  │     ├─ gammainc_asy.cpython-312.pyc
│  │        │  │  │     ├─ gammainc_data.cpython-312.pyc
│  │        │  │  │     ├─ hyp2f1_data.cpython-312.pyc
│  │        │  │  │     ├─ lambertw.cpython-312.pyc
│  │        │  │  │     ├─ loggamma.cpython-312.pyc
│  │        │  │  │     ├─ struve_convergence.cpython-312.pyc
│  │        │  │  │     ├─ utils.cpython-312.pyc
│  │        │  │  │     ├─ wrightomega.cpython-312.pyc
│  │        │  │  │     ├─ wright_bessel.cpython-312.pyc
│  │        │  │  │     ├─ wright_bessel_data.cpython-312.pyc
│  │        │  │  │     ├─ zetac.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _sf_error.py
│  │        │  │  ├─ _specfun.cpython-312-darwin.so
│  │        │  │  ├─ _special_ufuncs.cpython-312-darwin.so
│  │        │  │  ├─ _spfun_stats.py
│  │        │  │  ├─ _spherical_bessel.py
│  │        │  │  ├─ _support_alternative_backends.py
│  │        │  │  ├─ _testutils.py
│  │        │  │  ├─ _test_internal.cpython-312-darwin.so
│  │        │  │  ├─ _test_internal.pyi
│  │        │  │  ├─ _ufuncs.cpython-312-darwin.so
│  │        │  │  ├─ _ufuncs.pyi
│  │        │  │  ├─ _ufuncs.pyx
│  │        │  │  ├─ _ufuncs_cxx.cpython-312-darwin.so
│  │        │  │  ├─ _ufuncs_cxx.pxd
│  │        │  │  ├─ _ufuncs_cxx.pyx
│  │        │  │  ├─ _ufuncs_cxx_defs.h
│  │        │  │  ├─ _ufuncs_defs.h
│  │        │  │  ├─ __init__.pxd
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ add_newdocs.cpython-312.pyc
│  │        │  │     ├─ basic.cpython-312.pyc
│  │        │  │     ├─ orthogonal.cpython-312.pyc
│  │        │  │     ├─ sf_error.cpython-312.pyc
│  │        │  │     ├─ specfun.cpython-312.pyc
│  │        │  │     ├─ spfun_stats.cpython-312.pyc
│  │        │  │     ├─ _add_newdocs.cpython-312.pyc
│  │        │  │     ├─ _basic.cpython-312.pyc
│  │        │  │     ├─ _ellip_harm.cpython-312.pyc
│  │        │  │     ├─ _input_validation.cpython-312.pyc
│  │        │  │     ├─ _lambertw.cpython-312.pyc
│  │        │  │     ├─ _logsumexp.cpython-312.pyc
│  │        │  │     ├─ _mptestutils.cpython-312.pyc
│  │        │  │     ├─ _multiufuncs.cpython-312.pyc
│  │        │  │     ├─ _orthogonal.cpython-312.pyc
│  │        │  │     ├─ _sf_error.cpython-312.pyc
│  │        │  │     ├─ _spfun_stats.cpython-312.pyc
│  │        │  │     ├─ _spherical_bessel.cpython-312.pyc
│  │        │  │     ├─ _support_alternative_backends.cpython-312.pyc
│  │        │  │     ├─ _testutils.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ stats
│  │        │  │  ├─ biasedurn.py
│  │        │  │  ├─ contingency.py
│  │        │  │  ├─ distributions.py
│  │        │  │  ├─ kde.py
│  │        │  │  ├─ morestats.py
│  │        │  │  ├─ mstats.py
│  │        │  │  ├─ mstats_basic.py
│  │        │  │  ├─ mstats_extras.py
│  │        │  │  ├─ mvn.py
│  │        │  │  ├─ qmc.py
│  │        │  │  ├─ sampling.py
│  │        │  │  ├─ stats.py
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ common_tests.py
│  │        │  │  │  ├─ data
│  │        │  │  │  │  ├─ fisher_exact_results_from_r.py
│  │        │  │  │  │  ├─ jf_skew_t_gamlss_pdf_data.npy
│  │        │  │  │  │  ├─ levy_stable
│  │        │  │  │  │  │  ├─ stable-loc-scale-sample-data.npy
│  │        │  │  │  │  │  ├─ stable-Z1-cdf-sample-data.npy
│  │        │  │  │  │  │  └─ stable-Z1-pdf-sample-data.npy
│  │        │  │  │  │  ├─ nist_anova
│  │        │  │  │  │  │  ├─ AtmWtAg.dat
│  │        │  │  │  │  │  ├─ SiRstv.dat
│  │        │  │  │  │  │  ├─ SmLs01.dat
│  │        │  │  │  │  │  ├─ SmLs02.dat
│  │        │  │  │  │  │  ├─ SmLs03.dat
│  │        │  │  │  │  │  ├─ SmLs04.dat
│  │        │  │  │  │  │  ├─ SmLs05.dat
│  │        │  │  │  │  │  ├─ SmLs06.dat
│  │        │  │  │  │  │  ├─ SmLs07.dat
│  │        │  │  │  │  │  ├─ SmLs08.dat
│  │        │  │  │  │  │  └─ SmLs09.dat
│  │        │  │  │  │  ├─ nist_linregress
│  │        │  │  │  │  │  └─ Norris.dat
│  │        │  │  │  │  ├─ rel_breitwigner_pdf_sample_data_ROOT.npy
│  │        │  │  │  │  ├─ studentized_range_mpmath_ref.json
│  │        │  │  │  │  ├─ _mvt.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ fisher_exact_results_from_r.cpython-312.pyc
│  │        │  │  │  │     └─ _mvt.cpython-312.pyc
│  │        │  │  │  ├─ test_axis_nan_policy.py
│  │        │  │  │  ├─ test_binned_statistic.py
│  │        │  │  │  ├─ test_censored_data.py
│  │        │  │  │  ├─ test_contingency.py
│  │        │  │  │  ├─ test_continuous.py
│  │        │  │  │  ├─ test_continuous_basic.py
│  │        │  │  │  ├─ test_continuous_fit_censored.py
│  │        │  │  │  ├─ test_correlation.py
│  │        │  │  │  ├─ test_crosstab.py
│  │        │  │  │  ├─ test_discrete_basic.py
│  │        │  │  │  ├─ test_discrete_distns.py
│  │        │  │  │  ├─ test_distributions.py
│  │        │  │  │  ├─ test_entropy.py
│  │        │  │  │  ├─ test_fast_gen_inversion.py
│  │        │  │  │  ├─ test_fit.py
│  │        │  │  │  ├─ test_hypotests.py
│  │        │  │  │  ├─ test_kdeoth.py
│  │        │  │  │  ├─ test_mgc.py
│  │        │  │  │  ├─ test_morestats.py
│  │        │  │  │  ├─ test_mstats_basic.py
│  │        │  │  │  ├─ test_mstats_extras.py
│  │        │  │  │  ├─ test_multicomp.py
│  │        │  │  │  ├─ test_multivariate.py
│  │        │  │  │  ├─ test_odds_ratio.py
│  │        │  │  │  ├─ test_qmc.py
│  │        │  │  │  ├─ test_rank.py
│  │        │  │  │  ├─ test_relative_risk.py
│  │        │  │  │  ├─ test_resampling.py
│  │        │  │  │  ├─ test_sampling.py
│  │        │  │  │  ├─ test_sensitivity_analysis.py
│  │        │  │  │  ├─ test_stats.py
│  │        │  │  │  ├─ test_survival.py
│  │        │  │  │  ├─ test_tukeylambda_stats.py
│  │        │  │  │  ├─ test_variation.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ common_tests.cpython-312.pyc
│  │        │  │  │     ├─ test_axis_nan_policy.cpython-312.pyc
│  │        │  │  │     ├─ test_binned_statistic.cpython-312.pyc
│  │        │  │  │     ├─ test_censored_data.cpython-312.pyc
│  │        │  │  │     ├─ test_contingency.cpython-312.pyc
│  │        │  │  │     ├─ test_continuous.cpython-312.pyc
│  │        │  │  │     ├─ test_continuous_basic.cpython-312.pyc
│  │        │  │  │     ├─ test_continuous_fit_censored.cpython-312.pyc
│  │        │  │  │     ├─ test_correlation.cpython-312.pyc
│  │        │  │  │     ├─ test_crosstab.cpython-312.pyc
│  │        │  │  │     ├─ test_discrete_basic.cpython-312.pyc
│  │        │  │  │     ├─ test_discrete_distns.cpython-312.pyc
│  │        │  │  │     ├─ test_distributions.cpython-312.pyc
│  │        │  │  │     ├─ test_entropy.cpython-312.pyc
│  │        │  │  │     ├─ test_fast_gen_inversion.cpython-312.pyc
│  │        │  │  │     ├─ test_fit.cpython-312.pyc
│  │        │  │  │     ├─ test_hypotests.cpython-312.pyc
│  │        │  │  │     ├─ test_kdeoth.cpython-312.pyc
│  │        │  │  │     ├─ test_mgc.cpython-312.pyc
│  │        │  │  │     ├─ test_morestats.cpython-312.pyc
│  │        │  │  │     ├─ test_mstats_basic.cpython-312.pyc
│  │        │  │  │     ├─ test_mstats_extras.cpython-312.pyc
│  │        │  │  │     ├─ test_multicomp.cpython-312.pyc
│  │        │  │  │     ├─ test_multivariate.cpython-312.pyc
│  │        │  │  │     ├─ test_odds_ratio.cpython-312.pyc
│  │        │  │  │     ├─ test_qmc.cpython-312.pyc
│  │        │  │  │     ├─ test_rank.cpython-312.pyc
│  │        │  │  │     ├─ test_relative_risk.cpython-312.pyc
│  │        │  │  │     ├─ test_resampling.cpython-312.pyc
│  │        │  │  │     ├─ test_sampling.cpython-312.pyc
│  │        │  │  │     ├─ test_sensitivity_analysis.cpython-312.pyc
│  │        │  │  │     ├─ test_stats.cpython-312.pyc
│  │        │  │  │     ├─ test_survival.cpython-312.pyc
│  │        │  │  │     ├─ test_tukeylambda_stats.cpython-312.pyc
│  │        │  │  │     ├─ test_variation.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _ansari_swilk_statistics.cpython-312-darwin.so
│  │        │  │  ├─ _axis_nan_policy.py
│  │        │  │  ├─ _biasedurn.cpython-312-darwin.so
│  │        │  │  ├─ _biasedurn.pxd
│  │        │  │  ├─ _binned_statistic.py
│  │        │  │  ├─ _binomtest.py
│  │        │  │  ├─ _bws_test.py
│  │        │  │  ├─ _censored_data.py
│  │        │  │  ├─ _common.py
│  │        │  │  ├─ _constants.py
│  │        │  │  ├─ _continuous_distns.py
│  │        │  │  ├─ _correlation.py
│  │        │  │  ├─ _covariance.py
│  │        │  │  ├─ _crosstab.py
│  │        │  │  ├─ _discrete_distns.py
│  │        │  │  ├─ _distn_infrastructure.py
│  │        │  │  ├─ _distribution_infrastructure.py
│  │        │  │  ├─ _distr_params.py
│  │        │  │  ├─ _entropy.py
│  │        │  │  ├─ _fit.py
│  │        │  │  ├─ _hypotests.py
│  │        │  │  ├─ _kde.py
│  │        │  │  ├─ _ksstats.py
│  │        │  │  ├─ _levy_stable
│  │        │  │  │  ├─ levyst.cpython-312-darwin.so
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _mannwhitneyu.py
│  │        │  │  ├─ _mgc.py
│  │        │  │  ├─ _morestats.py
│  │        │  │  ├─ _mstats_basic.py
│  │        │  │  ├─ _mstats_extras.py
│  │        │  │  ├─ _multicomp.py
│  │        │  │  ├─ _multivariate.py
│  │        │  │  ├─ _mvn.cpython-312-darwin.so
│  │        │  │  ├─ _new_distributions.py
│  │        │  │  ├─ _odds_ratio.py
│  │        │  │  ├─ _page_trend_test.py
│  │        │  │  ├─ _probability_distribution.py
│  │        │  │  ├─ _qmc.py
│  │        │  │  ├─ _qmc_cy.cpython-312-darwin.so
│  │        │  │  ├─ _qmc_cy.pyi
│  │        │  │  ├─ _qmvnt.py
│  │        │  │  ├─ _rcont
│  │        │  │  │  ├─ rcont.cpython-312-darwin.so
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _relative_risk.py
│  │        │  │  ├─ _resampling.py
│  │        │  │  ├─ _result_classes.py
│  │        │  │  ├─ _sampling.py
│  │        │  │  ├─ _sensitivity_analysis.py
│  │        │  │  ├─ _sobol.cpython-312-darwin.so
│  │        │  │  ├─ _sobol.pyi
│  │        │  │  ├─ _sobol_direction_numbers.npz
│  │        │  │  ├─ _stats.cpython-312-darwin.so
│  │        │  │  ├─ _stats.pxd
│  │        │  │  ├─ _stats_mstats_common.py
│  │        │  │  ├─ _stats_py.py
│  │        │  │  ├─ _stats_pythran.cpython-312-darwin.so
│  │        │  │  ├─ _survival.py
│  │        │  │  ├─ _tukeylambda_stats.py
│  │        │  │  ├─ _unuran
│  │        │  │  │  ├─ unuran_wrapper.cpython-312-darwin.so
│  │        │  │  │  ├─ unuran_wrapper.pyi
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _variation.py
│  │        │  │  ├─ _warnings_errors.py
│  │        │  │  ├─ _wilcoxon.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ biasedurn.cpython-312.pyc
│  │        │  │     ├─ contingency.cpython-312.pyc
│  │        │  │     ├─ distributions.cpython-312.pyc
│  │        │  │     ├─ kde.cpython-312.pyc
│  │        │  │     ├─ morestats.cpython-312.pyc
│  │        │  │     ├─ mstats.cpython-312.pyc
│  │        │  │     ├─ mstats_basic.cpython-312.pyc
│  │        │  │     ├─ mstats_extras.cpython-312.pyc
│  │        │  │     ├─ mvn.cpython-312.pyc
│  │        │  │     ├─ qmc.cpython-312.pyc
│  │        │  │     ├─ sampling.cpython-312.pyc
│  │        │  │     ├─ stats.cpython-312.pyc
│  │        │  │     ├─ _axis_nan_policy.cpython-312.pyc
│  │        │  │     ├─ _binned_statistic.cpython-312.pyc
│  │        │  │     ├─ _binomtest.cpython-312.pyc
│  │        │  │     ├─ _bws_test.cpython-312.pyc
│  │        │  │     ├─ _censored_data.cpython-312.pyc
│  │        │  │     ├─ _common.cpython-312.pyc
│  │        │  │     ├─ _constants.cpython-312.pyc
│  │        │  │     ├─ _continuous_distns.cpython-312.pyc
│  │        │  │     ├─ _correlation.cpython-312.pyc
│  │        │  │     ├─ _covariance.cpython-312.pyc
│  │        │  │     ├─ _crosstab.cpython-312.pyc
│  │        │  │     ├─ _discrete_distns.cpython-312.pyc
│  │        │  │     ├─ _distn_infrastructure.cpython-312.pyc
│  │        │  │     ├─ _distribution_infrastructure.cpython-312.pyc
│  │        │  │     ├─ _distr_params.cpython-312.pyc
│  │        │  │     ├─ _entropy.cpython-312.pyc
│  │        │  │     ├─ _fit.cpython-312.pyc
│  │        │  │     ├─ _hypotests.cpython-312.pyc
│  │        │  │     ├─ _kde.cpython-312.pyc
│  │        │  │     ├─ _ksstats.cpython-312.pyc
│  │        │  │     ├─ _mannwhitneyu.cpython-312.pyc
│  │        │  │     ├─ _mgc.cpython-312.pyc
│  │        │  │     ├─ _morestats.cpython-312.pyc
│  │        │  │     ├─ _mstats_basic.cpython-312.pyc
│  │        │  │     ├─ _mstats_extras.cpython-312.pyc
│  │        │  │     ├─ _multicomp.cpython-312.pyc
│  │        │  │     ├─ _multivariate.cpython-312.pyc
│  │        │  │     ├─ _new_distributions.cpython-312.pyc
│  │        │  │     ├─ _odds_ratio.cpython-312.pyc
│  │        │  │     ├─ _page_trend_test.cpython-312.pyc
│  │        │  │     ├─ _probability_distribution.cpython-312.pyc
│  │        │  │     ├─ _qmc.cpython-312.pyc
│  │        │  │     ├─ _qmvnt.cpython-312.pyc
│  │        │  │     ├─ _relative_risk.cpython-312.pyc
│  │        │  │     ├─ _resampling.cpython-312.pyc
│  │        │  │     ├─ _result_classes.cpython-312.pyc
│  │        │  │     ├─ _sampling.cpython-312.pyc
│  │        │  │     ├─ _sensitivity_analysis.cpython-312.pyc
│  │        │  │     ├─ _stats_mstats_common.cpython-312.pyc
│  │        │  │     ├─ _stats_py.cpython-312.pyc
│  │        │  │     ├─ _survival.cpython-312.pyc
│  │        │  │     ├─ _tukeylambda_stats.cpython-312.pyc
│  │        │  │     ├─ _variation.cpython-312.pyc
│  │        │  │     ├─ _warnings_errors.cpython-312.pyc
│  │        │  │     ├─ _wilcoxon.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ version.py
│  │        │  ├─ _distributor_init.py
│  │        │  ├─ _lib
│  │        │  │  ├─ array_api_compat
│  │        │  │  │  ├─ common
│  │        │  │  │  │  ├─ _aliases.py
│  │        │  │  │  │  ├─ _fft.py
│  │        │  │  │  │  ├─ _helpers.py
│  │        │  │  │  │  ├─ _linalg.py
│  │        │  │  │  │  ├─ _typing.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ _aliases.cpython-312.pyc
│  │        │  │  │  │     ├─ _fft.cpython-312.pyc
│  │        │  │  │  │     ├─ _helpers.cpython-312.pyc
│  │        │  │  │  │     ├─ _linalg.cpython-312.pyc
│  │        │  │  │  │     ├─ _typing.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ cupy
│  │        │  │  │  │  ├─ fft.py
│  │        │  │  │  │  ├─ linalg.py
│  │        │  │  │  │  ├─ _aliases.py
│  │        │  │  │  │  ├─ _info.py
│  │        │  │  │  │  ├─ _typing.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ fft.cpython-312.pyc
│  │        │  │  │  │     ├─ linalg.cpython-312.pyc
│  │        │  │  │  │     ├─ _aliases.cpython-312.pyc
│  │        │  │  │  │     ├─ _info.cpython-312.pyc
│  │        │  │  │  │     ├─ _typing.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ dask
│  │        │  │  │  │  ├─ array
│  │        │  │  │  │  │  ├─ fft.py
│  │        │  │  │  │  │  ├─ linalg.py
│  │        │  │  │  │  │  ├─ _aliases.py
│  │        │  │  │  │  │  ├─ _info.py
│  │        │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │     ├─ fft.cpython-312.pyc
│  │        │  │  │  │  │     ├─ linalg.cpython-312.pyc
│  │        │  │  │  │  │     ├─ _aliases.cpython-312.pyc
│  │        │  │  │  │  │     ├─ _info.cpython-312.pyc
│  │        │  │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ numpy
│  │        │  │  │  │  ├─ fft.py
│  │        │  │  │  │  ├─ linalg.py
│  │        │  │  │  │  ├─ _aliases.py
│  │        │  │  │  │  ├─ _info.py
│  │        │  │  │  │  ├─ _typing.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ fft.cpython-312.pyc
│  │        │  │  │  │     ├─ linalg.cpython-312.pyc
│  │        │  │  │  │     ├─ _aliases.cpython-312.pyc
│  │        │  │  │  │     ├─ _info.cpython-312.pyc
│  │        │  │  │  │     ├─ _typing.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ torch
│  │        │  │  │  │  ├─ fft.py
│  │        │  │  │  │  ├─ linalg.py
│  │        │  │  │  │  ├─ _aliases.py
│  │        │  │  │  │  ├─ _info.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ fft.cpython-312.pyc
│  │        │  │  │  │     ├─ linalg.cpython-312.pyc
│  │        │  │  │  │     ├─ _aliases.cpython-312.pyc
│  │        │  │  │  │     ├─ _info.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ _internal.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ _internal.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ array_api_extra
│  │        │  │  │  ├─ _funcs.py
│  │        │  │  │  ├─ _typing.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ _funcs.cpython-312.pyc
│  │        │  │  │     ├─ _typing.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ cobyqa
│  │        │  │  │  ├─ framework.py
│  │        │  │  │  ├─ main.py
│  │        │  │  │  ├─ models.py
│  │        │  │  │  ├─ problem.py
│  │        │  │  │  ├─ settings.py
│  │        │  │  │  ├─ subsolvers
│  │        │  │  │  │  ├─ geometry.py
│  │        │  │  │  │  ├─ optim.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ geometry.cpython-312.pyc
│  │        │  │  │  │     ├─ optim.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ utils
│  │        │  │  │  │  ├─ exceptions.py
│  │        │  │  │  │  ├─ math.py
│  │        │  │  │  │  ├─ versions.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ exceptions.cpython-312.pyc
│  │        │  │  │  │     ├─ math.cpython-312.pyc
│  │        │  │  │  │     ├─ versions.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ framework.cpython-312.pyc
│  │        │  │  │     ├─ main.cpython-312.pyc
│  │        │  │  │     ├─ models.cpython-312.pyc
│  │        │  │  │     ├─ problem.cpython-312.pyc
│  │        │  │  │     ├─ settings.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ decorator.py
│  │        │  │  ├─ deprecation.py
│  │        │  │  ├─ doccer.py
│  │        │  │  ├─ messagestream.cpython-312-darwin.so
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ test_array_api.py
│  │        │  │  │  ├─ test_bunch.py
│  │        │  │  │  ├─ test_ccallback.py
│  │        │  │  │  ├─ test_config.py
│  │        │  │  │  ├─ test_deprecation.py
│  │        │  │  │  ├─ test_doccer.py
│  │        │  │  │  ├─ test_import_cycles.py
│  │        │  │  │  ├─ test_public_api.py
│  │        │  │  │  ├─ test_scipy_version.py
│  │        │  │  │  ├─ test_tmpdirs.py
│  │        │  │  │  ├─ test_warnings.py
│  │        │  │  │  ├─ test__gcutils.py
│  │        │  │  │  ├─ test__pep440.py
│  │        │  │  │  ├─ test__testutils.py
│  │        │  │  │  ├─ test__threadsafety.py
│  │        │  │  │  ├─ test__util.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_array_api.cpython-312.pyc
│  │        │  │  │     ├─ test_bunch.cpython-312.pyc
│  │        │  │  │     ├─ test_ccallback.cpython-312.pyc
│  │        │  │  │     ├─ test_config.cpython-312.pyc
│  │        │  │  │     ├─ test_deprecation.cpython-312.pyc
│  │        │  │  │     ├─ test_doccer.cpython-312.pyc
│  │        │  │  │     ├─ test_import_cycles.cpython-312.pyc
│  │        │  │  │     ├─ test_public_api.cpython-312.pyc
│  │        │  │  │     ├─ test_scipy_version.cpython-312.pyc
│  │        │  │  │     ├─ test_tmpdirs.cpython-312.pyc
│  │        │  │  │     ├─ test_warnings.cpython-312.pyc
│  │        │  │  │     ├─ test__gcutils.cpython-312.pyc
│  │        │  │  │     ├─ test__pep440.cpython-312.pyc
│  │        │  │  │     ├─ test__testutils.cpython-312.pyc
│  │        │  │  │     ├─ test__threadsafety.cpython-312.pyc
│  │        │  │  │     ├─ test__util.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ uarray.py
│  │        │  │  ├─ _array_api.py
│  │        │  │  ├─ _array_api_no_0d.py
│  │        │  │  ├─ _bunch.py
│  │        │  │  ├─ _ccallback.py
│  │        │  │  ├─ _ccallback_c.cpython-312-darwin.so
│  │        │  │  ├─ _disjoint_set.py
│  │        │  │  ├─ _docscrape.py
│  │        │  │  ├─ _elementwise_iterative_method.py
│  │        │  │  ├─ _finite_differences.py
│  │        │  │  ├─ _fpumode.cpython-312-darwin.so
│  │        │  │  ├─ _gcutils.py
│  │        │  │  ├─ _pep440.py
│  │        │  │  ├─ _testutils.py
│  │        │  │  ├─ _test_ccallback.cpython-312-darwin.so
│  │        │  │  ├─ _test_deprecation_call.cpython-312-darwin.so
│  │        │  │  ├─ _test_deprecation_def.cpython-312-darwin.so
│  │        │  │  ├─ _threadsafety.py
│  │        │  │  ├─ _tmpdirs.py
│  │        │  │  ├─ _uarray
│  │        │  │  │  ├─ LICENSE
│  │        │  │  │  ├─ _backend.py
│  │        │  │  │  ├─ _uarray.cpython-312-darwin.so
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ _backend.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _util.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ decorator.cpython-312.pyc
│  │        │  │     ├─ deprecation.cpython-312.pyc
│  │        │  │     ├─ doccer.cpython-312.pyc
│  │        │  │     ├─ uarray.cpython-312.pyc
│  │        │  │     ├─ _array_api.cpython-312.pyc
│  │        │  │     ├─ _array_api_no_0d.cpython-312.pyc
│  │        │  │     ├─ _bunch.cpython-312.pyc
│  │        │  │     ├─ _ccallback.cpython-312.pyc
│  │        │  │     ├─ _disjoint_set.cpython-312.pyc
│  │        │  │     ├─ _docscrape.cpython-312.pyc
│  │        │  │     ├─ _elementwise_iterative_method.cpython-312.pyc
│  │        │  │     ├─ _finite_differences.cpython-312.pyc
│  │        │  │     ├─ _gcutils.cpython-312.pyc
│  │        │  │     ├─ _pep440.cpython-312.pyc
│  │        │  │     ├─ _testutils.cpython-312.pyc
│  │        │  │     ├─ _threadsafety.cpython-312.pyc
│  │        │  │     ├─ _tmpdirs.cpython-312.pyc
│  │        │  │     ├─ _util.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ __config__.py
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     ├─ conftest.cpython-312.pyc
│  │        │     ├─ version.cpython-312.pyc
│  │        │     ├─ _distributor_init.cpython-312.pyc
│  │        │     ├─ __config__.cpython-312.pyc
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ scipy-1.15.3.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE.txt
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  └─ WHEEL
│  │        ├─ shellingham
│  │        │  ├─ nt.py
│  │        │  ├─ posix
│  │        │  │  ├─ proc.py
│  │        │  │  ├─ ps.py
│  │        │  │  ├─ _core.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ proc.cpython-312.pyc
│  │        │  │     ├─ ps.cpython-312.pyc
│  │        │  │     ├─ _core.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ _core.py
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     ├─ nt.cpython-312.pyc
│  │        │     ├─ _core.cpython-312.pyc
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ shellingham-1.5.4.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ top_level.txt
│  │        │  ├─ WHEEL
│  │        │  └─ zip-safe
│  │        ├─ six-1.17.0.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ top_level.txt
│  │        │  └─ WHEEL
│  │        ├─ six.py
│  │        ├─ sklearn
│  │        │  ├─ .dylibs
│  │        │  │  └─ libomp.dylib
│  │        │  ├─ base.py
│  │        │  ├─ calibration.py
│  │        │  ├─ cluster
│  │        │  │  ├─ meson.build
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ common.py
│  │        │  │  │  ├─ test_affinity_propagation.py
│  │        │  │  │  ├─ test_bicluster.py
│  │        │  │  │  ├─ test_birch.py
│  │        │  │  │  ├─ test_bisect_k_means.py
│  │        │  │  │  ├─ test_dbscan.py
│  │        │  │  │  ├─ test_feature_agglomeration.py
│  │        │  │  │  ├─ test_hdbscan.py
│  │        │  │  │  ├─ test_hierarchical.py
│  │        │  │  │  ├─ test_k_means.py
│  │        │  │  │  ├─ test_mean_shift.py
│  │        │  │  │  ├─ test_optics.py
│  │        │  │  │  ├─ test_spectral.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ common.cpython-312.pyc
│  │        │  │  │     ├─ test_affinity_propagation.cpython-312.pyc
│  │        │  │  │     ├─ test_bicluster.cpython-312.pyc
│  │        │  │  │     ├─ test_birch.cpython-312.pyc
│  │        │  │  │     ├─ test_bisect_k_means.cpython-312.pyc
│  │        │  │  │     ├─ test_dbscan.cpython-312.pyc
│  │        │  │  │     ├─ test_feature_agglomeration.cpython-312.pyc
│  │        │  │  │     ├─ test_hdbscan.cpython-312.pyc
│  │        │  │  │     ├─ test_hierarchical.cpython-312.pyc
│  │        │  │  │     ├─ test_k_means.cpython-312.pyc
│  │        │  │  │     ├─ test_mean_shift.cpython-312.pyc
│  │        │  │  │     ├─ test_optics.cpython-312.pyc
│  │        │  │  │     ├─ test_spectral.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _affinity_propagation.py
│  │        │  │  ├─ _agglomerative.py
│  │        │  │  ├─ _bicluster.py
│  │        │  │  ├─ _birch.py
│  │        │  │  ├─ _bisect_k_means.py
│  │        │  │  ├─ _dbscan.py
│  │        │  │  ├─ _dbscan_inner.cpython-312-darwin.so
│  │        │  │  ├─ _dbscan_inner.pyx
│  │        │  │  ├─ _feature_agglomeration.py
│  │        │  │  ├─ _hdbscan
│  │        │  │  │  ├─ hdbscan.py
│  │        │  │  │  ├─ meson.build
│  │        │  │  │  ├─ tests
│  │        │  │  │  │  ├─ test_reachibility.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_reachibility.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ _linkage.cpython-312-darwin.so
│  │        │  │  │  ├─ _linkage.pyx
│  │        │  │  │  ├─ _reachability.cpython-312-darwin.so
│  │        │  │  │  ├─ _reachability.pyx
│  │        │  │  │  ├─ _tree.cpython-312-darwin.so
│  │        │  │  │  ├─ _tree.pxd
│  │        │  │  │  ├─ _tree.pyx
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ hdbscan.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _hierarchical_fast.cpython-312-darwin.so
│  │        │  │  ├─ _hierarchical_fast.pxd
│  │        │  │  ├─ _hierarchical_fast.pyx
│  │        │  │  ├─ _kmeans.py
│  │        │  │  ├─ _k_means_common.cpython-312-darwin.so
│  │        │  │  ├─ _k_means_common.pxd
│  │        │  │  ├─ _k_means_common.pyx
│  │        │  │  ├─ _k_means_elkan.cpython-312-darwin.so
│  │        │  │  ├─ _k_means_elkan.pyx
│  │        │  │  ├─ _k_means_lloyd.cpython-312-darwin.so
│  │        │  │  ├─ _k_means_lloyd.pyx
│  │        │  │  ├─ _k_means_minibatch.cpython-312-darwin.so
│  │        │  │  ├─ _k_means_minibatch.pyx
│  │        │  │  ├─ _mean_shift.py
│  │        │  │  ├─ _optics.py
│  │        │  │  ├─ _spectral.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ _affinity_propagation.cpython-312.pyc
│  │        │  │     ├─ _agglomerative.cpython-312.pyc
│  │        │  │     ├─ _bicluster.cpython-312.pyc
│  │        │  │     ├─ _birch.cpython-312.pyc
│  │        │  │     ├─ _bisect_k_means.cpython-312.pyc
│  │        │  │     ├─ _dbscan.cpython-312.pyc
│  │        │  │     ├─ _feature_agglomeration.cpython-312.pyc
│  │        │  │     ├─ _kmeans.cpython-312.pyc
│  │        │  │     ├─ _mean_shift.cpython-312.pyc
│  │        │  │     ├─ _optics.cpython-312.pyc
│  │        │  │     ├─ _spectral.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ compose
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ test_column_transformer.py
│  │        │  │  │  ├─ test_target.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_column_transformer.cpython-312.pyc
│  │        │  │  │     ├─ test_target.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _column_transformer.py
│  │        │  │  ├─ _target.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ _column_transformer.cpython-312.pyc
│  │        │  │     ├─ _target.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ conftest.py
│  │        │  ├─ covariance
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ test_covariance.py
│  │        │  │  │  ├─ test_elliptic_envelope.py
│  │        │  │  │  ├─ test_graphical_lasso.py
│  │        │  │  │  ├─ test_robust_covariance.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_covariance.cpython-312.pyc
│  │        │  │  │     ├─ test_elliptic_envelope.cpython-312.pyc
│  │        │  │  │     ├─ test_graphical_lasso.cpython-312.pyc
│  │        │  │  │     ├─ test_robust_covariance.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _elliptic_envelope.py
│  │        │  │  ├─ _empirical_covariance.py
│  │        │  │  ├─ _graph_lasso.py
│  │        │  │  ├─ _robust_covariance.py
│  │        │  │  ├─ _shrunk_covariance.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ _elliptic_envelope.cpython-312.pyc
│  │        │  │     ├─ _empirical_covariance.cpython-312.pyc
│  │        │  │     ├─ _graph_lasso.cpython-312.pyc
│  │        │  │     ├─ _robust_covariance.cpython-312.pyc
│  │        │  │     ├─ _shrunk_covariance.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ cross_decomposition
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ test_pls.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_pls.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _pls.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ _pls.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ datasets
│  │        │  │  ├─ data
│  │        │  │  │  ├─ breast_cancer.csv
│  │        │  │  │  ├─ diabetes_data_raw.csv.gz
│  │        │  │  │  ├─ diabetes_target.csv.gz
│  │        │  │  │  ├─ digits.csv.gz
│  │        │  │  │  ├─ iris.csv
│  │        │  │  │  ├─ linnerud_exercise.csv
│  │        │  │  │  ├─ linnerud_physiological.csv
│  │        │  │  │  ├─ wine_data.csv
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ descr
│  │        │  │  │  ├─ breast_cancer.rst
│  │        │  │  │  ├─ california_housing.rst
│  │        │  │  │  ├─ covtype.rst
│  │        │  │  │  ├─ diabetes.rst
│  │        │  │  │  ├─ digits.rst
│  │        │  │  │  ├─ iris.rst
│  │        │  │  │  ├─ kddcup99.rst
│  │        │  │  │  ├─ lfw.rst
│  │        │  │  │  ├─ linnerud.rst
│  │        │  │  │  ├─ olivetti_faces.rst
│  │        │  │  │  ├─ rcv1.rst
│  │        │  │  │  ├─ species_distributions.rst
│  │        │  │  │  ├─ twenty_newsgroups.rst
│  │        │  │  │  ├─ wine_data.rst
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ images
│  │        │  │  │  ├─ china.jpg
│  │        │  │  │  ├─ flower.jpg
│  │        │  │  │  ├─ README.txt
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ meson.build
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ data
│  │        │  │  │  │  ├─ openml
│  │        │  │  │  │  │  ├─ id_1
│  │        │  │  │  │  │  │  ├─ api-v1-jd-1.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdf-1.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdq-1.json.gz
│  │        │  │  │  │  │  │  ├─ data-v1-dl-1.arff.gz
│  │        │  │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  │  │  ├─ id_1119
│  │        │  │  │  │  │  │  ├─ api-v1-jd-1119.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdf-1119.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdl-dn-adult-census-l-2-dv-1.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdl-dn-adult-census-l-2-s-act-.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdq-1119.json.gz
│  │        │  │  │  │  │  │  ├─ data-v1-dl-54002.arff.gz
│  │        │  │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  │  │  ├─ id_1590
│  │        │  │  │  │  │  │  ├─ api-v1-jd-1590.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdf-1590.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdq-1590.json.gz
│  │        │  │  │  │  │  │  ├─ data-v1-dl-1595261.arff.gz
│  │        │  │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  │  │  ├─ id_2
│  │        │  │  │  │  │  │  ├─ api-v1-jd-2.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdf-2.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdl-dn-anneal-l-2-dv-1.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdl-dn-anneal-l-2-s-act-.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdq-2.json.gz
│  │        │  │  │  │  │  │  ├─ data-v1-dl-1666876.arff.gz
│  │        │  │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  │  │  ├─ id_292
│  │        │  │  │  │  │  │  ├─ api-v1-jd-292.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jd-40981.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdf-292.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdf-40981.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdl-dn-australian-l-2-dv-1-s-dact.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdl-dn-australian-l-2-dv-1.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdl-dn-australian-l-2-s-act-.json.gz
│  │        │  │  │  │  │  │  ├─ data-v1-dl-49822.arff.gz
│  │        │  │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  │  │  ├─ id_3
│  │        │  │  │  │  │  │  ├─ api-v1-jd-3.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdf-3.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdq-3.json.gz
│  │        │  │  │  │  │  │  ├─ data-v1-dl-3.arff.gz
│  │        │  │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  │  │  ├─ id_40589
│  │        │  │  │  │  │  │  ├─ api-v1-jd-40589.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdf-40589.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdl-dn-emotions-l-2-dv-3.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdl-dn-emotions-l-2-s-act-.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdq-40589.json.gz
│  │        │  │  │  │  │  │  ├─ data-v1-dl-4644182.arff.gz
│  │        │  │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  │  │  ├─ id_40675
│  │        │  │  │  │  │  │  ├─ api-v1-jd-40675.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdf-40675.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdl-dn-glass2-l-2-dv-1-s-dact.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdl-dn-glass2-l-2-dv-1.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdl-dn-glass2-l-2-s-act-.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdq-40675.json.gz
│  │        │  │  │  │  │  │  ├─ data-v1-dl-4965250.arff.gz
│  │        │  │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  │  │  ├─ id_40945
│  │        │  │  │  │  │  │  ├─ api-v1-jd-40945.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdf-40945.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdq-40945.json.gz
│  │        │  │  │  │  │  │  ├─ data-v1-dl-16826755.arff.gz
│  │        │  │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  │  │  ├─ id_40966
│  │        │  │  │  │  │  │  ├─ api-v1-jd-40966.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdf-40966.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdl-dn-miceprotein-l-2-dv-4.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdl-dn-miceprotein-l-2-s-act-.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdq-40966.json.gz
│  │        │  │  │  │  │  │  ├─ data-v1-dl-17928620.arff.gz
│  │        │  │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  │  │  ├─ id_42074
│  │        │  │  │  │  │  │  ├─ api-v1-jd-42074.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdf-42074.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdq-42074.json.gz
│  │        │  │  │  │  │  │  ├─ data-v1-dl-21552912.arff.gz
│  │        │  │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  │  │  ├─ id_42585
│  │        │  │  │  │  │  │  ├─ api-v1-jd-42585.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdf-42585.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdq-42585.json.gz
│  │        │  │  │  │  │  │  ├─ data-v1-dl-21854866.arff.gz
│  │        │  │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  │  │  ├─ id_561
│  │        │  │  │  │  │  │  ├─ api-v1-jd-561.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdf-561.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdl-dn-cpu-l-2-dv-1.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdl-dn-cpu-l-2-s-act-.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdq-561.json.gz
│  │        │  │  │  │  │  │  ├─ data-v1-dl-52739.arff.gz
│  │        │  │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  │  │  ├─ id_61
│  │        │  │  │  │  │  │  ├─ api-v1-jd-61.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdf-61.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdl-dn-iris-l-2-dv-1.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdl-dn-iris-l-2-s-act-.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdq-61.json.gz
│  │        │  │  │  │  │  │  ├─ data-v1-dl-61.arff.gz
│  │        │  │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  │  │  ├─ id_62
│  │        │  │  │  │  │  │  ├─ api-v1-jd-62.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdf-62.json.gz
│  │        │  │  │  │  │  │  ├─ api-v1-jdq-62.json.gz
│  │        │  │  │  │  │  │  ├─ data-v1-dl-52352.arff.gz
│  │        │  │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  │  ├─ svmlight_classification.txt
│  │        │  │  │  │  ├─ svmlight_invalid.txt
│  │        │  │  │  │  ├─ svmlight_invalid_order.txt
│  │        │  │  │  │  ├─ svmlight_multilabel.txt
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ test_20news.py
│  │        │  │  │  ├─ test_arff_parser.py
│  │        │  │  │  ├─ test_base.py
│  │        │  │  │  ├─ test_california_housing.py
│  │        │  │  │  ├─ test_common.py
│  │        │  │  │  ├─ test_covtype.py
│  │        │  │  │  ├─ test_kddcup99.py
│  │        │  │  │  ├─ test_lfw.py
│  │        │  │  │  ├─ test_olivetti_faces.py
│  │        │  │  │  ├─ test_openml.py
│  │        │  │  │  ├─ test_rcv1.py
│  │        │  │  │  ├─ test_samples_generator.py
│  │        │  │  │  ├─ test_svmlight_format.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_20news.cpython-312.pyc
│  │        │  │  │     ├─ test_arff_parser.cpython-312.pyc
│  │        │  │  │     ├─ test_base.cpython-312.pyc
│  │        │  │  │     ├─ test_california_housing.cpython-312.pyc
│  │        │  │  │     ├─ test_common.cpython-312.pyc
│  │        │  │  │     ├─ test_covtype.cpython-312.pyc
│  │        │  │  │     ├─ test_kddcup99.cpython-312.pyc
│  │        │  │  │     ├─ test_lfw.cpython-312.pyc
│  │        │  │  │     ├─ test_olivetti_faces.cpython-312.pyc
│  │        │  │  │     ├─ test_openml.cpython-312.pyc
│  │        │  │  │     ├─ test_rcv1.cpython-312.pyc
│  │        │  │  │     ├─ test_samples_generator.cpython-312.pyc
│  │        │  │  │     ├─ test_svmlight_format.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _arff_parser.py
│  │        │  │  ├─ _base.py
│  │        │  │  ├─ _california_housing.py
│  │        │  │  ├─ _covtype.py
│  │        │  │  ├─ _kddcup99.py
│  │        │  │  ├─ _lfw.py
│  │        │  │  ├─ _olivetti_faces.py
│  │        │  │  ├─ _openml.py
│  │        │  │  ├─ _rcv1.py
│  │        │  │  ├─ _samples_generator.py
│  │        │  │  ├─ _species_distributions.py
│  │        │  │  ├─ _svmlight_format_fast.cpython-312-darwin.so
│  │        │  │  ├─ _svmlight_format_fast.pyx
│  │        │  │  ├─ _svmlight_format_io.py
│  │        │  │  ├─ _twenty_newsgroups.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ _arff_parser.cpython-312.pyc
│  │        │  │     ├─ _base.cpython-312.pyc
│  │        │  │     ├─ _california_housing.cpython-312.pyc
│  │        │  │     ├─ _covtype.cpython-312.pyc
│  │        │  │     ├─ _kddcup99.cpython-312.pyc
│  │        │  │     ├─ _lfw.cpython-312.pyc
│  │        │  │     ├─ _olivetti_faces.cpython-312.pyc
│  │        │  │     ├─ _openml.cpython-312.pyc
│  │        │  │     ├─ _rcv1.cpython-312.pyc
│  │        │  │     ├─ _samples_generator.cpython-312.pyc
│  │        │  │     ├─ _species_distributions.cpython-312.pyc
│  │        │  │     ├─ _svmlight_format_io.cpython-312.pyc
│  │        │  │     ├─ _twenty_newsgroups.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ decomposition
│  │        │  │  ├─ meson.build
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ test_dict_learning.py
│  │        │  │  │  ├─ test_factor_analysis.py
│  │        │  │  │  ├─ test_fastica.py
│  │        │  │  │  ├─ test_incremental_pca.py
│  │        │  │  │  ├─ test_kernel_pca.py
│  │        │  │  │  ├─ test_nmf.py
│  │        │  │  │  ├─ test_online_lda.py
│  │        │  │  │  ├─ test_pca.py
│  │        │  │  │  ├─ test_sparse_pca.py
│  │        │  │  │  ├─ test_truncated_svd.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_dict_learning.cpython-312.pyc
│  │        │  │  │     ├─ test_factor_analysis.cpython-312.pyc
│  │        │  │  │     ├─ test_fastica.cpython-312.pyc
│  │        │  │  │     ├─ test_incremental_pca.cpython-312.pyc
│  │        │  │  │     ├─ test_kernel_pca.cpython-312.pyc
│  │        │  │  │     ├─ test_nmf.cpython-312.pyc
│  │        │  │  │     ├─ test_online_lda.cpython-312.pyc
│  │        │  │  │     ├─ test_pca.cpython-312.pyc
│  │        │  │  │     ├─ test_sparse_pca.cpython-312.pyc
│  │        │  │  │     ├─ test_truncated_svd.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _base.py
│  │        │  │  ├─ _cdnmf_fast.cpython-312-darwin.so
│  │        │  │  ├─ _cdnmf_fast.pyx
│  │        │  │  ├─ _dict_learning.py
│  │        │  │  ├─ _factor_analysis.py
│  │        │  │  ├─ _fastica.py
│  │        │  │  ├─ _incremental_pca.py
│  │        │  │  ├─ _kernel_pca.py
│  │        │  │  ├─ _lda.py
│  │        │  │  ├─ _nmf.py
│  │        │  │  ├─ _online_lda_fast.cpython-312-darwin.so
│  │        │  │  ├─ _online_lda_fast.pyx
│  │        │  │  ├─ _pca.py
│  │        │  │  ├─ _sparse_pca.py
│  │        │  │  ├─ _truncated_svd.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ _base.cpython-312.pyc
│  │        │  │     ├─ _dict_learning.cpython-312.pyc
│  │        │  │     ├─ _factor_analysis.cpython-312.pyc
│  │        │  │     ├─ _fastica.cpython-312.pyc
│  │        │  │     ├─ _incremental_pca.cpython-312.pyc
│  │        │  │     ├─ _kernel_pca.cpython-312.pyc
│  │        │  │     ├─ _lda.cpython-312.pyc
│  │        │  │     ├─ _nmf.cpython-312.pyc
│  │        │  │     ├─ _pca.cpython-312.pyc
│  │        │  │     ├─ _sparse_pca.cpython-312.pyc
│  │        │  │     ├─ _truncated_svd.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ discriminant_analysis.py
│  │        │  ├─ dummy.py
│  │        │  ├─ ensemble
│  │        │  │  ├─ meson.build
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ test_bagging.py
│  │        │  │  │  ├─ test_base.py
│  │        │  │  │  ├─ test_common.py
│  │        │  │  │  ├─ test_forest.py
│  │        │  │  │  ├─ test_gradient_boosting.py
│  │        │  │  │  ├─ test_iforest.py
│  │        │  │  │  ├─ test_stacking.py
│  │        │  │  │  ├─ test_voting.py
│  │        │  │  │  ├─ test_weight_boosting.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_bagging.cpython-312.pyc
│  │        │  │  │     ├─ test_base.cpython-312.pyc
│  │        │  │  │     ├─ test_common.cpython-312.pyc
│  │        │  │  │     ├─ test_forest.cpython-312.pyc
│  │        │  │  │     ├─ test_gradient_boosting.cpython-312.pyc
│  │        │  │  │     ├─ test_iforest.cpython-312.pyc
│  │        │  │  │     ├─ test_stacking.cpython-312.pyc
│  │        │  │  │     ├─ test_voting.cpython-312.pyc
│  │        │  │  │     ├─ test_weight_boosting.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _bagging.py
│  │        │  │  ├─ _base.py
│  │        │  │  ├─ _forest.py
│  │        │  │  ├─ _gb.py
│  │        │  │  ├─ _gradient_boosting.cpython-312-darwin.so
│  │        │  │  ├─ _gradient_boosting.pyx
│  │        │  │  ├─ _hist_gradient_boosting
│  │        │  │  │  ├─ binning.py
│  │        │  │  │  ├─ common.cpython-312-darwin.so
│  │        │  │  │  ├─ common.pxd
│  │        │  │  │  ├─ common.pyx
│  │        │  │  │  ├─ gradient_boosting.py
│  │        │  │  │  ├─ grower.py
│  │        │  │  │  ├─ histogram.cpython-312-darwin.so
│  │        │  │  │  ├─ histogram.pyx
│  │        │  │  │  ├─ meson.build
│  │        │  │  │  ├─ predictor.py
│  │        │  │  │  ├─ splitting.cpython-312-darwin.so
│  │        │  │  │  ├─ splitting.pyx
│  │        │  │  │  ├─ tests
│  │        │  │  │  │  ├─ test_binning.py
│  │        │  │  │  │  ├─ test_bitset.py
│  │        │  │  │  │  ├─ test_compare_lightgbm.py
│  │        │  │  │  │  ├─ test_gradient_boosting.py
│  │        │  │  │  │  ├─ test_grower.py
│  │        │  │  │  │  ├─ test_histogram.py
│  │        │  │  │  │  ├─ test_monotonic_constraints.py
│  │        │  │  │  │  ├─ test_predictor.py
│  │        │  │  │  │  ├─ test_splitting.py
│  │        │  │  │  │  ├─ test_warm_start.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_binning.cpython-312.pyc
│  │        │  │  │  │     ├─ test_bitset.cpython-312.pyc
│  │        │  │  │  │     ├─ test_compare_lightgbm.cpython-312.pyc
│  │        │  │  │  │     ├─ test_gradient_boosting.cpython-312.pyc
│  │        │  │  │  │     ├─ test_grower.cpython-312.pyc
│  │        │  │  │  │     ├─ test_histogram.cpython-312.pyc
│  │        │  │  │  │     ├─ test_monotonic_constraints.cpython-312.pyc
│  │        │  │  │  │     ├─ test_predictor.cpython-312.pyc
│  │        │  │  │  │     ├─ test_splitting.cpython-312.pyc
│  │        │  │  │  │     ├─ test_warm_start.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ utils.py
│  │        │  │  │  ├─ _binning.cpython-312-darwin.so
│  │        │  │  │  ├─ _binning.pyx
│  │        │  │  │  ├─ _bitset.cpython-312-darwin.so
│  │        │  │  │  ├─ _bitset.pxd
│  │        │  │  │  ├─ _bitset.pyx
│  │        │  │  │  ├─ _gradient_boosting.cpython-312-darwin.so
│  │        │  │  │  ├─ _gradient_boosting.pyx
│  │        │  │  │  ├─ _predictor.cpython-312-darwin.so
│  │        │  │  │  ├─ _predictor.pyx
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ binning.cpython-312.pyc
│  │        │  │  │     ├─ gradient_boosting.cpython-312.pyc
│  │        │  │  │     ├─ grower.cpython-312.pyc
│  │        │  │  │     ├─ predictor.cpython-312.pyc
│  │        │  │  │     ├─ utils.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _iforest.py
│  │        │  │  ├─ _stacking.py
│  │        │  │  ├─ _voting.py
│  │        │  │  ├─ _weight_boosting.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ _bagging.cpython-312.pyc
│  │        │  │     ├─ _base.cpython-312.pyc
│  │        │  │     ├─ _forest.cpython-312.pyc
│  │        │  │     ├─ _gb.cpython-312.pyc
│  │        │  │     ├─ _iforest.cpython-312.pyc
│  │        │  │     ├─ _stacking.cpython-312.pyc
│  │        │  │     ├─ _voting.cpython-312.pyc
│  │        │  │     ├─ _weight_boosting.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ exceptions.py
│  │        │  ├─ experimental
│  │        │  │  ├─ enable_halving_search_cv.py
│  │        │  │  ├─ enable_hist_gradient_boosting.py
│  │        │  │  ├─ enable_iterative_imputer.py
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ test_enable_hist_gradient_boosting.py
│  │        │  │  │  ├─ test_enable_iterative_imputer.py
│  │        │  │  │  ├─ test_enable_successive_halving.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_enable_hist_gradient_boosting.cpython-312.pyc
│  │        │  │  │     ├─ test_enable_iterative_imputer.cpython-312.pyc
│  │        │  │  │     ├─ test_enable_successive_halving.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ enable_halving_search_cv.cpython-312.pyc
│  │        │  │     ├─ enable_hist_gradient_boosting.cpython-312.pyc
│  │        │  │     ├─ enable_iterative_imputer.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ externals
│  │        │  │  ├─ array_api_compat
│  │        │  │  │  ├─ common
│  │        │  │  │  │  ├─ _aliases.py
│  │        │  │  │  │  ├─ _fft.py
│  │        │  │  │  │  ├─ _helpers.py
│  │        │  │  │  │  ├─ _linalg.py
│  │        │  │  │  │  ├─ _typing.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ _aliases.cpython-312.pyc
│  │        │  │  │  │     ├─ _fft.cpython-312.pyc
│  │        │  │  │  │     ├─ _helpers.cpython-312.pyc
│  │        │  │  │  │     ├─ _linalg.cpython-312.pyc
│  │        │  │  │  │     ├─ _typing.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ cupy
│  │        │  │  │  │  ├─ fft.py
│  │        │  │  │  │  ├─ linalg.py
│  │        │  │  │  │  ├─ _aliases.py
│  │        │  │  │  │  ├─ _info.py
│  │        │  │  │  │  ├─ _typing.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ fft.cpython-312.pyc
│  │        │  │  │  │     ├─ linalg.cpython-312.pyc
│  │        │  │  │  │     ├─ _aliases.cpython-312.pyc
│  │        │  │  │  │     ├─ _info.cpython-312.pyc
│  │        │  │  │  │     ├─ _typing.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ dask
│  │        │  │  │  │  ├─ array
│  │        │  │  │  │  │  ├─ fft.py
│  │        │  │  │  │  │  ├─ linalg.py
│  │        │  │  │  │  │  ├─ _aliases.py
│  │        │  │  │  │  │  ├─ _info.py
│  │        │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │     ├─ fft.cpython-312.pyc
│  │        │  │  │  │  │     ├─ linalg.cpython-312.pyc
│  │        │  │  │  │  │     ├─ _aliases.cpython-312.pyc
│  │        │  │  │  │  │     ├─ _info.cpython-312.pyc
│  │        │  │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ LICENSE
│  │        │  │  │  ├─ numpy
│  │        │  │  │  │  ├─ fft.py
│  │        │  │  │  │  ├─ linalg.py
│  │        │  │  │  │  ├─ _aliases.py
│  │        │  │  │  │  ├─ _info.py
│  │        │  │  │  │  ├─ _typing.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ fft.cpython-312.pyc
│  │        │  │  │  │     ├─ linalg.cpython-312.pyc
│  │        │  │  │  │     ├─ _aliases.cpython-312.pyc
│  │        │  │  │  │     ├─ _info.cpython-312.pyc
│  │        │  │  │  │     ├─ _typing.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ README.md
│  │        │  │  │  ├─ torch
│  │        │  │  │  │  ├─ fft.py
│  │        │  │  │  │  ├─ linalg.py
│  │        │  │  │  │  ├─ _aliases.py
│  │        │  │  │  │  ├─ _info.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ fft.cpython-312.pyc
│  │        │  │  │  │     ├─ linalg.cpython-312.pyc
│  │        │  │  │  │     ├─ _aliases.cpython-312.pyc
│  │        │  │  │  │     ├─ _info.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ _internal.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ _internal.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ array_api_extra
│  │        │  │  │  ├─ LICENSE
│  │        │  │  │  ├─ py.typed
│  │        │  │  │  ├─ README.md
│  │        │  │  │  ├─ testing.py
│  │        │  │  │  ├─ _delegation.py
│  │        │  │  │  ├─ _lib
│  │        │  │  │  │  ├─ _at.py
│  │        │  │  │  │  ├─ _backends.py
│  │        │  │  │  │  ├─ _funcs.py
│  │        │  │  │  │  ├─ _lazy.py
│  │        │  │  │  │  ├─ _testing.py
│  │        │  │  │  │  ├─ _utils
│  │        │  │  │  │  │  ├─ _compat.py
│  │        │  │  │  │  │  ├─ _compat.pyi
│  │        │  │  │  │  │  ├─ _helpers.py
│  │        │  │  │  │  │  ├─ _typing.py
│  │        │  │  │  │  │  ├─ _typing.pyi
│  │        │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │     ├─ _compat.cpython-312.pyc
│  │        │  │  │  │  │     ├─ _helpers.cpython-312.pyc
│  │        │  │  │  │  │     ├─ _typing.cpython-312.pyc
│  │        │  │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ _at.cpython-312.pyc
│  │        │  │  │  │     ├─ _backends.cpython-312.pyc
│  │        │  │  │  │     ├─ _funcs.cpython-312.pyc
│  │        │  │  │  │     ├─ _lazy.cpython-312.pyc
│  │        │  │  │  │     ├─ _testing.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ testing.cpython-312.pyc
│  │        │  │  │     ├─ _delegation.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ conftest.py
│  │        │  │  ├─ README
│  │        │  │  ├─ _arff.py
│  │        │  │  ├─ _array_api_compat_vendor.py
│  │        │  │  ├─ _packaging
│  │        │  │  │  ├─ version.py
│  │        │  │  │  ├─ _structures.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ version.cpython-312.pyc
│  │        │  │  │     ├─ _structures.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _scipy
│  │        │  │  │  ├─ sparse
│  │        │  │  │  │  ├─ csgraph
│  │        │  │  │  │  │  ├─ _laplacian.py
│  │        │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  └─ __pycache__
│  │        │  │  │  │  │     ├─ _laplacian.cpython-312.pyc
│  │        │  │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ conftest.cpython-312.pyc
│  │        │  │     ├─ _arff.cpython-312.pyc
│  │        │  │     ├─ _array_api_compat_vendor.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ feature_extraction
│  │        │  │  ├─ image.py
│  │        │  │  ├─ meson.build
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ test_dict_vectorizer.py
│  │        │  │  │  ├─ test_feature_hasher.py
│  │        │  │  │  ├─ test_image.py
│  │        │  │  │  ├─ test_text.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_dict_vectorizer.cpython-312.pyc
│  │        │  │  │     ├─ test_feature_hasher.cpython-312.pyc
│  │        │  │  │     ├─ test_image.cpython-312.pyc
│  │        │  │  │     ├─ test_text.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ text.py
│  │        │  │  ├─ _dict_vectorizer.py
│  │        │  │  ├─ _hash.py
│  │        │  │  ├─ _hashing_fast.cpython-312-darwin.so
│  │        │  │  ├─ _hashing_fast.pyx
│  │        │  │  ├─ _stop_words.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ image.cpython-312.pyc
│  │        │  │     ├─ text.cpython-312.pyc
│  │        │  │     ├─ _dict_vectorizer.cpython-312.pyc
│  │        │  │     ├─ _hash.cpython-312.pyc
│  │        │  │     ├─ _stop_words.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ feature_selection
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ test_base.py
│  │        │  │  │  ├─ test_chi2.py
│  │        │  │  │  ├─ test_feature_select.py
│  │        │  │  │  ├─ test_from_model.py
│  │        │  │  │  ├─ test_mutual_info.py
│  │        │  │  │  ├─ test_rfe.py
│  │        │  │  │  ├─ test_sequential.py
│  │        │  │  │  ├─ test_variance_threshold.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_base.cpython-312.pyc
│  │        │  │  │     ├─ test_chi2.cpython-312.pyc
│  │        │  │  │     ├─ test_feature_select.cpython-312.pyc
│  │        │  │  │     ├─ test_from_model.cpython-312.pyc
│  │        │  │  │     ├─ test_mutual_info.cpython-312.pyc
│  │        │  │  │     ├─ test_rfe.cpython-312.pyc
│  │        │  │  │     ├─ test_sequential.cpython-312.pyc
│  │        │  │  │     ├─ test_variance_threshold.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _base.py
│  │        │  │  ├─ _from_model.py
│  │        │  │  ├─ _mutual_info.py
│  │        │  │  ├─ _rfe.py
│  │        │  │  ├─ _sequential.py
│  │        │  │  ├─ _univariate_selection.py
│  │        │  │  ├─ _variance_threshold.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ _base.cpython-312.pyc
│  │        │  │     ├─ _from_model.cpython-312.pyc
│  │        │  │     ├─ _mutual_info.cpython-312.pyc
│  │        │  │     ├─ _rfe.cpython-312.pyc
│  │        │  │     ├─ _sequential.cpython-312.pyc
│  │        │  │     ├─ _univariate_selection.cpython-312.pyc
│  │        │  │     ├─ _variance_threshold.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ frozen
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ test_frozen.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_frozen.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _frozen.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ _frozen.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ gaussian_process
│  │        │  │  ├─ kernels.py
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ test_gpc.py
│  │        │  │  │  ├─ test_gpr.py
│  │        │  │  │  ├─ test_kernels.py
│  │        │  │  │  ├─ _mini_sequence_kernel.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_gpc.cpython-312.pyc
│  │        │  │  │     ├─ test_gpr.cpython-312.pyc
│  │        │  │  │     ├─ test_kernels.cpython-312.pyc
│  │        │  │  │     ├─ _mini_sequence_kernel.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _gpc.py
│  │        │  │  ├─ _gpr.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ kernels.cpython-312.pyc
│  │        │  │     ├─ _gpc.cpython-312.pyc
│  │        │  │     ├─ _gpr.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ impute
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ test_base.py
│  │        │  │  │  ├─ test_common.py
│  │        │  │  │  ├─ test_impute.py
│  │        │  │  │  ├─ test_knn.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_base.cpython-312.pyc
│  │        │  │  │     ├─ test_common.cpython-312.pyc
│  │        │  │  │     ├─ test_impute.cpython-312.pyc
│  │        │  │  │     ├─ test_knn.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _base.py
│  │        │  │  ├─ _iterative.py
│  │        │  │  ├─ _knn.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ _base.cpython-312.pyc
│  │        │  │     ├─ _iterative.cpython-312.pyc
│  │        │  │     ├─ _knn.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ inspection
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ test_partial_dependence.py
│  │        │  │  │  ├─ test_pd_utils.py
│  │        │  │  │  ├─ test_permutation_importance.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_partial_dependence.cpython-312.pyc
│  │        │  │  │     ├─ test_pd_utils.cpython-312.pyc
│  │        │  │  │     ├─ test_permutation_importance.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _partial_dependence.py
│  │        │  │  ├─ _pd_utils.py
│  │        │  │  ├─ _permutation_importance.py
│  │        │  │  ├─ _plot
│  │        │  │  │  ├─ decision_boundary.py
│  │        │  │  │  ├─ partial_dependence.py
│  │        │  │  │  ├─ tests
│  │        │  │  │  │  ├─ test_boundary_decision_display.py
│  │        │  │  │  │  ├─ test_plot_partial_dependence.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_boundary_decision_display.cpython-312.pyc
│  │        │  │  │  │     ├─ test_plot_partial_dependence.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ decision_boundary.cpython-312.pyc
│  │        │  │  │     ├─ partial_dependence.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ _partial_dependence.cpython-312.pyc
│  │        │  │     ├─ _pd_utils.cpython-312.pyc
│  │        │  │     ├─ _permutation_importance.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ isotonic.py
│  │        │  ├─ kernel_approximation.py
│  │        │  ├─ kernel_ridge.py
│  │        │  ├─ linear_model
│  │        │  │  ├─ meson.build
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ test_base.py
│  │        │  │  │  ├─ test_bayes.py
│  │        │  │  │  ├─ test_common.py
│  │        │  │  │  ├─ test_coordinate_descent.py
│  │        │  │  │  ├─ test_huber.py
│  │        │  │  │  ├─ test_least_angle.py
│  │        │  │  │  ├─ test_linear_loss.py
│  │        │  │  │  ├─ test_logistic.py
│  │        │  │  │  ├─ test_omp.py
│  │        │  │  │  ├─ test_passive_aggressive.py
│  │        │  │  │  ├─ test_perceptron.py
│  │        │  │  │  ├─ test_quantile.py
│  │        │  │  │  ├─ test_ransac.py
│  │        │  │  │  ├─ test_ridge.py
│  │        │  │  │  ├─ test_sag.py
│  │        │  │  │  ├─ test_sgd.py
│  │        │  │  │  ├─ test_sparse_coordinate_descent.py
│  │        │  │  │  ├─ test_theil_sen.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_base.cpython-312.pyc
│  │        │  │  │     ├─ test_bayes.cpython-312.pyc
│  │        │  │  │     ├─ test_common.cpython-312.pyc
│  │        │  │  │     ├─ test_coordinate_descent.cpython-312.pyc
│  │        │  │  │     ├─ test_huber.cpython-312.pyc
│  │        │  │  │     ├─ test_least_angle.cpython-312.pyc
│  │        │  │  │     ├─ test_linear_loss.cpython-312.pyc
│  │        │  │  │     ├─ test_logistic.cpython-312.pyc
│  │        │  │  │     ├─ test_omp.cpython-312.pyc
│  │        │  │  │     ├─ test_passive_aggressive.cpython-312.pyc
│  │        │  │  │     ├─ test_perceptron.cpython-312.pyc
│  │        │  │  │     ├─ test_quantile.cpython-312.pyc
│  │        │  │  │     ├─ test_ransac.cpython-312.pyc
│  │        │  │  │     ├─ test_ridge.cpython-312.pyc
│  │        │  │  │     ├─ test_sag.cpython-312.pyc
│  │        │  │  │     ├─ test_sgd.cpython-312.pyc
│  │        │  │  │     ├─ test_sparse_coordinate_descent.cpython-312.pyc
│  │        │  │  │     ├─ test_theil_sen.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _base.py
│  │        │  │  ├─ _bayes.py
│  │        │  │  ├─ _cd_fast.cpython-312-darwin.so
│  │        │  │  ├─ _cd_fast.pyx
│  │        │  │  ├─ _coordinate_descent.py
│  │        │  │  ├─ _glm
│  │        │  │  │  ├─ glm.py
│  │        │  │  │  ├─ tests
│  │        │  │  │  │  ├─ test_glm.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_glm.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ _newton_solver.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ glm.cpython-312.pyc
│  │        │  │  │     ├─ _newton_solver.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _huber.py
│  │        │  │  ├─ _least_angle.py
│  │        │  │  ├─ _linear_loss.py
│  │        │  │  ├─ _logistic.py
│  │        │  │  ├─ _omp.py
│  │        │  │  ├─ _passive_aggressive.py
│  │        │  │  ├─ _perceptron.py
│  │        │  │  ├─ _quantile.py
│  │        │  │  ├─ _ransac.py
│  │        │  │  ├─ _ridge.py
│  │        │  │  ├─ _sag.py
│  │        │  │  ├─ _sag_fast.cpython-312-darwin.so
│  │        │  │  ├─ _sag_fast.pyx.tp
│  │        │  │  ├─ _sgd_fast.cpython-312-darwin.so
│  │        │  │  ├─ _sgd_fast.pyx.tp
│  │        │  │  ├─ _stochastic_gradient.py
│  │        │  │  ├─ _theil_sen.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ _base.cpython-312.pyc
│  │        │  │     ├─ _bayes.cpython-312.pyc
│  │        │  │     ├─ _coordinate_descent.cpython-312.pyc
│  │        │  │     ├─ _huber.cpython-312.pyc
│  │        │  │     ├─ _least_angle.cpython-312.pyc
│  │        │  │     ├─ _linear_loss.cpython-312.pyc
│  │        │  │     ├─ _logistic.cpython-312.pyc
│  │        │  │     ├─ _omp.cpython-312.pyc
│  │        │  │     ├─ _passive_aggressive.cpython-312.pyc
│  │        │  │     ├─ _perceptron.cpython-312.pyc
│  │        │  │     ├─ _quantile.cpython-312.pyc
│  │        │  │     ├─ _ransac.cpython-312.pyc
│  │        │  │     ├─ _ridge.cpython-312.pyc
│  │        │  │     ├─ _sag.cpython-312.pyc
│  │        │  │     ├─ _stochastic_gradient.cpython-312.pyc
│  │        │  │     ├─ _theil_sen.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ manifold
│  │        │  │  ├─ meson.build
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ test_isomap.py
│  │        │  │  │  ├─ test_locally_linear.py
│  │        │  │  │  ├─ test_mds.py
│  │        │  │  │  ├─ test_spectral_embedding.py
│  │        │  │  │  ├─ test_t_sne.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_isomap.cpython-312.pyc
│  │        │  │  │     ├─ test_locally_linear.cpython-312.pyc
│  │        │  │  │     ├─ test_mds.cpython-312.pyc
│  │        │  │  │     ├─ test_spectral_embedding.cpython-312.pyc
│  │        │  │  │     ├─ test_t_sne.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _barnes_hut_tsne.cpython-312-darwin.so
│  │        │  │  ├─ _barnes_hut_tsne.pyx
│  │        │  │  ├─ _isomap.py
│  │        │  │  ├─ _locally_linear.py
│  │        │  │  ├─ _mds.py
│  │        │  │  ├─ _spectral_embedding.py
│  │        │  │  ├─ _t_sne.py
│  │        │  │  ├─ _utils.cpython-312-darwin.so
│  │        │  │  ├─ _utils.pyx
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ _isomap.cpython-312.pyc
│  │        │  │     ├─ _locally_linear.cpython-312.pyc
│  │        │  │     ├─ _mds.cpython-312.pyc
│  │        │  │     ├─ _spectral_embedding.cpython-312.pyc
│  │        │  │     ├─ _t_sne.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ meson.build
│  │        │  ├─ metrics
│  │        │  │  ├─ cluster
│  │        │  │  │  ├─ meson.build
│  │        │  │  │  ├─ tests
│  │        │  │  │  │  ├─ test_bicluster.py
│  │        │  │  │  │  ├─ test_common.py
│  │        │  │  │  │  ├─ test_supervised.py
│  │        │  │  │  │  ├─ test_unsupervised.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_bicluster.cpython-312.pyc
│  │        │  │  │  │     ├─ test_common.cpython-312.pyc
│  │        │  │  │  │     ├─ test_supervised.cpython-312.pyc
│  │        │  │  │  │     ├─ test_unsupervised.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ _bicluster.py
│  │        │  │  │  ├─ _expected_mutual_info_fast.cpython-312-darwin.so
│  │        │  │  │  ├─ _expected_mutual_info_fast.pyx
│  │        │  │  │  ├─ _supervised.py
│  │        │  │  │  ├─ _unsupervised.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ _bicluster.cpython-312.pyc
│  │        │  │  │     ├─ _supervised.cpython-312.pyc
│  │        │  │  │     ├─ _unsupervised.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ meson.build
│  │        │  │  ├─ pairwise.py
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ test_classification.py
│  │        │  │  │  ├─ test_common.py
│  │        │  │  │  ├─ test_dist_metrics.py
│  │        │  │  │  ├─ test_pairwise.py
│  │        │  │  │  ├─ test_pairwise_distances_reduction.py
│  │        │  │  │  ├─ test_ranking.py
│  │        │  │  │  ├─ test_regression.py
│  │        │  │  │  ├─ test_score_objects.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_classification.cpython-312.pyc
│  │        │  │  │     ├─ test_common.cpython-312.pyc
│  │        │  │  │     ├─ test_dist_metrics.cpython-312.pyc
│  │        │  │  │     ├─ test_pairwise.cpython-312.pyc
│  │        │  │  │     ├─ test_pairwise_distances_reduction.cpython-312.pyc
│  │        │  │  │     ├─ test_ranking.cpython-312.pyc
│  │        │  │  │     ├─ test_regression.cpython-312.pyc
│  │        │  │  │     ├─ test_score_objects.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _base.py
│  │        │  │  ├─ _classification.py
│  │        │  │  ├─ _dist_metrics.cpython-312-darwin.so
│  │        │  │  ├─ _dist_metrics.pxd
│  │        │  │  ├─ _dist_metrics.pxd.tp
│  │        │  │  ├─ _dist_metrics.pyx.tp
│  │        │  │  ├─ _pairwise_distances_reduction
│  │        │  │  │  ├─ meson.build
│  │        │  │  │  ├─ _argkmin.cpython-312-darwin.so
│  │        │  │  │  ├─ _argkmin.pxd.tp
│  │        │  │  │  ├─ _argkmin.pyx.tp
│  │        │  │  │  ├─ _argkmin_classmode.cpython-312-darwin.so
│  │        │  │  │  ├─ _argkmin_classmode.pyx.tp
│  │        │  │  │  ├─ _base.cpython-312-darwin.so
│  │        │  │  │  ├─ _base.pxd.tp
│  │        │  │  │  ├─ _base.pyx.tp
│  │        │  │  │  ├─ _classmode.pxd
│  │        │  │  │  ├─ _datasets_pair.cpython-312-darwin.so
│  │        │  │  │  ├─ _datasets_pair.pxd.tp
│  │        │  │  │  ├─ _datasets_pair.pyx.tp
│  │        │  │  │  ├─ _dispatcher.py
│  │        │  │  │  ├─ _middle_term_computer.cpython-312-darwin.so
│  │        │  │  │  ├─ _middle_term_computer.pxd.tp
│  │        │  │  │  ├─ _middle_term_computer.pyx.tp
│  │        │  │  │  ├─ _radius_neighbors.cpython-312-darwin.so
│  │        │  │  │  ├─ _radius_neighbors.pxd.tp
│  │        │  │  │  ├─ _radius_neighbors.pyx.tp
│  │        │  │  │  ├─ _radius_neighbors_classmode.cpython-312-darwin.so
│  │        │  │  │  ├─ _radius_neighbors_classmode.pyx.tp
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ _dispatcher.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _pairwise_fast.cpython-312-darwin.so
│  │        │  │  ├─ _pairwise_fast.pyx
│  │        │  │  ├─ _plot
│  │        │  │  │  ├─ confusion_matrix.py
│  │        │  │  │  ├─ det_curve.py
│  │        │  │  │  ├─ precision_recall_curve.py
│  │        │  │  │  ├─ regression.py
│  │        │  │  │  ├─ roc_curve.py
│  │        │  │  │  ├─ tests
│  │        │  │  │  │  ├─ test_common_curve_display.py
│  │        │  │  │  │  ├─ test_confusion_matrix_display.py
│  │        │  │  │  │  ├─ test_det_curve_display.py
│  │        │  │  │  │  ├─ test_precision_recall_display.py
│  │        │  │  │  │  ├─ test_predict_error_display.py
│  │        │  │  │  │  ├─ test_roc_curve_display.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_common_curve_display.cpython-312.pyc
│  │        │  │  │  │     ├─ test_confusion_matrix_display.cpython-312.pyc
│  │        │  │  │  │     ├─ test_det_curve_display.cpython-312.pyc
│  │        │  │  │  │     ├─ test_precision_recall_display.cpython-312.pyc
│  │        │  │  │  │     ├─ test_predict_error_display.cpython-312.pyc
│  │        │  │  │  │     ├─ test_roc_curve_display.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ confusion_matrix.cpython-312.pyc
│  │        │  │  │     ├─ det_curve.cpython-312.pyc
│  │        │  │  │     ├─ precision_recall_curve.cpython-312.pyc
│  │        │  │  │     ├─ regression.cpython-312.pyc
│  │        │  │  │     ├─ roc_curve.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _ranking.py
│  │        │  │  ├─ _regression.py
│  │        │  │  ├─ _scorer.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ pairwise.cpython-312.pyc
│  │        │  │     ├─ _base.cpython-312.pyc
│  │        │  │     ├─ _classification.cpython-312.pyc
│  │        │  │     ├─ _ranking.cpython-312.pyc
│  │        │  │     ├─ _regression.cpython-312.pyc
│  │        │  │     ├─ _scorer.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ mixture
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ test_bayesian_mixture.py
│  │        │  │  │  ├─ test_gaussian_mixture.py
│  │        │  │  │  ├─ test_mixture.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_bayesian_mixture.cpython-312.pyc
│  │        │  │  │     ├─ test_gaussian_mixture.cpython-312.pyc
│  │        │  │  │     ├─ test_mixture.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _base.py
│  │        │  │  ├─ _bayesian_mixture.py
│  │        │  │  ├─ _gaussian_mixture.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ _base.cpython-312.pyc
│  │        │  │     ├─ _bayesian_mixture.cpython-312.pyc
│  │        │  │     ├─ _gaussian_mixture.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ model_selection
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ common.py
│  │        │  │  │  ├─ test_classification_threshold.py
│  │        │  │  │  ├─ test_plot.py
│  │        │  │  │  ├─ test_search.py
│  │        │  │  │  ├─ test_split.py
│  │        │  │  │  ├─ test_successive_halving.py
│  │        │  │  │  ├─ test_validation.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ common.cpython-312.pyc
│  │        │  │  │     ├─ test_classification_threshold.cpython-312.pyc
│  │        │  │  │     ├─ test_plot.cpython-312.pyc
│  │        │  │  │     ├─ test_search.cpython-312.pyc
│  │        │  │  │     ├─ test_split.cpython-312.pyc
│  │        │  │  │     ├─ test_successive_halving.cpython-312.pyc
│  │        │  │  │     ├─ test_validation.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _classification_threshold.py
│  │        │  │  ├─ _plot.py
│  │        │  │  ├─ _search.py
│  │        │  │  ├─ _search_successive_halving.py
│  │        │  │  ├─ _split.py
│  │        │  │  ├─ _validation.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ _classification_threshold.cpython-312.pyc
│  │        │  │     ├─ _plot.cpython-312.pyc
│  │        │  │     ├─ _search.cpython-312.pyc
│  │        │  │     ├─ _search_successive_halving.cpython-312.pyc
│  │        │  │     ├─ _split.cpython-312.pyc
│  │        │  │     ├─ _validation.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ multiclass.py
│  │        │  ├─ multioutput.py
│  │        │  ├─ naive_bayes.py
│  │        │  ├─ neighbors
│  │        │  │  ├─ meson.build
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ test_ball_tree.py
│  │        │  │  │  ├─ test_graph.py
│  │        │  │  │  ├─ test_kde.py
│  │        │  │  │  ├─ test_kd_tree.py
│  │        │  │  │  ├─ test_lof.py
│  │        │  │  │  ├─ test_nca.py
│  │        │  │  │  ├─ test_nearest_centroid.py
│  │        │  │  │  ├─ test_neighbors.py
│  │        │  │  │  ├─ test_neighbors_pipeline.py
│  │        │  │  │  ├─ test_neighbors_tree.py
│  │        │  │  │  ├─ test_quad_tree.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_ball_tree.cpython-312.pyc
│  │        │  │  │     ├─ test_graph.cpython-312.pyc
│  │        │  │  │     ├─ test_kde.cpython-312.pyc
│  │        │  │  │     ├─ test_kd_tree.cpython-312.pyc
│  │        │  │  │     ├─ test_lof.cpython-312.pyc
│  │        │  │  │     ├─ test_nca.cpython-312.pyc
│  │        │  │  │     ├─ test_nearest_centroid.cpython-312.pyc
│  │        │  │  │     ├─ test_neighbors.cpython-312.pyc
│  │        │  │  │     ├─ test_neighbors_pipeline.cpython-312.pyc
│  │        │  │  │     ├─ test_neighbors_tree.cpython-312.pyc
│  │        │  │  │     ├─ test_quad_tree.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _ball_tree.cpython-312-darwin.so
│  │        │  │  ├─ _ball_tree.pyx.tp
│  │        │  │  ├─ _base.py
│  │        │  │  ├─ _binary_tree.pxi.tp
│  │        │  │  ├─ _classification.py
│  │        │  │  ├─ _graph.py
│  │        │  │  ├─ _kde.py
│  │        │  │  ├─ _kd_tree.cpython-312-darwin.so
│  │        │  │  ├─ _kd_tree.pyx.tp
│  │        │  │  ├─ _lof.py
│  │        │  │  ├─ _nca.py
│  │        │  │  ├─ _nearest_centroid.py
│  │        │  │  ├─ _partition_nodes.cpython-312-darwin.so
│  │        │  │  ├─ _partition_nodes.pxd
│  │        │  │  ├─ _partition_nodes.pyx
│  │        │  │  ├─ _quad_tree.cpython-312-darwin.so
│  │        │  │  ├─ _quad_tree.pxd
│  │        │  │  ├─ _quad_tree.pyx
│  │        │  │  ├─ _regression.py
│  │        │  │  ├─ _unsupervised.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ _base.cpython-312.pyc
│  │        │  │     ├─ _classification.cpython-312.pyc
│  │        │  │     ├─ _graph.cpython-312.pyc
│  │        │  │     ├─ _kde.cpython-312.pyc
│  │        │  │     ├─ _lof.cpython-312.pyc
│  │        │  │     ├─ _nca.cpython-312.pyc
│  │        │  │     ├─ _nearest_centroid.cpython-312.pyc
│  │        │  │     ├─ _regression.cpython-312.pyc
│  │        │  │     ├─ _unsupervised.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ neural_network
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ test_base.py
│  │        │  │  │  ├─ test_mlp.py
│  │        │  │  │  ├─ test_rbm.py
│  │        │  │  │  ├─ test_stochastic_optimizers.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_base.cpython-312.pyc
│  │        │  │  │     ├─ test_mlp.cpython-312.pyc
│  │        │  │  │     ├─ test_rbm.cpython-312.pyc
│  │        │  │  │     ├─ test_stochastic_optimizers.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _base.py
│  │        │  │  ├─ _multilayer_perceptron.py
│  │        │  │  ├─ _rbm.py
│  │        │  │  ├─ _stochastic_optimizers.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ _base.cpython-312.pyc
│  │        │  │     ├─ _multilayer_perceptron.cpython-312.pyc
│  │        │  │     ├─ _rbm.cpython-312.pyc
│  │        │  │     ├─ _stochastic_optimizers.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ pipeline.py
│  │        │  ├─ preprocessing
│  │        │  │  ├─ meson.build
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ test_common.py
│  │        │  │  │  ├─ test_data.py
│  │        │  │  │  ├─ test_discretization.py
│  │        │  │  │  ├─ test_encoders.py
│  │        │  │  │  ├─ test_function_transformer.py
│  │        │  │  │  ├─ test_label.py
│  │        │  │  │  ├─ test_polynomial.py
│  │        │  │  │  ├─ test_target_encoder.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_common.cpython-312.pyc
│  │        │  │  │     ├─ test_data.cpython-312.pyc
│  │        │  │  │     ├─ test_discretization.cpython-312.pyc
│  │        │  │  │     ├─ test_encoders.cpython-312.pyc
│  │        │  │  │     ├─ test_function_transformer.cpython-312.pyc
│  │        │  │  │     ├─ test_label.cpython-312.pyc
│  │        │  │  │     ├─ test_polynomial.cpython-312.pyc
│  │        │  │  │     ├─ test_target_encoder.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _csr_polynomial_expansion.cpython-312-darwin.so
│  │        │  │  ├─ _csr_polynomial_expansion.pyx
│  │        │  │  ├─ _data.py
│  │        │  │  ├─ _discretization.py
│  │        │  │  ├─ _encoders.py
│  │        │  │  ├─ _function_transformer.py
│  │        │  │  ├─ _label.py
│  │        │  │  ├─ _polynomial.py
│  │        │  │  ├─ _target_encoder.py
│  │        │  │  ├─ _target_encoder_fast.cpython-312-darwin.so
│  │        │  │  ├─ _target_encoder_fast.pyx
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ _data.cpython-312.pyc
│  │        │  │     ├─ _discretization.cpython-312.pyc
│  │        │  │     ├─ _encoders.cpython-312.pyc
│  │        │  │     ├─ _function_transformer.cpython-312.pyc
│  │        │  │     ├─ _label.cpython-312.pyc
│  │        │  │     ├─ _polynomial.cpython-312.pyc
│  │        │  │     ├─ _target_encoder.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ random_projection.py
│  │        │  ├─ semi_supervised
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ test_label_propagation.py
│  │        │  │  │  ├─ test_self_training.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_label_propagation.cpython-312.pyc
│  │        │  │  │     ├─ test_self_training.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _label_propagation.py
│  │        │  │  ├─ _self_training.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ _label_propagation.cpython-312.pyc
│  │        │  │     ├─ _self_training.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ svm
│  │        │  │  ├─ meson.build
│  │        │  │  ├─ src
│  │        │  │  │  ├─ liblinear
│  │        │  │  │  │  ├─ COPYRIGHT
│  │        │  │  │  │  ├─ liblinear_helper.c
│  │        │  │  │  │  ├─ linear.cpp
│  │        │  │  │  │  ├─ linear.h
│  │        │  │  │  │  ├─ tron.cpp
│  │        │  │  │  │  ├─ tron.h
│  │        │  │  │  │  └─ _cython_blas_helpers.h
│  │        │  │  │  ├─ libsvm
│  │        │  │  │  │  ├─ LIBSVM_CHANGES
│  │        │  │  │  │  ├─ libsvm_helper.c
│  │        │  │  │  │  ├─ libsvm_sparse_helper.c
│  │        │  │  │  │  ├─ libsvm_template.cpp
│  │        │  │  │  │  ├─ svm.cpp
│  │        │  │  │  │  ├─ svm.h
│  │        │  │  │  │  └─ _svm_cython_blas_helpers.h
│  │        │  │  │  └─ newrand
│  │        │  │  │     └─ newrand.h
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ test_bounds.py
│  │        │  │  │  ├─ test_sparse.py
│  │        │  │  │  ├─ test_svm.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_bounds.cpython-312.pyc
│  │        │  │  │     ├─ test_sparse.cpython-312.pyc
│  │        │  │  │     ├─ test_svm.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _base.py
│  │        │  │  ├─ _bounds.py
│  │        │  │  ├─ _classes.py
│  │        │  │  ├─ _liblinear.cpython-312-darwin.so
│  │        │  │  ├─ _liblinear.pxi
│  │        │  │  ├─ _liblinear.pyx
│  │        │  │  ├─ _libsvm.cpython-312-darwin.so
│  │        │  │  ├─ _libsvm.pxi
│  │        │  │  ├─ _libsvm.pyx
│  │        │  │  ├─ _libsvm_sparse.cpython-312-darwin.so
│  │        │  │  ├─ _libsvm_sparse.pyx
│  │        │  │  ├─ _newrand.cpython-312-darwin.so
│  │        │  │  ├─ _newrand.pyx
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ _base.cpython-312.pyc
│  │        │  │     ├─ _bounds.cpython-312.pyc
│  │        │  │     ├─ _classes.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ tests
│  │        │  │  ├─ metadata_routing_common.py
│  │        │  │  ├─ test_base.py
│  │        │  │  ├─ test_build.py
│  │        │  │  ├─ test_calibration.py
│  │        │  │  ├─ test_check_build.py
│  │        │  │  ├─ test_common.py
│  │        │  │  ├─ test_config.py
│  │        │  │  ├─ test_discriminant_analysis.py
│  │        │  │  ├─ test_docstrings.py
│  │        │  │  ├─ test_docstring_parameters.py
│  │        │  │  ├─ test_docstring_parameters_consistency.py
│  │        │  │  ├─ test_dummy.py
│  │        │  │  ├─ test_init.py
│  │        │  │  ├─ test_isotonic.py
│  │        │  │  ├─ test_kernel_approximation.py
│  │        │  │  ├─ test_kernel_ridge.py
│  │        │  │  ├─ test_metadata_routing.py
│  │        │  │  ├─ test_metaestimators.py
│  │        │  │  ├─ test_metaestimators_metadata_routing.py
│  │        │  │  ├─ test_min_dependencies_readme.py
│  │        │  │  ├─ test_multiclass.py
│  │        │  │  ├─ test_multioutput.py
│  │        │  │  ├─ test_naive_bayes.py
│  │        │  │  ├─ test_pipeline.py
│  │        │  │  ├─ test_public_functions.py
│  │        │  │  ├─ test_random_projection.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ metadata_routing_common.cpython-312.pyc
│  │        │  │     ├─ test_base.cpython-312.pyc
│  │        │  │     ├─ test_build.cpython-312.pyc
│  │        │  │     ├─ test_calibration.cpython-312.pyc
│  │        │  │     ├─ test_check_build.cpython-312.pyc
│  │        │  │     ├─ test_common.cpython-312.pyc
│  │        │  │     ├─ test_config.cpython-312.pyc
│  │        │  │     ├─ test_discriminant_analysis.cpython-312.pyc
│  │        │  │     ├─ test_docstrings.cpython-312.pyc
│  │        │  │     ├─ test_docstring_parameters.cpython-312.pyc
│  │        │  │     ├─ test_docstring_parameters_consistency.cpython-312.pyc
│  │        │  │     ├─ test_dummy.cpython-312.pyc
│  │        │  │     ├─ test_init.cpython-312.pyc
│  │        │  │     ├─ test_isotonic.cpython-312.pyc
│  │        │  │     ├─ test_kernel_approximation.cpython-312.pyc
│  │        │  │     ├─ test_kernel_ridge.cpython-312.pyc
│  │        │  │     ├─ test_metadata_routing.cpython-312.pyc
│  │        │  │     ├─ test_metaestimators.cpython-312.pyc
│  │        │  │     ├─ test_metaestimators_metadata_routing.cpython-312.pyc
│  │        │  │     ├─ test_min_dependencies_readme.cpython-312.pyc
│  │        │  │     ├─ test_multiclass.cpython-312.pyc
│  │        │  │     ├─ test_multioutput.cpython-312.pyc
│  │        │  │     ├─ test_naive_bayes.cpython-312.pyc
│  │        │  │     ├─ test_pipeline.cpython-312.pyc
│  │        │  │     ├─ test_public_functions.cpython-312.pyc
│  │        │  │     ├─ test_random_projection.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ tree
│  │        │  │  ├─ meson.build
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ test_export.py
│  │        │  │  │  ├─ test_monotonic_tree.py
│  │        │  │  │  ├─ test_reingold_tilford.py
│  │        │  │  │  ├─ test_tree.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_export.cpython-312.pyc
│  │        │  │  │     ├─ test_monotonic_tree.cpython-312.pyc
│  │        │  │  │     ├─ test_reingold_tilford.cpython-312.pyc
│  │        │  │  │     ├─ test_tree.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _classes.py
│  │        │  │  ├─ _criterion.cpython-312-darwin.so
│  │        │  │  ├─ _criterion.pxd
│  │        │  │  ├─ _criterion.pyx
│  │        │  │  ├─ _export.py
│  │        │  │  ├─ _partitioner.cpython-312-darwin.so
│  │        │  │  ├─ _partitioner.pxd
│  │        │  │  ├─ _partitioner.pyx
│  │        │  │  ├─ _reingold_tilford.py
│  │        │  │  ├─ _splitter.cpython-312-darwin.so
│  │        │  │  ├─ _splitter.pxd
│  │        │  │  ├─ _splitter.pyx
│  │        │  │  ├─ _tree.cpython-312-darwin.so
│  │        │  │  ├─ _tree.pxd
│  │        │  │  ├─ _tree.pyx
│  │        │  │  ├─ _utils.cpython-312-darwin.so
│  │        │  │  ├─ _utils.pxd
│  │        │  │  ├─ _utils.pyx
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ _classes.cpython-312.pyc
│  │        │  │     ├─ _export.cpython-312.pyc
│  │        │  │     ├─ _reingold_tilford.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ utils
│  │        │  │  ├─ arrayfuncs.cpython-312-darwin.so
│  │        │  │  ├─ arrayfuncs.pyx
│  │        │  │  ├─ class_weight.py
│  │        │  │  ├─ deprecation.py
│  │        │  │  ├─ discovery.py
│  │        │  │  ├─ estimator_checks.py
│  │        │  │  ├─ extmath.py
│  │        │  │  ├─ fixes.py
│  │        │  │  ├─ graph.py
│  │        │  │  ├─ meson.build
│  │        │  │  ├─ metadata_routing.py
│  │        │  │  ├─ metaestimators.py
│  │        │  │  ├─ multiclass.py
│  │        │  │  ├─ murmurhash.cpython-312-darwin.so
│  │        │  │  ├─ murmurhash.pxd
│  │        │  │  ├─ murmurhash.pyx
│  │        │  │  ├─ optimize.py
│  │        │  │  ├─ parallel.py
│  │        │  │  ├─ random.py
│  │        │  │  ├─ sparsefuncs.py
│  │        │  │  ├─ sparsefuncs_fast.cpython-312-darwin.so
│  │        │  │  ├─ sparsefuncs_fast.pyx
│  │        │  │  ├─ src
│  │        │  │  │  ├─ MurmurHash3.cpp
│  │        │  │  │  └─ MurmurHash3.h
│  │        │  │  ├─ stats.py
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ test_arpack.py
│  │        │  │  │  ├─ test_arrayfuncs.py
│  │        │  │  │  ├─ test_array_api.py
│  │        │  │  │  ├─ test_bunch.py
│  │        │  │  │  ├─ test_chunking.py
│  │        │  │  │  ├─ test_class_weight.py
│  │        │  │  │  ├─ test_cython_blas.py
│  │        │  │  │  ├─ test_deprecation.py
│  │        │  │  │  ├─ test_encode.py
│  │        │  │  │  ├─ test_estimator_checks.py
│  │        │  │  │  ├─ test_extmath.py
│  │        │  │  │  ├─ test_fast_dict.py
│  │        │  │  │  ├─ test_fixes.py
│  │        │  │  │  ├─ test_graph.py
│  │        │  │  │  ├─ test_indexing.py
│  │        │  │  │  ├─ test_mask.py
│  │        │  │  │  ├─ test_metaestimators.py
│  │        │  │  │  ├─ test_missing.py
│  │        │  │  │  ├─ test_mocking.py
│  │        │  │  │  ├─ test_multiclass.py
│  │        │  │  │  ├─ test_murmurhash.py
│  │        │  │  │  ├─ test_optimize.py
│  │        │  │  │  ├─ test_parallel.py
│  │        │  │  │  ├─ test_param_validation.py
│  │        │  │  │  ├─ test_plotting.py
│  │        │  │  │  ├─ test_pprint.py
│  │        │  │  │  ├─ test_random.py
│  │        │  │  │  ├─ test_response.py
│  │        │  │  │  ├─ test_seq_dataset.py
│  │        │  │  │  ├─ test_set_output.py
│  │        │  │  │  ├─ test_shortest_path.py
│  │        │  │  │  ├─ test_show_versions.py
│  │        │  │  │  ├─ test_sparsefuncs.py
│  │        │  │  │  ├─ test_stats.py
│  │        │  │  │  ├─ test_tags.py
│  │        │  │  │  ├─ test_testing.py
│  │        │  │  │  ├─ test_typedefs.py
│  │        │  │  │  ├─ test_unique.py
│  │        │  │  │  ├─ test_user_interface.py
│  │        │  │  │  ├─ test_validation.py
│  │        │  │  │  ├─ test_weight_vector.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_arpack.cpython-312.pyc
│  │        │  │  │     ├─ test_arrayfuncs.cpython-312.pyc
│  │        │  │  │     ├─ test_array_api.cpython-312.pyc
│  │        │  │  │     ├─ test_bunch.cpython-312.pyc
│  │        │  │  │     ├─ test_chunking.cpython-312.pyc
│  │        │  │  │     ├─ test_class_weight.cpython-312.pyc
│  │        │  │  │     ├─ test_cython_blas.cpython-312.pyc
│  │        │  │  │     ├─ test_deprecation.cpython-312.pyc
│  │        │  │  │     ├─ test_encode.cpython-312.pyc
│  │        │  │  │     ├─ test_estimator_checks.cpython-312.pyc
│  │        │  │  │     ├─ test_extmath.cpython-312.pyc
│  │        │  │  │     ├─ test_fast_dict.cpython-312.pyc
│  │        │  │  │     ├─ test_fixes.cpython-312.pyc
│  │        │  │  │     ├─ test_graph.cpython-312.pyc
│  │        │  │  │     ├─ test_indexing.cpython-312.pyc
│  │        │  │  │     ├─ test_mask.cpython-312.pyc
│  │        │  │  │     ├─ test_metaestimators.cpython-312.pyc
│  │        │  │  │     ├─ test_missing.cpython-312.pyc
│  │        │  │  │     ├─ test_mocking.cpython-312.pyc
│  │        │  │  │     ├─ test_multiclass.cpython-312.pyc
│  │        │  │  │     ├─ test_murmurhash.cpython-312.pyc
│  │        │  │  │     ├─ test_optimize.cpython-312.pyc
│  │        │  │  │     ├─ test_parallel.cpython-312.pyc
│  │        │  │  │     ├─ test_param_validation.cpython-312.pyc
│  │        │  │  │     ├─ test_plotting.cpython-312.pyc
│  │        │  │  │     ├─ test_pprint.cpython-312.pyc
│  │        │  │  │     ├─ test_random.cpython-312.pyc
│  │        │  │  │     ├─ test_response.cpython-312.pyc
│  │        │  │  │     ├─ test_seq_dataset.cpython-312.pyc
│  │        │  │  │     ├─ test_set_output.cpython-312.pyc
│  │        │  │  │     ├─ test_shortest_path.cpython-312.pyc
│  │        │  │  │     ├─ test_show_versions.cpython-312.pyc
│  │        │  │  │     ├─ test_sparsefuncs.cpython-312.pyc
│  │        │  │  │     ├─ test_stats.cpython-312.pyc
│  │        │  │  │     ├─ test_tags.cpython-312.pyc
│  │        │  │  │     ├─ test_testing.cpython-312.pyc
│  │        │  │  │     ├─ test_typedefs.cpython-312.pyc
│  │        │  │  │     ├─ test_unique.cpython-312.pyc
│  │        │  │  │     ├─ test_user_interface.cpython-312.pyc
│  │        │  │  │     ├─ test_validation.cpython-312.pyc
│  │        │  │  │     ├─ test_weight_vector.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ validation.py
│  │        │  │  ├─ _arpack.py
│  │        │  │  ├─ _array_api.py
│  │        │  │  ├─ _available_if.py
│  │        │  │  ├─ _bunch.py
│  │        │  │  ├─ _chunking.py
│  │        │  │  ├─ _cython_blas.cpython-312-darwin.so
│  │        │  │  ├─ _cython_blas.pxd
│  │        │  │  ├─ _cython_blas.pyx
│  │        │  │  ├─ _encode.py
│  │        │  │  ├─ _fast_dict.cpython-312-darwin.so
│  │        │  │  ├─ _fast_dict.pxd
│  │        │  │  ├─ _fast_dict.pyx
│  │        │  │  ├─ _heap.cpython-312-darwin.so
│  │        │  │  ├─ _heap.pxd
│  │        │  │  ├─ _heap.pyx
│  │        │  │  ├─ _indexing.py
│  │        │  │  ├─ _isfinite.cpython-312-darwin.so
│  │        │  │  ├─ _isfinite.pyx
│  │        │  │  ├─ _mask.py
│  │        │  │  ├─ _metadata_requests.py
│  │        │  │  ├─ _missing.py
│  │        │  │  ├─ _mocking.py
│  │        │  │  ├─ _openmp_helpers.cpython-312-darwin.so
│  │        │  │  ├─ _openmp_helpers.pxd
│  │        │  │  ├─ _openmp_helpers.pyx
│  │        │  │  ├─ _optional_dependencies.py
│  │        │  │  ├─ _param_validation.py
│  │        │  │  ├─ _plotting.py
│  │        │  │  ├─ _pprint.py
│  │        │  │  ├─ _random.cpython-312-darwin.so
│  │        │  │  ├─ _random.pxd
│  │        │  │  ├─ _random.pyx
│  │        │  │  ├─ _repr_html
│  │        │  │  │  ├─ base.py
│  │        │  │  │  ├─ estimator.css
│  │        │  │  │  ├─ estimator.js
│  │        │  │  │  ├─ estimator.py
│  │        │  │  │  ├─ params.css
│  │        │  │  │  ├─ params.py
│  │        │  │  │  ├─ tests
│  │        │  │  │  │  ├─ test_estimator.py
│  │        │  │  │  │  ├─ test_params.py
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     ├─ test_estimator.cpython-312.pyc
│  │        │  │  │  │     ├─ test_params.cpython-312.pyc
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ base.cpython-312.pyc
│  │        │  │  │     ├─ estimator.cpython-312.pyc
│  │        │  │  │     ├─ params.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _response.py
│  │        │  │  ├─ _seq_dataset.cpython-312-darwin.so
│  │        │  │  ├─ _seq_dataset.pxd.tp
│  │        │  │  ├─ _seq_dataset.pyx.tp
│  │        │  │  ├─ _set_output.py
│  │        │  │  ├─ _show_versions.py
│  │        │  │  ├─ _sorting.cpython-312-darwin.so
│  │        │  │  ├─ _sorting.pxd
│  │        │  │  ├─ _sorting.pyx
│  │        │  │  ├─ _tags.py
│  │        │  │  ├─ _testing.py
│  │        │  │  ├─ _test_common
│  │        │  │  │  ├─ instance_generator.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ instance_generator.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _typedefs.cpython-312-darwin.so
│  │        │  │  ├─ _typedefs.pxd
│  │        │  │  ├─ _typedefs.pyx
│  │        │  │  ├─ _unique.py
│  │        │  │  ├─ _user_interface.py
│  │        │  │  ├─ _vector_sentinel.cpython-312-darwin.so
│  │        │  │  ├─ _vector_sentinel.pxd
│  │        │  │  ├─ _vector_sentinel.pyx
│  │        │  │  ├─ _weight_vector.cpython-312-darwin.so
│  │        │  │  ├─ _weight_vector.pxd.tp
│  │        │  │  ├─ _weight_vector.pyx.tp
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ class_weight.cpython-312.pyc
│  │        │  │     ├─ deprecation.cpython-312.pyc
│  │        │  │     ├─ discovery.cpython-312.pyc
│  │        │  │     ├─ estimator_checks.cpython-312.pyc
│  │        │  │     ├─ extmath.cpython-312.pyc
│  │        │  │     ├─ fixes.cpython-312.pyc
│  │        │  │     ├─ graph.cpython-312.pyc
│  │        │  │     ├─ metadata_routing.cpython-312.pyc
│  │        │  │     ├─ metaestimators.cpython-312.pyc
│  │        │  │     ├─ multiclass.cpython-312.pyc
│  │        │  │     ├─ optimize.cpython-312.pyc
│  │        │  │     ├─ parallel.cpython-312.pyc
│  │        │  │     ├─ random.cpython-312.pyc
│  │        │  │     ├─ sparsefuncs.cpython-312.pyc
│  │        │  │     ├─ stats.cpython-312.pyc
│  │        │  │     ├─ validation.cpython-312.pyc
│  │        │  │     ├─ _arpack.cpython-312.pyc
│  │        │  │     ├─ _array_api.cpython-312.pyc
│  │        │  │     ├─ _available_if.cpython-312.pyc
│  │        │  │     ├─ _bunch.cpython-312.pyc
│  │        │  │     ├─ _chunking.cpython-312.pyc
│  │        │  │     ├─ _encode.cpython-312.pyc
│  │        │  │     ├─ _indexing.cpython-312.pyc
│  │        │  │     ├─ _mask.cpython-312.pyc
│  │        │  │     ├─ _metadata_requests.cpython-312.pyc
│  │        │  │     ├─ _missing.cpython-312.pyc
│  │        │  │     ├─ _mocking.cpython-312.pyc
│  │        │  │     ├─ _optional_dependencies.cpython-312.pyc
│  │        │  │     ├─ _param_validation.cpython-312.pyc
│  │        │  │     ├─ _plotting.cpython-312.pyc
│  │        │  │     ├─ _pprint.cpython-312.pyc
│  │        │  │     ├─ _response.cpython-312.pyc
│  │        │  │     ├─ _set_output.cpython-312.pyc
│  │        │  │     ├─ _show_versions.cpython-312.pyc
│  │        │  │     ├─ _tags.cpython-312.pyc
│  │        │  │     ├─ _testing.cpython-312.pyc
│  │        │  │     ├─ _unique.cpython-312.pyc
│  │        │  │     ├─ _user_interface.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ _build_utils
│  │        │  │  ├─ tempita.py
│  │        │  │  ├─ version.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ tempita.cpython-312.pyc
│  │        │  │     ├─ version.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ _built_with_meson.py
│  │        │  ├─ _config.py
│  │        │  ├─ _distributor_init.py
│  │        │  ├─ _isotonic.cpython-312-darwin.so
│  │        │  ├─ _isotonic.pyx
│  │        │  ├─ _loss
│  │        │  │  ├─ link.py
│  │        │  │  ├─ loss.py
│  │        │  │  ├─ meson.build
│  │        │  │  ├─ tests
│  │        │  │  │  ├─ test_link.py
│  │        │  │  │  ├─ test_loss.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ test_link.cpython-312.pyc
│  │        │  │  │     ├─ test_loss.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ _loss.cpython-312-darwin.so
│  │        │  │  ├─ _loss.pxd
│  │        │  │  ├─ _loss.pyx.tp
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ link.cpython-312.pyc
│  │        │  │     ├─ loss.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ _min_dependencies.py
│  │        │  ├─ __check_build
│  │        │  │  ├─ meson.build
│  │        │  │  ├─ _check_build.cpython-312-darwin.so
│  │        │  │  ├─ _check_build.pyx
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     ├─ base.cpython-312.pyc
│  │        │     ├─ calibration.cpython-312.pyc
│  │        │     ├─ conftest.cpython-312.pyc
│  │        │     ├─ discriminant_analysis.cpython-312.pyc
│  │        │     ├─ dummy.cpython-312.pyc
│  │        │     ├─ exceptions.cpython-312.pyc
│  │        │     ├─ isotonic.cpython-312.pyc
│  │        │     ├─ kernel_approximation.cpython-312.pyc
│  │        │     ├─ kernel_ridge.cpython-312.pyc
│  │        │     ├─ multiclass.cpython-312.pyc
│  │        │     ├─ multioutput.cpython-312.pyc
│  │        │     ├─ naive_bayes.cpython-312.pyc
│  │        │     ├─ pipeline.cpython-312.pyc
│  │        │     ├─ random_projection.cpython-312.pyc
│  │        │     ├─ _built_with_meson.cpython-312.pyc
│  │        │     ├─ _config.cpython-312.pyc
│  │        │     ├─ _distributor_init.cpython-312.pyc
│  │        │     ├─ _min_dependencies.cpython-312.pyc
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ sniffio
│  │        │  ├─ py.typed
│  │        │  ├─ _impl.py
│  │        │  ├─ _tests
│  │        │  │  ├─ test_sniffio.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ test_sniffio.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ _version.py
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     ├─ _impl.cpython-312.pyc
│  │        │     ├─ _version.cpython-312.pyc
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ sniffio-1.3.1.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE
│  │        │  ├─ LICENSE.APACHE2
│  │        │  ├─ LICENSE.MIT
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ top_level.txt
│  │        │  └─ WHEEL
│  │        ├─ starlette
│  │        │  ├─ applications.py
│  │        │  ├─ authentication.py
│  │        │  ├─ background.py
│  │        │  ├─ concurrency.py
│  │        │  ├─ config.py
│  │        │  ├─ convertors.py
│  │        │  ├─ datastructures.py
│  │        │  ├─ endpoints.py
│  │        │  ├─ exceptions.py
│  │        │  ├─ formparsers.py
│  │        │  ├─ middleware
│  │        │  │  ├─ authentication.py
│  │        │  │  ├─ base.py
│  │        │  │  ├─ cors.py
│  │        │  │  ├─ errors.py
│  │        │  │  ├─ exceptions.py
│  │        │  │  ├─ gzip.py
│  │        │  │  ├─ httpsredirect.py
│  │        │  │  ├─ sessions.py
│  │        │  │  ├─ trustedhost.py
│  │        │  │  ├─ wsgi.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ authentication.cpython-312.pyc
│  │        │  │     ├─ base.cpython-312.pyc
│  │        │  │     ├─ cors.cpython-312.pyc
│  │        │  │     ├─ errors.cpython-312.pyc
│  │        │  │     ├─ exceptions.cpython-312.pyc
│  │        │  │     ├─ gzip.cpython-312.pyc
│  │        │  │     ├─ httpsredirect.cpython-312.pyc
│  │        │  │     ├─ sessions.cpython-312.pyc
│  │        │  │     ├─ trustedhost.cpython-312.pyc
│  │        │  │     ├─ wsgi.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ py.typed
│  │        │  ├─ requests.py
│  │        │  ├─ responses.py
│  │        │  ├─ routing.py
│  │        │  ├─ schemas.py
│  │        │  ├─ staticfiles.py
│  │        │  ├─ status.py
│  │        │  ├─ templating.py
│  │        │  ├─ testclient.py
│  │        │  ├─ types.py
│  │        │  ├─ websockets.py
│  │        │  ├─ _exception_handler.py
│  │        │  ├─ _utils.py
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     ├─ applications.cpython-312.pyc
│  │        │     ├─ authentication.cpython-312.pyc
│  │        │     ├─ background.cpython-312.pyc
│  │        │     ├─ concurrency.cpython-312.pyc
│  │        │     ├─ config.cpython-312.pyc
│  │        │     ├─ convertors.cpython-312.pyc
│  │        │     ├─ datastructures.cpython-312.pyc
│  │        │     ├─ endpoints.cpython-312.pyc
│  │        │     ├─ exceptions.cpython-312.pyc
│  │        │     ├─ formparsers.cpython-312.pyc
│  │        │     ├─ requests.cpython-312.pyc
│  │        │     ├─ responses.cpython-312.pyc
│  │        │     ├─ routing.cpython-312.pyc
│  │        │     ├─ schemas.cpython-312.pyc
│  │        │     ├─ staticfiles.cpython-312.pyc
│  │        │     ├─ status.cpython-312.pyc
│  │        │     ├─ templating.cpython-312.pyc
│  │        │     ├─ testclient.cpython-312.pyc
│  │        │     ├─ types.cpython-312.pyc
│  │        │     ├─ websockets.cpython-312.pyc
│  │        │     ├─ _exception_handler.cpython-312.pyc
│  │        │     ├─ _utils.cpython-312.pyc
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ starlette-0.46.2.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ licenses
│  │        │  │  └─ LICENSE.md
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  └─ WHEEL
│  │        ├─ threadpoolctl-3.6.0.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ licenses
│  │        │  │  └─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  └─ WHEEL
│  │        ├─ threadpoolctl.py
│  │        ├─ typer
│  │        │  ├─ cli.py
│  │        │  ├─ colors.py
│  │        │  ├─ completion.py
│  │        │  ├─ core.py
│  │        │  ├─ main.py
│  │        │  ├─ models.py
│  │        │  ├─ params.py
│  │        │  ├─ py.typed
│  │        │  ├─ rich_utils.py
│  │        │  ├─ testing.py
│  │        │  ├─ utils.py
│  │        │  ├─ _completion_classes.py
│  │        │  ├─ _completion_shared.py
│  │        │  ├─ _types.py
│  │        │  ├─ _typing.py
│  │        │  ├─ __init__.py
│  │        │  ├─ __main__.py
│  │        │  └─ __pycache__
│  │        │     ├─ cli.cpython-312.pyc
│  │        │     ├─ colors.cpython-312.pyc
│  │        │     ├─ completion.cpython-312.pyc
│  │        │     ├─ core.cpython-312.pyc
│  │        │     ├─ main.cpython-312.pyc
│  │        │     ├─ models.cpython-312.pyc
│  │        │     ├─ params.cpython-312.pyc
│  │        │     ├─ rich_utils.cpython-312.pyc
│  │        │     ├─ testing.cpython-312.pyc
│  │        │     ├─ utils.cpython-312.pyc
│  │        │     ├─ _completion_classes.cpython-312.pyc
│  │        │     ├─ _completion_shared.cpython-312.pyc
│  │        │     ├─ _types.cpython-312.pyc
│  │        │     ├─ _typing.cpython-312.pyc
│  │        │     ├─ __init__.cpython-312.pyc
│  │        │     └─ __main__.cpython-312.pyc
│  │        ├─ typer-0.16.0.dist-info
│  │        │  ├─ entry_points.txt
│  │        │  ├─ INSTALLER
│  │        │  ├─ licenses
│  │        │  │  └─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  └─ WHEEL
│  │        ├─ typing_extensions-4.13.2.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ licenses
│  │        │  │  └─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  └─ WHEEL
│  │        ├─ typing_extensions.py
│  │        ├─ typing_inspection
│  │        │  ├─ introspection.py
│  │        │  ├─ py.typed
│  │        │  ├─ typing_objects.py
│  │        │  ├─ typing_objects.pyi
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     ├─ introspection.cpython-312.pyc
│  │        │     ├─ typing_objects.cpython-312.pyc
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ typing_inspection-0.4.1.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ licenses
│  │        │  │  └─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  └─ WHEEL
│  │        ├─ tzdata
│  │        │  ├─ zoneinfo
│  │        │  │  ├─ Africa
│  │        │  │  │  ├─ Abidjan
│  │        │  │  │  ├─ Accra
│  │        │  │  │  ├─ Addis_Ababa
│  │        │  │  │  ├─ Algiers
│  │        │  │  │  ├─ Asmara
│  │        │  │  │  ├─ Asmera
│  │        │  │  │  ├─ Bamako
│  │        │  │  │  ├─ Bangui
│  │        │  │  │  ├─ Banjul
│  │        │  │  │  ├─ Bissau
│  │        │  │  │  ├─ Blantyre
│  │        │  │  │  ├─ Brazzaville
│  │        │  │  │  ├─ Bujumbura
│  │        │  │  │  ├─ Cairo
│  │        │  │  │  ├─ Casablanca
│  │        │  │  │  ├─ Ceuta
│  │        │  │  │  ├─ Conakry
│  │        │  │  │  ├─ Dakar
│  │        │  │  │  ├─ Dar_es_Salaam
│  │        │  │  │  ├─ Djibouti
│  │        │  │  │  ├─ Douala
│  │        │  │  │  ├─ El_Aaiun
│  │        │  │  │  ├─ Freetown
│  │        │  │  │  ├─ Gaborone
│  │        │  │  │  ├─ Harare
│  │        │  │  │  ├─ Johannesburg
│  │        │  │  │  ├─ Juba
│  │        │  │  │  ├─ Kampala
│  │        │  │  │  ├─ Khartoum
│  │        │  │  │  ├─ Kigali
│  │        │  │  │  ├─ Kinshasa
│  │        │  │  │  ├─ Lagos
│  │        │  │  │  ├─ Libreville
│  │        │  │  │  ├─ Lome
│  │        │  │  │  ├─ Luanda
│  │        │  │  │  ├─ Lubumbashi
│  │        │  │  │  ├─ Lusaka
│  │        │  │  │  ├─ Malabo
│  │        │  │  │  ├─ Maputo
│  │        │  │  │  ├─ Maseru
│  │        │  │  │  ├─ Mbabane
│  │        │  │  │  ├─ Mogadishu
│  │        │  │  │  ├─ Monrovia
│  │        │  │  │  ├─ Nairobi
│  │        │  │  │  ├─ Ndjamena
│  │        │  │  │  ├─ Niamey
│  │        │  │  │  ├─ Nouakchott
│  │        │  │  │  ├─ Ouagadougou
│  │        │  │  │  ├─ Porto-Novo
│  │        │  │  │  ├─ Sao_Tome
│  │        │  │  │  ├─ Timbuktu
│  │        │  │  │  ├─ Tripoli
│  │        │  │  │  ├─ Tunis
│  │        │  │  │  ├─ Windhoek
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ America
│  │        │  │  │  ├─ Adak
│  │        │  │  │  ├─ Anchorage
│  │        │  │  │  ├─ Anguilla
│  │        │  │  │  ├─ Antigua
│  │        │  │  │  ├─ Araguaina
│  │        │  │  │  ├─ Argentina
│  │        │  │  │  │  ├─ Buenos_Aires
│  │        │  │  │  │  ├─ Catamarca
│  │        │  │  │  │  ├─ ComodRivadavia
│  │        │  │  │  │  ├─ Cordoba
│  │        │  │  │  │  ├─ Jujuy
│  │        │  │  │  │  ├─ La_Rioja
│  │        │  │  │  │  ├─ Mendoza
│  │        │  │  │  │  ├─ Rio_Gallegos
│  │        │  │  │  │  ├─ Salta
│  │        │  │  │  │  ├─ San_Juan
│  │        │  │  │  │  ├─ San_Luis
│  │        │  │  │  │  ├─ Tucuman
│  │        │  │  │  │  ├─ Ushuaia
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ Aruba
│  │        │  │  │  ├─ Asuncion
│  │        │  │  │  ├─ Atikokan
│  │        │  │  │  ├─ Atka
│  │        │  │  │  ├─ Bahia
│  │        │  │  │  ├─ Bahia_Banderas
│  │        │  │  │  ├─ Barbados
│  │        │  │  │  ├─ Belem
│  │        │  │  │  ├─ Belize
│  │        │  │  │  ├─ Blanc-Sablon
│  │        │  │  │  ├─ Boa_Vista
│  │        │  │  │  ├─ Bogota
│  │        │  │  │  ├─ Boise
│  │        │  │  │  ├─ Buenos_Aires
│  │        │  │  │  ├─ Cambridge_Bay
│  │        │  │  │  ├─ Campo_Grande
│  │        │  │  │  ├─ Cancun
│  │        │  │  │  ├─ Caracas
│  │        │  │  │  ├─ Catamarca
│  │        │  │  │  ├─ Cayenne
│  │        │  │  │  ├─ Cayman
│  │        │  │  │  ├─ Chicago
│  │        │  │  │  ├─ Chihuahua
│  │        │  │  │  ├─ Ciudad_Juarez
│  │        │  │  │  ├─ Coral_Harbour
│  │        │  │  │  ├─ Cordoba
│  │        │  │  │  ├─ Costa_Rica
│  │        │  │  │  ├─ Coyhaique
│  │        │  │  │  ├─ Creston
│  │        │  │  │  ├─ Cuiaba
│  │        │  │  │  ├─ Curacao
│  │        │  │  │  ├─ Danmarkshavn
│  │        │  │  │  ├─ Dawson
│  │        │  │  │  ├─ Dawson_Creek
│  │        │  │  │  ├─ Denver
│  │        │  │  │  ├─ Detroit
│  │        │  │  │  ├─ Dominica
│  │        │  │  │  ├─ Edmonton
│  │        │  │  │  ├─ Eirunepe
│  │        │  │  │  ├─ El_Salvador
│  │        │  │  │  ├─ Ensenada
│  │        │  │  │  ├─ Fortaleza
│  │        │  │  │  ├─ Fort_Nelson
│  │        │  │  │  ├─ Fort_Wayne
│  │        │  │  │  ├─ Glace_Bay
│  │        │  │  │  ├─ Godthab
│  │        │  │  │  ├─ Goose_Bay
│  │        │  │  │  ├─ Grand_Turk
│  │        │  │  │  ├─ Grenada
│  │        │  │  │  ├─ Guadeloupe
│  │        │  │  │  ├─ Guatemala
│  │        │  │  │  ├─ Guayaquil
│  │        │  │  │  ├─ Guyana
│  │        │  │  │  ├─ Halifax
│  │        │  │  │  ├─ Havana
│  │        │  │  │  ├─ Hermosillo
│  │        │  │  │  ├─ Indiana
│  │        │  │  │  │  ├─ Indianapolis
│  │        │  │  │  │  ├─ Knox
│  │        │  │  │  │  ├─ Marengo
│  │        │  │  │  │  ├─ Petersburg
│  │        │  │  │  │  ├─ Tell_City
│  │        │  │  │  │  ├─ Vevay
│  │        │  │  │  │  ├─ Vincennes
│  │        │  │  │  │  ├─ Winamac
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ Indianapolis
│  │        │  │  │  ├─ Inuvik
│  │        │  │  │  ├─ Iqaluit
│  │        │  │  │  ├─ Jamaica
│  │        │  │  │  ├─ Jujuy
│  │        │  │  │  ├─ Juneau
│  │        │  │  │  ├─ Kentucky
│  │        │  │  │  │  ├─ Louisville
│  │        │  │  │  │  ├─ Monticello
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ Knox_IN
│  │        │  │  │  ├─ Kralendijk
│  │        │  │  │  ├─ La_Paz
│  │        │  │  │  ├─ Lima
│  │        │  │  │  ├─ Los_Angeles
│  │        │  │  │  ├─ Louisville
│  │        │  │  │  ├─ Lower_Princes
│  │        │  │  │  ├─ Maceio
│  │        │  │  │  ├─ Managua
│  │        │  │  │  ├─ Manaus
│  │        │  │  │  ├─ Marigot
│  │        │  │  │  ├─ Martinique
│  │        │  │  │  ├─ Matamoros
│  │        │  │  │  ├─ Mazatlan
│  │        │  │  │  ├─ Mendoza
│  │        │  │  │  ├─ Menominee
│  │        │  │  │  ├─ Merida
│  │        │  │  │  ├─ Metlakatla
│  │        │  │  │  ├─ Mexico_City
│  │        │  │  │  ├─ Miquelon
│  │        │  │  │  ├─ Moncton
│  │        │  │  │  ├─ Monterrey
│  │        │  │  │  ├─ Montevideo
│  │        │  │  │  ├─ Montreal
│  │        │  │  │  ├─ Montserrat
│  │        │  │  │  ├─ Nassau
│  │        │  │  │  ├─ New_York
│  │        │  │  │  ├─ Nipigon
│  │        │  │  │  ├─ Nome
│  │        │  │  │  ├─ Noronha
│  │        │  │  │  ├─ North_Dakota
│  │        │  │  │  │  ├─ Beulah
│  │        │  │  │  │  ├─ Center
│  │        │  │  │  │  ├─ New_Salem
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ __pycache__
│  │        │  │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  │  ├─ Nuuk
│  │        │  │  │  ├─ Ojinaga
│  │        │  │  │  ├─ Panama
│  │        │  │  │  ├─ Pangnirtung
│  │        │  │  │  ├─ Paramaribo
│  │        │  │  │  ├─ Phoenix
│  │        │  │  │  ├─ Port-au-Prince
│  │        │  │  │  ├─ Porto_Acre
│  │        │  │  │  ├─ Porto_Velho
│  │        │  │  │  ├─ Port_of_Spain
│  │        │  │  │  ├─ Puerto_Rico
│  │        │  │  │  ├─ Punta_Arenas
│  │        │  │  │  ├─ Rainy_River
│  │        │  │  │  ├─ Rankin_Inlet
│  │        │  │  │  ├─ Recife
│  │        │  │  │  ├─ Regina
│  │        │  │  │  ├─ Resolute
│  │        │  │  │  ├─ Rio_Branco
│  │        │  │  │  ├─ Rosario
│  │        │  │  │  ├─ Santarem
│  │        │  │  │  ├─ Santa_Isabel
│  │        │  │  │  ├─ Santiago
│  │        │  │  │  ├─ Santo_Domingo
│  │        │  │  │  ├─ Sao_Paulo
│  │        │  │  │  ├─ Scoresbysund
│  │        │  │  │  ├─ Shiprock
│  │        │  │  │  ├─ Sitka
│  │        │  │  │  ├─ St_Barthelemy
│  │        │  │  │  ├─ St_Johns
│  │        │  │  │  ├─ St_Kitts
│  │        │  │  │  ├─ St_Lucia
│  │        │  │  │  ├─ St_Thomas
│  │        │  │  │  ├─ St_Vincent
│  │        │  │  │  ├─ Swift_Current
│  │        │  │  │  ├─ Tegucigalpa
│  │        │  │  │  ├─ Thule
│  │        │  │  │  ├─ Thunder_Bay
│  │        │  │  │  ├─ Tijuana
│  │        │  │  │  ├─ Toronto
│  │        │  │  │  ├─ Tortola
│  │        │  │  │  ├─ Vancouver
│  │        │  │  │  ├─ Virgin
│  │        │  │  │  ├─ Whitehorse
│  │        │  │  │  ├─ Winnipeg
│  │        │  │  │  ├─ Yakutat
│  │        │  │  │  ├─ Yellowknife
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ Antarctica
│  │        │  │  │  ├─ Casey
│  │        │  │  │  ├─ Davis
│  │        │  │  │  ├─ DumontDUrville
│  │        │  │  │  ├─ Macquarie
│  │        │  │  │  ├─ Mawson
│  │        │  │  │  ├─ McMurdo
│  │        │  │  │  ├─ Palmer
│  │        │  │  │  ├─ Rothera
│  │        │  │  │  ├─ South_Pole
│  │        │  │  │  ├─ Syowa
│  │        │  │  │  ├─ Troll
│  │        │  │  │  ├─ Vostok
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ Arctic
│  │        │  │  │  ├─ Longyearbyen
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ Asia
│  │        │  │  │  ├─ Aden
│  │        │  │  │  ├─ Almaty
│  │        │  │  │  ├─ Amman
│  │        │  │  │  ├─ Anadyr
│  │        │  │  │  ├─ Aqtau
│  │        │  │  │  ├─ Aqtobe
│  │        │  │  │  ├─ Ashgabat
│  │        │  │  │  ├─ Ashkhabad
│  │        │  │  │  ├─ Atyrau
│  │        │  │  │  ├─ Baghdad
│  │        │  │  │  ├─ Bahrain
│  │        │  │  │  ├─ Baku
│  │        │  │  │  ├─ Bangkok
│  │        │  │  │  ├─ Barnaul
│  │        │  │  │  ├─ Beirut
│  │        │  │  │  ├─ Bishkek
│  │        │  │  │  ├─ Brunei
│  │        │  │  │  ├─ Calcutta
│  │        │  │  │  ├─ Chita
│  │        │  │  │  ├─ Choibalsan
│  │        │  │  │  ├─ Chongqing
│  │        │  │  │  ├─ Chungking
│  │        │  │  │  ├─ Colombo
│  │        │  │  │  ├─ Dacca
│  │        │  │  │  ├─ Damascus
│  │        │  │  │  ├─ Dhaka
│  │        │  │  │  ├─ Dili
│  │        │  │  │  ├─ Dubai
│  │        │  │  │  ├─ Dushanbe
│  │        │  │  │  ├─ Famagusta
│  │        │  │  │  ├─ Gaza
│  │        │  │  │  ├─ Harbin
│  │        │  │  │  ├─ Hebron
│  │        │  │  │  ├─ Hong_Kong
│  │        │  │  │  ├─ Hovd
│  │        │  │  │  ├─ Ho_Chi_Minh
│  │        │  │  │  ├─ Irkutsk
│  │        │  │  │  ├─ Istanbul
│  │        │  │  │  ├─ Jakarta
│  │        │  │  │  ├─ Jayapura
│  │        │  │  │  ├─ Jerusalem
│  │        │  │  │  ├─ Kabul
│  │        │  │  │  ├─ Kamchatka
│  │        │  │  │  ├─ Karachi
│  │        │  │  │  ├─ Kashgar
│  │        │  │  │  ├─ Kathmandu
│  │        │  │  │  ├─ Katmandu
│  │        │  │  │  ├─ Khandyga
│  │        │  │  │  ├─ Kolkata
│  │        │  │  │  ├─ Krasnoyarsk
│  │        │  │  │  ├─ Kuala_Lumpur
│  │        │  │  │  ├─ Kuching
│  │        │  │  │  ├─ Kuwait
│  │        │  │  │  ├─ Macao
│  │        │  │  │  ├─ Macau
│  │        │  │  │  ├─ Magadan
│  │        │  │  │  ├─ Makassar
│  │        │  │  │  ├─ Manila
│  │        │  │  │  ├─ Muscat
│  │        │  │  │  ├─ Nicosia
│  │        │  │  │  ├─ Novokuznetsk
│  │        │  │  │  ├─ Novosibirsk
│  │        │  │  │  ├─ Omsk
│  │        │  │  │  ├─ Oral
│  │        │  │  │  ├─ Phnom_Penh
│  │        │  │  │  ├─ Pontianak
│  │        │  │  │  ├─ Pyongyang
│  │        │  │  │  ├─ Qatar
│  │        │  │  │  ├─ Qostanay
│  │        │  │  │  ├─ Qyzylorda
│  │        │  │  │  ├─ Rangoon
│  │        │  │  │  ├─ Riyadh
│  │        │  │  │  ├─ Saigon
│  │        │  │  │  ├─ Sakhalin
│  │        │  │  │  ├─ Samarkand
│  │        │  │  │  ├─ Seoul
│  │        │  │  │  ├─ Shanghai
│  │        │  │  │  ├─ Singapore
│  │        │  │  │  ├─ Srednekolymsk
│  │        │  │  │  ├─ Taipei
│  │        │  │  │  ├─ Tashkent
│  │        │  │  │  ├─ Tbilisi
│  │        │  │  │  ├─ Tehran
│  │        │  │  │  ├─ Tel_Aviv
│  │        │  │  │  ├─ Thimbu
│  │        │  │  │  ├─ Thimphu
│  │        │  │  │  ├─ Tokyo
│  │        │  │  │  ├─ Tomsk
│  │        │  │  │  ├─ Ujung_Pandang
│  │        │  │  │  ├─ Ulaanbaatar
│  │        │  │  │  ├─ Ulan_Bator
│  │        │  │  │  ├─ Urumqi
│  │        │  │  │  ├─ Ust-Nera
│  │        │  │  │  ├─ Vientiane
│  │        │  │  │  ├─ Vladivostok
│  │        │  │  │  ├─ Yakutsk
│  │        │  │  │  ├─ Yangon
│  │        │  │  │  ├─ Yekaterinburg
│  │        │  │  │  ├─ Yerevan
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ Atlantic
│  │        │  │  │  ├─ Azores
│  │        │  │  │  ├─ Bermuda
│  │        │  │  │  ├─ Canary
│  │        │  │  │  ├─ Cape_Verde
│  │        │  │  │  ├─ Faeroe
│  │        │  │  │  ├─ Faroe
│  │        │  │  │  ├─ Jan_Mayen
│  │        │  │  │  ├─ Madeira
│  │        │  │  │  ├─ Reykjavik
│  │        │  │  │  ├─ South_Georgia
│  │        │  │  │  ├─ Stanley
│  │        │  │  │  ├─ St_Helena
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ Australia
│  │        │  │  │  ├─ ACT
│  │        │  │  │  ├─ Adelaide
│  │        │  │  │  ├─ Brisbane
│  │        │  │  │  ├─ Broken_Hill
│  │        │  │  │  ├─ Canberra
│  │        │  │  │  ├─ Currie
│  │        │  │  │  ├─ Darwin
│  │        │  │  │  ├─ Eucla
│  │        │  │  │  ├─ Hobart
│  │        │  │  │  ├─ LHI
│  │        │  │  │  ├─ Lindeman
│  │        │  │  │  ├─ Lord_Howe
│  │        │  │  │  ├─ Melbourne
│  │        │  │  │  ├─ North
│  │        │  │  │  ├─ NSW
│  │        │  │  │  ├─ Perth
│  │        │  │  │  ├─ Queensland
│  │        │  │  │  ├─ South
│  │        │  │  │  ├─ Sydney
│  │        │  │  │  ├─ Tasmania
│  │        │  │  │  ├─ Victoria
│  │        │  │  │  ├─ West
│  │        │  │  │  ├─ Yancowinna
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ Brazil
│  │        │  │  │  ├─ Acre
│  │        │  │  │  ├─ DeNoronha
│  │        │  │  │  ├─ East
│  │        │  │  │  ├─ West
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ Canada
│  │        │  │  │  ├─ Atlantic
│  │        │  │  │  ├─ Central
│  │        │  │  │  ├─ Eastern
│  │        │  │  │  ├─ Mountain
│  │        │  │  │  ├─ Newfoundland
│  │        │  │  │  ├─ Pacific
│  │        │  │  │  ├─ Saskatchewan
│  │        │  │  │  ├─ Yukon
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ CET
│  │        │  │  ├─ Chile
│  │        │  │  │  ├─ Continental
│  │        │  │  │  ├─ EasterIsland
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ CST6CDT
│  │        │  │  ├─ Cuba
│  │        │  │  ├─ EET
│  │        │  │  ├─ Egypt
│  │        │  │  ├─ Eire
│  │        │  │  ├─ EST
│  │        │  │  ├─ EST5EDT
│  │        │  │  ├─ Etc
│  │        │  │  │  ├─ GMT
│  │        │  │  │  ├─ GMT+0
│  │        │  │  │  ├─ GMT+1
│  │        │  │  │  ├─ GMT+10
│  │        │  │  │  ├─ GMT+11
│  │        │  │  │  ├─ GMT+12
│  │        │  │  │  ├─ GMT+2
│  │        │  │  │  ├─ GMT+3
│  │        │  │  │  ├─ GMT+4
│  │        │  │  │  ├─ GMT+5
│  │        │  │  │  ├─ GMT+6
│  │        │  │  │  ├─ GMT+7
│  │        │  │  │  ├─ GMT+8
│  │        │  │  │  ├─ GMT+9
│  │        │  │  │  ├─ GMT-0
│  │        │  │  │  ├─ GMT-1
│  │        │  │  │  ├─ GMT-10
│  │        │  │  │  ├─ GMT-11
│  │        │  │  │  ├─ GMT-12
│  │        │  │  │  ├─ GMT-13
│  │        │  │  │  ├─ GMT-14
│  │        │  │  │  ├─ GMT-2
│  │        │  │  │  ├─ GMT-3
│  │        │  │  │  ├─ GMT-4
│  │        │  │  │  ├─ GMT-5
│  │        │  │  │  ├─ GMT-6
│  │        │  │  │  ├─ GMT-7
│  │        │  │  │  ├─ GMT-8
│  │        │  │  │  ├─ GMT-9
│  │        │  │  │  ├─ GMT0
│  │        │  │  │  ├─ Greenwich
│  │        │  │  │  ├─ UCT
│  │        │  │  │  ├─ Universal
│  │        │  │  │  ├─ UTC
│  │        │  │  │  ├─ Zulu
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ Europe
│  │        │  │  │  ├─ Amsterdam
│  │        │  │  │  ├─ Andorra
│  │        │  │  │  ├─ Astrakhan
│  │        │  │  │  ├─ Athens
│  │        │  │  │  ├─ Belfast
│  │        │  │  │  ├─ Belgrade
│  │        │  │  │  ├─ Berlin
│  │        │  │  │  ├─ Bratislava
│  │        │  │  │  ├─ Brussels
│  │        │  │  │  ├─ Bucharest
│  │        │  │  │  ├─ Budapest
│  │        │  │  │  ├─ Busingen
│  │        │  │  │  ├─ Chisinau
│  │        │  │  │  ├─ Copenhagen
│  │        │  │  │  ├─ Dublin
│  │        │  │  │  ├─ Gibraltar
│  │        │  │  │  ├─ Guernsey
│  │        │  │  │  ├─ Helsinki
│  │        │  │  │  ├─ Isle_of_Man
│  │        │  │  │  ├─ Istanbul
│  │        │  │  │  ├─ Jersey
│  │        │  │  │  ├─ Kaliningrad
│  │        │  │  │  ├─ Kiev
│  │        │  │  │  ├─ Kirov
│  │        │  │  │  ├─ Kyiv
│  │        │  │  │  ├─ Lisbon
│  │        │  │  │  ├─ Ljubljana
│  │        │  │  │  ├─ London
│  │        │  │  │  ├─ Luxembourg
│  │        │  │  │  ├─ Madrid
│  │        │  │  │  ├─ Malta
│  │        │  │  │  ├─ Mariehamn
│  │        │  │  │  ├─ Minsk
│  │        │  │  │  ├─ Monaco
│  │        │  │  │  ├─ Moscow
│  │        │  │  │  ├─ Nicosia
│  │        │  │  │  ├─ Oslo
│  │        │  │  │  ├─ Paris
│  │        │  │  │  ├─ Podgorica
│  │        │  │  │  ├─ Prague
│  │        │  │  │  ├─ Riga
│  │        │  │  │  ├─ Rome
│  │        │  │  │  ├─ Samara
│  │        │  │  │  ├─ San_Marino
│  │        │  │  │  ├─ Sarajevo
│  │        │  │  │  ├─ Saratov
│  │        │  │  │  ├─ Simferopol
│  │        │  │  │  ├─ Skopje
│  │        │  │  │  ├─ Sofia
│  │        │  │  │  ├─ Stockholm
│  │        │  │  │  ├─ Tallinn
│  │        │  │  │  ├─ Tirane
│  │        │  │  │  ├─ Tiraspol
│  │        │  │  │  ├─ Ulyanovsk
│  │        │  │  │  ├─ Uzhgorod
│  │        │  │  │  ├─ Vaduz
│  │        │  │  │  ├─ Vatican
│  │        │  │  │  ├─ Vienna
│  │        │  │  │  ├─ Vilnius
│  │        │  │  │  ├─ Volgograd
│  │        │  │  │  ├─ Warsaw
│  │        │  │  │  ├─ Zagreb
│  │        │  │  │  ├─ Zaporozhye
│  │        │  │  │  ├─ Zurich
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ Factory
│  │        │  │  ├─ GB
│  │        │  │  ├─ GB-Eire
│  │        │  │  ├─ GMT
│  │        │  │  ├─ GMT+0
│  │        │  │  ├─ GMT-0
│  │        │  │  ├─ GMT0
│  │        │  │  ├─ Greenwich
│  │        │  │  ├─ Hongkong
│  │        │  │  ├─ HST
│  │        │  │  ├─ Iceland
│  │        │  │  ├─ Indian
│  │        │  │  │  ├─ Antananarivo
│  │        │  │  │  ├─ Chagos
│  │        │  │  │  ├─ Christmas
│  │        │  │  │  ├─ Cocos
│  │        │  │  │  ├─ Comoro
│  │        │  │  │  ├─ Kerguelen
│  │        │  │  │  ├─ Mahe
│  │        │  │  │  ├─ Maldives
│  │        │  │  │  ├─ Mauritius
│  │        │  │  │  ├─ Mayotte
│  │        │  │  │  ├─ Reunion
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ Iran
│  │        │  │  ├─ iso3166.tab
│  │        │  │  ├─ Israel
│  │        │  │  ├─ Jamaica
│  │        │  │  ├─ Japan
│  │        │  │  ├─ Kwajalein
│  │        │  │  ├─ leapseconds
│  │        │  │  ├─ Libya
│  │        │  │  ├─ MET
│  │        │  │  ├─ Mexico
│  │        │  │  │  ├─ BajaNorte
│  │        │  │  │  ├─ BajaSur
│  │        │  │  │  ├─ General
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ MST
│  │        │  │  ├─ MST7MDT
│  │        │  │  ├─ Navajo
│  │        │  │  ├─ NZ
│  │        │  │  ├─ NZ-CHAT
│  │        │  │  ├─ Pacific
│  │        │  │  │  ├─ Apia
│  │        │  │  │  ├─ Auckland
│  │        │  │  │  ├─ Bougainville
│  │        │  │  │  ├─ Chatham
│  │        │  │  │  ├─ Chuuk
│  │        │  │  │  ├─ Easter
│  │        │  │  │  ├─ Efate
│  │        │  │  │  ├─ Enderbury
│  │        │  │  │  ├─ Fakaofo
│  │        │  │  │  ├─ Fiji
│  │        │  │  │  ├─ Funafuti
│  │        │  │  │  ├─ Galapagos
│  │        │  │  │  ├─ Gambier
│  │        │  │  │  ├─ Guadalcanal
│  │        │  │  │  ├─ Guam
│  │        │  │  │  ├─ Honolulu
│  │        │  │  │  ├─ Johnston
│  │        │  │  │  ├─ Kanton
│  │        │  │  │  ├─ Kiritimati
│  │        │  │  │  ├─ Kosrae
│  │        │  │  │  ├─ Kwajalein
│  │        │  │  │  ├─ Majuro
│  │        │  │  │  ├─ Marquesas
│  │        │  │  │  ├─ Midway
│  │        │  │  │  ├─ Nauru
│  │        │  │  │  ├─ Niue
│  │        │  │  │  ├─ Norfolk
│  │        │  │  │  ├─ Noumea
│  │        │  │  │  ├─ Pago_Pago
│  │        │  │  │  ├─ Palau
│  │        │  │  │  ├─ Pitcairn
│  │        │  │  │  ├─ Pohnpei
│  │        │  │  │  ├─ Ponape
│  │        │  │  │  ├─ Port_Moresby
│  │        │  │  │  ├─ Rarotonga
│  │        │  │  │  ├─ Saipan
│  │        │  │  │  ├─ Samoa
│  │        │  │  │  ├─ Tahiti
│  │        │  │  │  ├─ Tarawa
│  │        │  │  │  ├─ Tongatapu
│  │        │  │  │  ├─ Truk
│  │        │  │  │  ├─ Wake
│  │        │  │  │  ├─ Wallis
│  │        │  │  │  ├─ Yap
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ Poland
│  │        │  │  ├─ Portugal
│  │        │  │  ├─ PRC
│  │        │  │  ├─ PST8PDT
│  │        │  │  ├─ ROC
│  │        │  │  ├─ ROK
│  │        │  │  ├─ Singapore
│  │        │  │  ├─ Turkey
│  │        │  │  ├─ tzdata.zi
│  │        │  │  ├─ UCT
│  │        │  │  ├─ Universal
│  │        │  │  ├─ US
│  │        │  │  │  ├─ Alaska
│  │        │  │  │  ├─ Aleutian
│  │        │  │  │  ├─ Arizona
│  │        │  │  │  ├─ Central
│  │        │  │  │  ├─ East-Indiana
│  │        │  │  │  ├─ Eastern
│  │        │  │  │  ├─ Hawaii
│  │        │  │  │  ├─ Indiana-Starke
│  │        │  │  │  ├─ Michigan
│  │        │  │  │  ├─ Mountain
│  │        │  │  │  ├─ Pacific
│  │        │  │  │  ├─ Samoa
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ UTC
│  │        │  │  ├─ W-SU
│  │        │  │  ├─ WET
│  │        │  │  ├─ zone.tab
│  │        │  │  ├─ zone1970.tab
│  │        │  │  ├─ zonenow.tab
│  │        │  │  ├─ Zulu
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ zones
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ tzdata-2025.2.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ licenses
│  │        │  │  ├─ LICENSE
│  │        │  │  └─ licenses
│  │        │  │     └─ LICENSE_APACHE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ top_level.txt
│  │        │  └─ WHEEL
│  │        ├─ ujson-5.10.0.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE.txt
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ top_level.txt
│  │        │  └─ WHEEL
│  │        ├─ ujson.cpython-312-darwin.so
│  │        ├─ uvicorn
│  │        │  ├─ config.py
│  │        │  ├─ importer.py
│  │        │  ├─ lifespan
│  │        │  │  ├─ off.py
│  │        │  │  ├─ on.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ off.cpython-312.pyc
│  │        │  │     ├─ on.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ logging.py
│  │        │  ├─ loops
│  │        │  │  ├─ asyncio.py
│  │        │  │  ├─ auto.py
│  │        │  │  ├─ uvloop.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ asyncio.cpython-312.pyc
│  │        │  │     ├─ auto.cpython-312.pyc
│  │        │  │     ├─ uvloop.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ main.py
│  │        │  ├─ middleware
│  │        │  │  ├─ asgi2.py
│  │        │  │  ├─ message_logger.py
│  │        │  │  ├─ proxy_headers.py
│  │        │  │  ├─ wsgi.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ asgi2.cpython-312.pyc
│  │        │  │     ├─ message_logger.cpython-312.pyc
│  │        │  │     ├─ proxy_headers.cpython-312.pyc
│  │        │  │     ├─ wsgi.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ protocols
│  │        │  │  ├─ http
│  │        │  │  │  ├─ auto.py
│  │        │  │  │  ├─ flow_control.py
│  │        │  │  │  ├─ h11_impl.py
│  │        │  │  │  ├─ httptools_impl.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ auto.cpython-312.pyc
│  │        │  │  │     ├─ flow_control.cpython-312.pyc
│  │        │  │  │     ├─ h11_impl.cpython-312.pyc
│  │        │  │  │     ├─ httptools_impl.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ utils.py
│  │        │  │  ├─ websockets
│  │        │  │  │  ├─ auto.py
│  │        │  │  │  ├─ websockets_impl.py
│  │        │  │  │  ├─ wsproto_impl.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ __pycache__
│  │        │  │  │     ├─ auto.cpython-312.pyc
│  │        │  │  │     ├─ websockets_impl.cpython-312.pyc
│  │        │  │  │     ├─ wsproto_impl.cpython-312.pyc
│  │        │  │  │     └─ __init__.cpython-312.pyc
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ utils.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ py.typed
│  │        │  ├─ server.py
│  │        │  ├─ supervisors
│  │        │  │  ├─ basereload.py
│  │        │  │  ├─ multiprocess.py
│  │        │  │  ├─ statreload.py
│  │        │  │  ├─ watchfilesreload.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ basereload.cpython-312.pyc
│  │        │  │     ├─ multiprocess.cpython-312.pyc
│  │        │  │     ├─ statreload.cpython-312.pyc
│  │        │  │     ├─ watchfilesreload.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ workers.py
│  │        │  ├─ _subprocess.py
│  │        │  ├─ _types.py
│  │        │  ├─ __init__.py
│  │        │  ├─ __main__.py
│  │        │  └─ __pycache__
│  │        │     ├─ config.cpython-312.pyc
│  │        │     ├─ importer.cpython-312.pyc
│  │        │     ├─ logging.cpython-312.pyc
│  │        │     ├─ main.cpython-312.pyc
│  │        │     ├─ server.cpython-312.pyc
│  │        │     ├─ workers.cpython-312.pyc
│  │        │     ├─ _subprocess.cpython-312.pyc
│  │        │     ├─ _types.cpython-312.pyc
│  │        │     ├─ __init__.cpython-312.pyc
│  │        │     └─ __main__.cpython-312.pyc
│  │        ├─ uvicorn-0.34.3.dist-info
│  │        │  ├─ entry_points.txt
│  │        │  ├─ INSTALLER
│  │        │  ├─ licenses
│  │        │  │  └─ LICENSE.md
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  └─ WHEEL
│  │        ├─ uvloop
│  │        │  ├─ cbhandles.pxd
│  │        │  ├─ cbhandles.pyx
│  │        │  ├─ dns.pyx
│  │        │  ├─ errors.pyx
│  │        │  ├─ handles
│  │        │  │  ├─ async_.pxd
│  │        │  │  ├─ async_.pyx
│  │        │  │  ├─ basetransport.pxd
│  │        │  │  ├─ basetransport.pyx
│  │        │  │  ├─ check.pxd
│  │        │  │  ├─ check.pyx
│  │        │  │  ├─ fsevent.pxd
│  │        │  │  ├─ fsevent.pyx
│  │        │  │  ├─ handle.pxd
│  │        │  │  ├─ handle.pyx
│  │        │  │  ├─ idle.pxd
│  │        │  │  ├─ idle.pyx
│  │        │  │  ├─ pipe.pxd
│  │        │  │  ├─ pipe.pyx
│  │        │  │  ├─ poll.pxd
│  │        │  │  ├─ poll.pyx
│  │        │  │  ├─ process.pxd
│  │        │  │  ├─ process.pyx
│  │        │  │  ├─ stream.pxd
│  │        │  │  ├─ stream.pyx
│  │        │  │  ├─ streamserver.pxd
│  │        │  │  ├─ streamserver.pyx
│  │        │  │  ├─ tcp.pxd
│  │        │  │  ├─ tcp.pyx
│  │        │  │  ├─ timer.pxd
│  │        │  │  ├─ timer.pyx
│  │        │  │  ├─ udp.pxd
│  │        │  │  └─ udp.pyx
│  │        │  ├─ includes
│  │        │  │  ├─ consts.pxi
│  │        │  │  ├─ debug.pxd
│  │        │  │  ├─ flowcontrol.pxd
│  │        │  │  ├─ python.pxd
│  │        │  │  ├─ stdlib.pxi
│  │        │  │  ├─ system.pxd
│  │        │  │  ├─ uv.pxd
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ loop.cpython-312-darwin.so
│  │        │  ├─ loop.pxd
│  │        │  ├─ loop.pyi
│  │        │  ├─ loop.pyx
│  │        │  ├─ lru.pyx
│  │        │  ├─ pseudosock.pyx
│  │        │  ├─ py.typed
│  │        │  ├─ request.pxd
│  │        │  ├─ request.pyx
│  │        │  ├─ server.pxd
│  │        │  ├─ server.pyx
│  │        │  ├─ sslproto.pxd
│  │        │  ├─ sslproto.pyx
│  │        │  ├─ _noop.py
│  │        │  ├─ _testbase.py
│  │        │  ├─ _version.py
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     ├─ _noop.cpython-312.pyc
│  │        │     ├─ _testbase.cpython-312.pyc
│  │        │     ├─ _version.cpython-312.pyc
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ uvloop-0.21.0.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE-APACHE
│  │        │  ├─ LICENSE-MIT
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ top_level.txt
│  │        │  └─ WHEEL
│  │        ├─ watchfiles
│  │        │  ├─ cli.py
│  │        │  ├─ filters.py
│  │        │  ├─ main.py
│  │        │  ├─ py.typed
│  │        │  ├─ run.py
│  │        │  ├─ version.py
│  │        │  ├─ _rust_notify.cpython-312-darwin.so
│  │        │  ├─ _rust_notify.pyi
│  │        │  ├─ __init__.py
│  │        │  ├─ __main__.py
│  │        │  └─ __pycache__
│  │        │     ├─ cli.cpython-312.pyc
│  │        │     ├─ filters.cpython-312.pyc
│  │        │     ├─ main.cpython-312.pyc
│  │        │     ├─ run.cpython-312.pyc
│  │        │     ├─ version.cpython-312.pyc
│  │        │     ├─ __init__.cpython-312.pyc
│  │        │     └─ __main__.cpython-312.pyc
│  │        ├─ watchfiles-1.0.5.dist-info
│  │        │  ├─ entry_points.txt
│  │        │  ├─ INSTALLER
│  │        │  ├─ licenses
│  │        │  │  └─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  └─ WHEEL
│  │        ├─ websockets
│  │        │  ├─ asyncio
│  │        │  │  ├─ async_timeout.py
│  │        │  │  ├─ client.py
│  │        │  │  ├─ compatibility.py
│  │        │  │  ├─ connection.py
│  │        │  │  ├─ messages.py
│  │        │  │  ├─ router.py
│  │        │  │  ├─ server.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ async_timeout.cpython-312.pyc
│  │        │  │     ├─ client.cpython-312.pyc
│  │        │  │     ├─ compatibility.cpython-312.pyc
│  │        │  │     ├─ connection.cpython-312.pyc
│  │        │  │     ├─ messages.cpython-312.pyc
│  │        │  │     ├─ router.cpython-312.pyc
│  │        │  │     ├─ server.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ auth.py
│  │        │  ├─ cli.py
│  │        │  ├─ client.py
│  │        │  ├─ connection.py
│  │        │  ├─ datastructures.py
│  │        │  ├─ exceptions.py
│  │        │  ├─ extensions
│  │        │  │  ├─ base.py
│  │        │  │  ├─ permessage_deflate.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ base.cpython-312.pyc
│  │        │  │     ├─ permessage_deflate.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ frames.py
│  │        │  ├─ headers.py
│  │        │  ├─ http.py
│  │        │  ├─ http11.py
│  │        │  ├─ imports.py
│  │        │  ├─ legacy
│  │        │  │  ├─ auth.py
│  │        │  │  ├─ client.py
│  │        │  │  ├─ exceptions.py
│  │        │  │  ├─ framing.py
│  │        │  │  ├─ handshake.py
│  │        │  │  ├─ http.py
│  │        │  │  ├─ protocol.py
│  │        │  │  ├─ server.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ auth.cpython-312.pyc
│  │        │  │     ├─ client.cpython-312.pyc
│  │        │  │     ├─ exceptions.cpython-312.pyc
│  │        │  │     ├─ framing.cpython-312.pyc
│  │        │  │     ├─ handshake.cpython-312.pyc
│  │        │  │     ├─ http.cpython-312.pyc
│  │        │  │     ├─ protocol.cpython-312.pyc
│  │        │  │     ├─ server.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ protocol.py
│  │        │  ├─ py.typed
│  │        │  ├─ server.py
│  │        │  ├─ speedups.c
│  │        │  ├─ speedups.cpython-312-darwin.so
│  │        │  ├─ speedups.pyi
│  │        │  ├─ streams.py
│  │        │  ├─ sync
│  │        │  │  ├─ client.py
│  │        │  │  ├─ connection.py
│  │        │  │  ├─ messages.py
│  │        │  │  ├─ router.py
│  │        │  │  ├─ server.py
│  │        │  │  ├─ utils.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ client.cpython-312.pyc
│  │        │  │     ├─ connection.cpython-312.pyc
│  │        │  │     ├─ messages.cpython-312.pyc
│  │        │  │     ├─ router.cpython-312.pyc
│  │        │  │     ├─ server.cpython-312.pyc
│  │        │  │     ├─ utils.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ typing.py
│  │        │  ├─ uri.py
│  │        │  ├─ utils.py
│  │        │  ├─ version.py
│  │        │  ├─ __init__.py
│  │        │  ├─ __main__.py
│  │        │  └─ __pycache__
│  │        │     ├─ auth.cpython-312.pyc
│  │        │     ├─ cli.cpython-312.pyc
│  │        │     ├─ client.cpython-312.pyc
│  │        │     ├─ connection.cpython-312.pyc
│  │        │     ├─ datastructures.cpython-312.pyc
│  │        │     ├─ exceptions.cpython-312.pyc
│  │        │     ├─ frames.cpython-312.pyc
│  │        │     ├─ headers.cpython-312.pyc
│  │        │     ├─ http.cpython-312.pyc
│  │        │     ├─ http11.cpython-312.pyc
│  │        │     ├─ imports.cpython-312.pyc
│  │        │     ├─ protocol.cpython-312.pyc
│  │        │     ├─ server.cpython-312.pyc
│  │        │     ├─ streams.cpython-312.pyc
│  │        │     ├─ typing.cpython-312.pyc
│  │        │     ├─ uri.cpython-312.pyc
│  │        │     ├─ utils.cpython-312.pyc
│  │        │     ├─ version.cpython-312.pyc
│  │        │     ├─ __init__.cpython-312.pyc
│  │        │     └─ __main__.cpython-312.pyc
│  │        ├─ websockets-15.0.1.dist-info
│  │        │  ├─ entry_points.txt
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ top_level.txt
│  │        │  └─ WHEEL
│  │        ├─ xgboost
│  │        │  ├─ callback.py
│  │        │  ├─ collective.py
│  │        │  ├─ compat.py
│  │        │  ├─ config.py
│  │        │  ├─ core.py
│  │        │  ├─ dask
│  │        │  │  ├─ data.py
│  │        │  │  ├─ utils.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ data.cpython-312.pyc
│  │        │  │     ├─ utils.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ data.py
│  │        │  ├─ federated.py
│  │        │  ├─ lib
│  │        │  │  └─ libxgboost.dylib
│  │        │  ├─ libpath.py
│  │        │  ├─ plotting.py
│  │        │  ├─ py.typed
│  │        │  ├─ sklearn.py
│  │        │  ├─ spark
│  │        │  │  ├─ core.py
│  │        │  │  ├─ data.py
│  │        │  │  ├─ estimator.py
│  │        │  │  ├─ params.py
│  │        │  │  ├─ summary.py
│  │        │  │  ├─ utils.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ core.cpython-312.pyc
│  │        │  │     ├─ data.cpython-312.pyc
│  │        │  │     ├─ estimator.cpython-312.pyc
│  │        │  │     ├─ params.cpython-312.pyc
│  │        │  │     ├─ summary.cpython-312.pyc
│  │        │  │     ├─ utils.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ testing
│  │        │  │  ├─ continuation.py
│  │        │  │  ├─ dask.py
│  │        │  │  ├─ data.py
│  │        │  │  ├─ data_iter.py
│  │        │  │  ├─ federated.py
│  │        │  │  ├─ metrics.py
│  │        │  │  ├─ params.py
│  │        │  │  ├─ quantile_dmatrix.py
│  │        │  │  ├─ ranking.py
│  │        │  │  ├─ shared.py
│  │        │  │  ├─ updater.py
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     ├─ continuation.cpython-312.pyc
│  │        │  │     ├─ dask.cpython-312.pyc
│  │        │  │     ├─ data.cpython-312.pyc
│  │        │  │     ├─ data_iter.cpython-312.pyc
│  │        │  │     ├─ federated.cpython-312.pyc
│  │        │  │     ├─ metrics.cpython-312.pyc
│  │        │  │     ├─ params.cpython-312.pyc
│  │        │  │     ├─ quantile_dmatrix.cpython-312.pyc
│  │        │  │     ├─ ranking.cpython-312.pyc
│  │        │  │     ├─ shared.cpython-312.pyc
│  │        │  │     ├─ updater.cpython-312.pyc
│  │        │  │     └─ __init__.cpython-312.pyc
│  │        │  ├─ tracker.py
│  │        │  ├─ training.py
│  │        │  ├─ VERSION
│  │        │  ├─ _data_utils.py
│  │        │  ├─ _typing.py
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     ├─ callback.cpython-312.pyc
│  │        │     ├─ collective.cpython-312.pyc
│  │        │     ├─ compat.cpython-312.pyc
│  │        │     ├─ config.cpython-312.pyc
│  │        │     ├─ core.cpython-312.pyc
│  │        │     ├─ data.cpython-312.pyc
│  │        │     ├─ federated.cpython-312.pyc
│  │        │     ├─ libpath.cpython-312.pyc
│  │        │     ├─ plotting.cpython-312.pyc
│  │        │     ├─ sklearn.cpython-312.pyc
│  │        │     ├─ tracker.cpython-312.pyc
│  │        │     ├─ training.cpython-312.pyc
│  │        │     ├─ _data_utils.cpython-312.pyc
│  │        │     ├─ _typing.cpython-312.pyc
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ xgboost-3.0.2.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ REQUESTED
│  │        │  └─ WHEEL
│  │        ├─ yaml
│  │        │  ├─ composer.py
│  │        │  ├─ constructor.py
│  │        │  ├─ cyaml.py
│  │        │  ├─ dumper.py
│  │        │  ├─ emitter.py
│  │        │  ├─ error.py
│  │        │  ├─ events.py
│  │        │  ├─ loader.py
│  │        │  ├─ nodes.py
│  │        │  ├─ parser.py
│  │        │  ├─ reader.py
│  │        │  ├─ representer.py
│  │        │  ├─ resolver.py
│  │        │  ├─ scanner.py
│  │        │  ├─ serializer.py
│  │        │  ├─ tokens.py
│  │        │  ├─ _yaml.cpython-312-darwin.so
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     ├─ composer.cpython-312.pyc
│  │        │     ├─ constructor.cpython-312.pyc
│  │        │     ├─ cyaml.cpython-312.pyc
│  │        │     ├─ dumper.cpython-312.pyc
│  │        │     ├─ emitter.cpython-312.pyc
│  │        │     ├─ error.cpython-312.pyc
│  │        │     ├─ events.cpython-312.pyc
│  │        │     ├─ loader.cpython-312.pyc
│  │        │     ├─ nodes.cpython-312.pyc
│  │        │     ├─ parser.cpython-312.pyc
│  │        │     ├─ reader.cpython-312.pyc
│  │        │     ├─ representer.cpython-312.pyc
│  │        │     ├─ resolver.cpython-312.pyc
│  │        │     ├─ scanner.cpython-312.pyc
│  │        │     ├─ serializer.cpython-312.pyc
│  │        │     ├─ tokens.cpython-312.pyc
│  │        │     └─ __init__.cpython-312.pyc
│  │        ├─ _yaml
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     └─ __init__.cpython-312.pyc
│  │        └─ __pycache__
│  │           ├─ six.cpython-312.pyc
│  │           ├─ threadpoolctl.cpython-312.pyc
│  │           └─ typing_extensions.cpython-312.pyc
│  └─ pyvenv.cfg
├─ vite.config.ts
└─ __pycache__
   ├─ database.cpython-312.pyc
   ├─ main.cpython-312.pyc
   └─ simulations.cpython-312.pyc

```