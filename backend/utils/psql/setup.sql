-- ANSI SQL
-- Create Role
CREATE ROLE admin WITH SUPERUSER CREATEDROLE LOGIN;

-- Create a read-only role (no login)
CREATE ROLE read_only;

-- Create a read-write role
CREATE ROLE read_write;

-----------------------------------------
-- Create users
-----------------------------------------
CREATE USER root WITH PASSWORD 'iNwPlmwXD3z7K8yxGVmL';
CREATE USER kumbi WITH PASSWORD 'Cc_Jm8bw-DeHW1FjbWQ';
CREATE USER reader WITH PASSWORD '8J_m0w-3ZeHW1Xj1WQ';

-- Assing roles to users
GRANT admin TO root;
GRANT read_only TO reader;
GRANT read_write TO kumbi;

--- GRANT SELECT PRIVILEGES on all tables in a specific schema
GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA public TO admin;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO read_only;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO read_write;

-- Grant read-write privileges to the `read_write` rol
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO read_write;

-- Grant specific privileges for future tables automatically (optional)
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO read_only;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO read_write;

-- Create database
CREATE DATABASE kumbivote WITH OWNER kumbi;
GRANT ALL PRIVILEGES ON DATABASE kumbivote TO kumbi;
GRANT CONNECT, SELECT ON ALL TABLES IN DATABASE kumbivote TO reader;
