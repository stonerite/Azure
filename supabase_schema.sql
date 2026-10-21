-- ==============================================================================
-- Azure Buddy AI - Production Supabase Database Schema
-- Run this in your Supabase Dashboard -> SQL Editor -> New Query -> Run
-- ==============================================================================

-- 1. Create Sessions Table (With User Privacy Isolation)
create table if not exists public.sessions (
    id text default gen_random_uuid()::text primary key,
    user_id text not null default 'anonymous',
    title text not null default 'New Study Session',
    language text default 'English',
    created_at timestamp with time zone default timezone('utc'::text, now()) not null,
    updated_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- Ensure user_id column exists if table was created previously
alter table public.sessions add column if not exists user_id text not null default 'anonymous';

-- 2. Create Messages Table
create table if not exists public.messages (
    id text default gen_random_uuid()::text primary key,
    session_id text references public.sessions(id) on delete cascade not null,
    role text not null check (role in ('user', 'assistant', 'system')),
    content text not null,
    metadata jsonb default '{}'::jsonb,
    created_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- 3. Create Quiz Attempts Table (Tracks score & weak areas)
create table if not exists public.quiz_attempts (
    id text default gen_random_uuid()::text primary key,
    session_id text references public.sessions(id) on delete cascade,
    question_id integer,
    topic text,
    selected_option text,
    is_correct boolean not null,
    created_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- 4. Enable Row Level Security (RLS)
alter table public.sessions enable row level security;
alter table public.messages enable row level security;
alter table public.quiz_attempts enable row level security;

-- 5. Access Policies (Public / Anonymous)
drop policy if exists "Allow public access to sessions" on public.sessions;
create policy "Allow public access to sessions" on public.sessions for all using (true) with check (true);

drop policy if exists "Allow public access to messages" on public.messages;
create policy "Allow public access to messages" on public.messages for all using (true) with check (true);

drop policy if exists "Allow public access to quiz_attempts" on public.quiz_attempts;
create policy "Allow public access to quiz_attempts" on public.quiz_attempts for all using (true) with check (true);

-- 6. Performance & Privacy Indexing
create index if not exists idx_sessions_user_id on public.sessions(user_id);
create index if not exists idx_messages_session_id on public.messages(session_id);
create index if not exists idx_messages_created_at on public.messages(created_at asc);
create index if not exists idx_quiz_session_id on public.quiz_attempts(session_id);
create index if not exists idx_sessions_updated_at on public.sessions(updated_at desc);
