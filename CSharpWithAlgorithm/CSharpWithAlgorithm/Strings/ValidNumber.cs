using CSharpWithAlgorithm.Interfaces;

namespace CSharpWithAlgorithm.Strings;

public sealed class ValidNumber : ISolution<bool>
{
    private const char positiveSign = '+';
    private const char negativeSign = '-';

    private const string digits = "0123456789";

    private const char dot = '.';

    private const char lowerExponent = 'e';

    private const char upperExponent = 'E';

    private readonly string s;





    private class CharacterRuleSchema
    {
        private List<char> _spaces = new();

        private IDictionary<char, CharacterEntry> _entryMap = new Dictionary<char, CharacterEntry>();

        public IEnumerable<CharacterEntry> AllEntries
            => _entryMap.Values;

        public bool HasCharacter(char c)
        { return _spaces.Contains(c); }

        public CharacterEntry WithEntryOf(char c)
        {
            if (_entryMap.TryGetValue(c, out var entry))
                return entry;
            _entryMap[c] = new CharacterEntry { Character = c };

            return _entryMap[c];
        }

        public CharacterRuleSchema HasAllCharacter(char[] characters)
        {
            _spaces = characters.ToList();
            return this;
        }


        public CharacterRuleSchema ConfigRule(char entryKey, Action<CharacterEntry> configureFunc)
        {
            if (!_spaces.Contains(entryKey))
                throw new ArgumentException("Invalid entryKey", nameof(entryKey));

            var entry = WithEntryOf(entryKey);

            configureFunc(entry);

            return this;
        }

        public CharacterRuleSchema ConfigGroupRule(string entryKeys, Action<CharacterEntry> configureFunc)
        {
            if (!entryKeys.ToHashSet().IsSubsetOf(_spaces.ToHashSet()))
                throw new ArgumentException("Invalid entryKeys", nameof(entryKeys));

            foreach (var entryKey in entryKeys)
                ConfigRule(entryKey, configureFunc);

            return this;
        }

        public CharacterRuleSchema HasAllPossibleCharacters(string sequence)
        {
            _spaces = sequence.ToList();
            return this;
        }

        public CharacterRuleSchema()
        {

        }
    }


    private class CharacterSequenceEngine
    {
        private readonly CharacterRuleSchema schema;
        private readonly string s;

        public CharacterSequenceEngine(CharacterRuleSchema schema, string s)
        {
            this.schema = schema;
            this.s = s;
        }

        public bool Run()
        {
            var context = new CharacterSequenceContext(s);

            bool result = context.LoopUntil(c =>
            {
                foreach (var entry in this.schema.AllEntries)
                {
                    if (!entry.TemporaryCheck(c)) return false;
                }

                return true;
            });

            if (!result)
                return false;
            return this.schema.AllEntries.All(c => c.FinalCheck);
        }
    }

    private class CharacterSequenceContext
    {
        private readonly string s;
        private int _currentPosition;

        public CharacterSequenceContext(string s)
        {
            this.s = s;
            this._currentPosition = 0;

        }
        public char CurrentCharacter
        {
            get
            {
                if (this._currentPosition <= -1 || this._currentPosition >= s.Length)
                    throw new InvalidOperationException();

                return this.s[_currentPosition];

            }
        }

        public bool HasNext => this._currentPosition < this.s.Length;

        public bool StepNext()
        {
            this._currentPosition++;
            return this.HasNext;
        }

        public void Reset()
        {
            _currentPosition = 0;
        }

        public int CurrentPosition { get => _currentPosition; }

        public int Length { get => s.Length; }


        public void LoopOver(Action<CharacterSequenceContext> action)
        {
            Reset();
            while (this.HasNext)
            {
                action(this);
                StepNext();
            }

        }

        public bool LoopUntil(Predicate<CharacterSequenceContext> predicate)
        {
            Reset();
            while (this.HasNext)
            {
                if (!predicate(this))
                    return false;
                StepNext();
            }

            return true;
        }
    }

    private abstract class CharacterRule
    {
        public abstract CharacterEntry Entry { get; }
        public abstract void Invoke(CharacterSequenceContext context);

        public abstract bool IsValid { get; }

        public bool IsTerminated { get; protected set; } = false;
    }


    private sealed class ExistRule : CharacterRule
    {
        private bool _isExist = false;
        public ExistRule(CharacterEntry entry)
        {
            Entry = entry;

        }

        public override bool IsValid => _isExist;

        public override CharacterEntry Entry { get; }

        public override void Invoke(CharacterSequenceContext context)
        {
            if (context.CurrentCharacter == Entry.Character)
                _isExist = true;
        }
    }


    private sealed class FollowedRule : CharacterRule
    {
        private int _lastAppearPosition = -1;
        private char _followingCharacter = ' ';
        private bool _isValid = true;
        public FollowedRule(CharacterEntry entry, char followingChar)
        {
            Entry = entry;
            _followingCharacter = followingChar;
        }
        public override CharacterEntry Entry { get; }

        public override bool IsValid => _isValid;

        public override void Invoke(CharacterSequenceContext context)
        {


            if (_lastAppearPosition == -1)
                return;

            if (_lastAppearPosition + 1 == context.CurrentPosition && context.CurrentCharacter != _followingCharacter)
            {
                _isValid = false;
                IsTerminated = true;
            }

            if (context.CurrentCharacter == Entry.Character)
            {
                _lastAppearPosition = context.CurrentPosition;

            }
        }
    }

    private class AppearAtPositionRule : CharacterRule
    {
        private int _position = -1;
        private bool _isValid = false;



        public AppearAtPositionRule(CharacterEntry entry, int position)
        {
            Entry = entry;
            _position = position;
        }

        public override CharacterEntry Entry { get; }

        public override bool IsValid => _isValid;

        public override void Invoke(CharacterSequenceContext context)
        {
            if (context.CurrentPosition != _position)
                return;
            IsTerminated = true;
            _isValid = context.CurrentCharacter == Entry.Character;
        }
    }

    private class FrequencyRule : CharacterRule
    {

        private readonly ComparisonOperator comparisonOperator;
        private readonly int frequency;
        private int _counter = 0;
        public enum ComparisonOperator : ushort
        {
            LessThan = 0,
            LessThanOrEqual = 1,
            GreaterThan = 2,
            GreaterThanOrEqual = 3,
            Equal = 4
        }

        public FrequencyRule(CharacterEntry entry, ComparisonOperator comparisonOperator, int frequency)
        {
            this.comparisonOperator = comparisonOperator;
            this.frequency = frequency;
            Entry = entry;
        }
        public override CharacterEntry Entry { get; }

        public override bool IsValid => comparisonOperator switch
        {
            ComparisonOperator.LessThan => _counter < frequency,
            ComparisonOperator.GreaterThan => _counter > frequency,
            ComparisonOperator.Equal => _counter == frequency,
            ComparisonOperator.GreaterThanOrEqual => _counter >= frequency,
            ComparisonOperator.LessThanOrEqual => _counter <= frequency,
            _ => false
        };

        public override void Invoke(CharacterSequenceContext context)
        {
            if (context.CurrentCharacter != Entry.Character)
                return;
            _counter++;
        }
    }


    private class NegationRule : CharacterRule
    {
        private readonly CharacterRule innerRule;

        public NegationRule(CharacterRule innerRule)
        {
            this.innerRule = innerRule;
        }
        public override CharacterEntry Entry => innerRule.Entry;

        public override bool IsValid => !innerRule.IsValid;

        public override void Invoke(CharacterSequenceContext context)
        {
            innerRule.Invoke(context);
        }
    }

    private class ExpressionRule<TState> : CharacterRule
    {
        private Action<CharacterSequenceContext, TState> OnIvokingCalling;

        private Action<int, TState> OnMatchingCharacterCalling;
        private readonly bool shouldCallMatchingCallFirst;
        private Predicate<TState> HowIsValid;

        public TState State { get; set; }

        public ExpressionRule(CharacterEntry entry,
                              Predicate<TState> howIsValid,
                              Action<CharacterSequenceContext, TState>? onIvokingCalling = null,
                              Action<int, TState>? onMatchingCharacterCalling = null,
                              bool shouldInvokeMatchingCallerFirst = false)
        {
            Entry = entry;
            OnIvokingCalling = onIvokingCalling ?? ((_, _) => { });
            OnMatchingCharacterCalling = onMatchingCharacterCalling ?? ((_, _) => { });
            this.shouldCallMatchingCallFirst = shouldInvokeMatchingCallerFirst;
            HowIsValid = howIsValid;
        }
        public override CharacterEntry Entry { get; }

        public override bool IsValid => HowIsValid(this.State);

        public override void Invoke(CharacterSequenceContext context)
        {
            if (shouldCallMatchingCallFirst && context.CurrentCharacter == Entry.Character)
            {
                OnMatchingCharacterCalling(context.CurrentPosition, this.State);
                OnIvokingCalling(context, this.State);
            }
            else if (context.CurrentCharacter == Entry.Character)
            {
                OnIvokingCalling(context, this.State);
                OnMatchingCharacterCalling(context.CurrentPosition, State);
            }
            else OnIvokingCalling(context, this.State);
        }


    }

    private partial class CharacterEntry
    {
        public char Character { get; init; }

        public IDictionary<string, CharacterRule> RuleMap { get; private init; } = new Dictionary<string, CharacterRule>();

        public void AddRule(string name, CharacterRule rule)
        {
            RuleMap.Add(name, rule);
        }

        public CharacterRule? GetRule(string name)
        {
            return RuleMap.TryGetValue(name, out var value) ? value : null;
        }

        public bool TemporaryCheck(CharacterSequenceContext context)
        {
            foreach (var rule in RuleMap.Values)
            {
                rule.Invoke(context);
                if (rule.IsTerminated && !rule.IsValid)
                    return false;
            }
            return true;
        }

        public bool FinalCheck => RuleMap.Values.All(x => x.IsValid);

        public void DropRule(string ruleName)
        {
            if (RuleMap.ContainsKey(ruleName))
                RuleMap.Remove(ruleName);
        }

    }

    private partial class CharacterEntry
    {
        public CharacterEntry IncludeExistRule()
        {
            var rule = new ExistRule(this);

            this.AddRule("exist-rule", rule);

            return this;
        }

        public CharacterEntry IncludeAppearPositionRule(int position)
        {
            var rule = new AppearAtPositionRule(this, position);

            this.AddRule($"appear-position-{position}", rule);

            return this;
        }

        public CharacterEntry IncludeFollowedRule(char followingCharacter)
        {
            var rule = new FollowedRule(this, followingCharacter);

            this.AddRule($"followed-by-{followingCharacter}", rule);

            return this;
        }


    }

    public void Initialize()
    {
        throw new NotImplementedException();
    }


    public bool Solve()
    {
        var schema = new CharacterRuleSchema();

        schema.HasAllPossibleCharacters("+-.eE0123456789");

        return true;

    }
}
