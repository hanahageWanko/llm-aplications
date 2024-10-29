CREATE SEQUENCE auth_permission_sequence START 1 INCREMENT 1;
CREATE TABLE IF NOT EXISTS "django_admin_log" (
    "id" integer NOT NULL PRIMARY KEY,
    "action_time" date NOT NULL,
    "user_id" integer NOT NULL,
    "content_type_id" integer,
    "object_id" text,
    "object_repr" varchar(200) NOT NULL,
    "action_flag" smallint NOT NULL,
    "change_message" text NOT NULL
);
CREATE TABLE IF NOT EXISTS "auth_permission" (
    "id" integer NOT NULL PRIMARY KEY DEFAULT nextval('auth_permission_sequence'),
    "name" varchar(50) NOT NULL,
    "content_type_id" integer NOT NULL,
    "codename" varchar(100) NOT NULL,
    UNIQUE ("content_type_id", "codename")
);
CREATE TABLE IF NOT EXISTS "auth_group_permissions" (
    "id" integer NOT NULL PRIMARY KEY,
    "group_id" integer NOT NULL,
    "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id"),
    UNIQUE ("group_id", "permission_id")
);
CREATE TABLE IF NOT EXISTS "auth_group" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(80) NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS "auth_user_groups" (
    "id" integer NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL,
    "group_id" integer NOT NULL REFERENCES "auth_group" ("id"),
    UNIQUE ("user_id", "group_id")
);
CREATE TABLE IF NOT EXISTS "auth_user_user_permissions" (
    "id" integer NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL,
    "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id"),
    UNIQUE ("user_id", "permission_id")
);
CREATE TABLE IF NOT EXISTS "auth_user" (
    "id" integer NOT NULL PRIMARY KEY,
    "password" varchar(128) NOT NULL,
    "last_login" date NOT NULL,
    "is_superuser" bool NOT NULL,
    "username" varchar(30) NOT NULL UNIQUE,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL,
    "email" varchar(75) NOT NULL,
    "is_staff" bool NOT NULL,
    "is_active" bool NOT NULL,
    "date_joined" date NOT NULL
);
CREATE TABLE IF NOT EXISTS "django_content_type" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(100) NOT NULL,
    "app_label" varchar(100) NOT NULL,
    "model" varchar(100) NOT NULL,
    UNIQUE ("app_label", "model")
);
CREATE TABLE IF NOT EXISTS "django_session" (
    "session_key" varchar(40) NOT NULL PRIMARY KEY,
    "session_data" text NOT NULL,
    "expire_date" date NOT NULL
);
CREATE TABLE IF NOT EXISTS "products_category" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(30) NOT NULL,
    "created_at" date NOT NULL
);
CREATE TABLE IF NOT EXISTS "products_product" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(255) NOT NULL,
    "category_id" integer NOT NULL REFERENCES "products_category" ("id"),
    "created_at" date NOT NULL,
    "updated_at" date NOT NULL,
    "deleted_at" date
);
CREATE TABLE IF NOT EXISTS "products_price" (
    "id" integer NOT NULL PRIMARY KEY,
    "price" integer NOT NULL,
    "product_id" integer NOT NULL REFERENCES "products_product" ("id"),
    "effective_date_start" date,
    "effective_date_end" date
);
CREATE TABLE IF NOT EXISTS "sales_sales" (
    "id" integer NOT NULL PRIMARY KEY,
    "product_id" integer NOT NULL REFERENCES "products_product" ("id"),
    "sold_at" date NOT NULL
);
CREATE TABLE IF NOT EXISTS "sales_summary" (
    "id" integer NOT NULL PRIMARY KEY,
    "date" date NOT NULL,
    "total_sales" integer NOT NULL,
    "total_price" integer NOT NULL,
    "unique_user" integer NOT NULL
);
CREATE INDEX "django_admin_log_6340c63c" ON "django_admin_log" ("user_id");
CREATE INDEX "django_admin_log_37ef4eb4" ON "django_admin_log" ("content_type_id");
CREATE INDEX "auth_permission_37ef4eb4" ON "auth_permission" ("content_type_id");
CREATE INDEX "auth_group_permissions_5f412f9a" ON "auth_group_permissions" ("group_id");
CREATE INDEX "auth_group_permissions_83d7f98b" ON "auth_group_permissions" ("permission_id");
CREATE INDEX "auth_user_groups_6340c63c" ON "auth_user_groups" ("user_id");
CREATE INDEX "auth_user_groups_5f412f9a" ON "auth_user_groups" ("group_id");
CREATE INDEX "auth_user_user_permissions_6340c63c" ON "auth_user_user_permissions" ("user_id");
CREATE INDEX "auth_user_user_permissions_83d7f98b" ON "auth_user_user_permissions" ("permission_id");
CREATE INDEX "django_session_b7b81f0c" ON "django_session" ("expire_date");
CREATE INDEX "products_product_6f33f001" ON "products_product" ("category_id");
CREATE INDEX "products_price_7f1b40ad" ON "products_price" ("product_id");
CREATE INDEX "sales_sales_7f1b40ad" ON "sales_sales" ("product_id");