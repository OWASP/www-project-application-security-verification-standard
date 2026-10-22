@echo off
setlocal
pushd "%~dp0"
if errorlevel 1 exit /b 1

where ruby >nul 2>&1
if errorlevel 1 (
    echo Ruby is required. Install Ruby 4.0.7 with Devkit from https://rubyinstaller.org/downloads/
    echo Run the installer's MSYS2 toolchain setup, then open this file again.
    goto :failed
)

rem Use Windows trust for Ruby HTTPS unless a CA file is already configured.
if defined SSL_CERT_FILE goto :certificates_ready
set "ASVS_CA_FILE=%TEMP%\asvs-ca-%RANDOM%-%RANDOM%.pem"
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\export-windows-ca.ps1" -Destination "%ASVS_CA_FILE%"
if errorlevel 1 goto :failed
set "SSL_CERT_FILE=%ASVS_CA_FILE%"
if not defined BUNDLE_SSL_CA_CERT set "BUNDLE_SSL_CA_CERT=%ASVS_CA_FILE%"
:certificates_ready

where bundle >nul 2>&1
if errorlevel 1 (
    echo Installing Bundler...
    call gem install bundler --no-document
    if errorlevel 1 goto :failed
)

ruby -e "exit(Gem::Requirement.new('~> 4.0', '>= 4.0.7').satisfied_by?(Gem::Version.new(RUBY_VERSION)) ? 0 : 1)"
if errorlevel 1 (
    echo This site requires Ruby 4.0.7 or a newer Ruby 4.x release.
    echo Check ruby --version and install Ruby with Devkit from https://rubyinstaller.org/downloads/
    goto :failed
)

rem Fail early if Ruby's encoding extension is missing or cannot be loaded.
ruby -e "s = 'test'.encode('UTF-16BE'); abort('Unexpected encoding result') unless s.encoding.name == 'UTF-16BE'"
if errorlevel 1 (
    echo Ruby's UTF-16BE encoding support failed before dependency installation.
    echo Repair or reinstall Ruby 4.0.7 with Devkit, then open a new terminal.
    goto :failed
)

rem Keep downloaded gems in this checkout.
set "BUNDLE_PATH=vendor/bundle"
set "JEKYLL_ENV=development"
call bundle check >nul 2>&1
if errorlevel 1 (
    echo Installing site dependencies. The first run may take a few minutes...
    call bundle install
    if errorlevel 1 goto :failed
)

echo.
echo Starting the ASVS website at http://127.0.0.1:4000/
echo Wait for Jekyll's Server running message, then open that address in your browser.
echo Keep this window open. Press Ctrl+C to stop the server.
echo.
call bundle exec jekyll serve --host 127.0.0.1 --port 4000 --baseurl ""
if errorlevel 1 goto :failed
if defined ASVS_CA_FILE del /q "%ASVS_CA_FILE%" >nul 2>&1
popd
endlocal
exit /b 0

:failed
if defined ASVS_CA_FILE del /q "%ASVS_CA_FILE%" >nul 2>&1
echo.
echo Could not start the website. See the error above.
echo If native gem compilation failed, run ridk install to install the Ruby Devkit toolchain.
echo If port 4000 is in use, stop the other server and try again.
pause
popd
endlocal
exit /b 1
