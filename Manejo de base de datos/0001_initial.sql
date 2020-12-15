BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS 'currency' (
    'code' TEXT,
    'name' TEXT,
    'symbol' TEXT,
    PRIMARY KEY('code')
);

COMMIT;