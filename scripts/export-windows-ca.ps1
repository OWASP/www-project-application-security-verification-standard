param([Parameter(Mandatory = $true)][string]$Destination)

$ErrorActionPreference = 'Stop'
# Ruby's OpenSSL does not automatically use the Windows certificate stores.
$certificates = foreach ($location in 'CurrentUser', 'LocalMachine') {
    $store = New-Object System.Security.Cryptography.X509Certificates.X509Store('Root', $location)
    try {
        $store.Open([System.Security.Cryptography.X509Certificates.OpenFlags]::ReadOnly)
        $store.Certificates
    } finally {
        $store.Close()
    }
}
$certificates = $certificates | Sort-Object Thumbprint -Unique
if (-not $certificates) {
    throw 'No trusted Windows root certificates were found.'
}
$pem = foreach ($certificate in $certificates) {
    '-----BEGIN CERTIFICATE-----'
    [Convert]::ToBase64String($certificate.RawData, [Base64FormattingOptions]::InsertLineBreaks)
    '-----END CERTIFICATE-----'
}
[IO.File]::WriteAllLines($Destination, $pem, [Text.Encoding]::ASCII)
